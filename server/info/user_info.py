from datetime import datetime
import sys
from sqlalchemy.orm import Session
from sqlalchemy import alias, select, func
from database.schema import Account, t_paymenthistory, t_companyhistory
import numpy as np


def get_past_holding_dump(
    session: Session, account: Account, time_start: float, time_end: float
):

    # start_time, end_time = get_time_range(session, account, time_start, time_end)
    # if start_time is None or end_time is None:
    #     return None

    time_created = t_paymenthistory.columns.time_created
    amount_invested = t_paymenthistory.columns.amount_invested
    user_id = t_paymenthistory.columns.user_id
    time_fetched = t_companyhistory.columns.time_fetched
    trading_price = t_companyhistory.columns.trading_price
    company_id = t_companyhistory.columns.company_id

    ret = []

    for latest_time in np.linspace(time_start, time_end, 100, False):

        user_money_query = (
            select(amount_invested, func.max(time_created))
            .where(user_id == account.user_id, time_created <= latest_time)
            .group_by(amount_invested)
        )

        latest_times = (
            select(company_id, func.max(time_fetched).label("time"))
            .where(time_fetched <= latest_time)
            .group_by(company_id)
            .subquery()
        )

        total_holdings_query = select(func.sum(trading_price).label("price")).where(
            company_id == latest_times.c.company_id, time_fetched == latest_times.c.time
        )

        res = session.execute(total_holdings_query).one()
        ret.append((latest_time, res.price))

    return ret
