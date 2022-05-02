from datetime import datetime
import sys
from sqlalchemy.orm import Session
from sqlalchemy import Float, Integer, alias, select, func
from database.schema import (
    Account,
    t_paymenthistory,
    t_companyhistory,
    t_fundperformance,
)
import numpy as np


def get_fund_fitness(session: Session, time):
    query = select(t_fundperformance).where(
        t_fundperformance.columns.time_created == (
            select(func.max(t_fundperformance.columns.ts)).where(
                t_fundperformance.columns.ts <= time
            )
        )
    )
    result = session.execute(query).one_or_none()

    return 0 if not result else result.fund_value


def get_past_holdings(session: Session, account: Account, time_start: float, time_end: float):
    time_start = 0
    time_end = 100

    times = []
    values = []

    last_invested = 0
    last_investment = 0
    last_fund_fitness = 0
    for time in np.linspace(time_start, time_end, 500):
        query = select(t_paymenthistory).where(
            t_paymenthistory.columns.time_created == (
                select(func.max(t_paymenthistory.columns.time_created)).where(
                    t_paymenthistory.columns.time_created <= time
                )
            )
        )
        result = session.execute(query).one_or_none()
        if result.time_created != last_invested:
            last_invested = result.time_created
            last_investment = result.money_invested
            times.append(time)
            values.append(result.money_invested)
            last_fund_fitness = get_fund_fitness(session, result.time_created)
            continue

        
        new_fund_fitness = get_fund_fitness(session, time)
        times.append(time)
        values.append(new_fund_fitness / last_fund_fitness * last_investment)

        







def get_past_holding_dump(
    session: Session, account: Account, time_start: float, time_end: float
):

    time_start = 0
    time_end = 100000

    time_created = t_paymenthistory.columns.time_created
    # amount_invested = t_paymenthistory.columns.amount_invested
    # user_id = t_paymenthistory.columns.user_id
    # time_fetched = t_companyhistory.columns.time_fetched
    # trading_price = t_companyhistory.columns.trading_price
    # company_id = t_companyhistory.columns.company_id

    ret = []

    query = select(
        t_fundperformance.columns.fund_value.cast(Float),
        t_fundperformance.columns.ts,
    ).where(
        t_fundperformance.columns.ts >= time_start,
        t_fundperformance.columns.ts <= time_end,
    )

    ranged_performances = session.execute(query).all()
    for performance in ranged_performances:


        query = select(t_paymenthistory.columns.amount_invested.cast(Float), time_created).where(
            time_created == (
                select(func.max(time_created)).where(time_created <= performance.ts)
            )
            # , t_paymenthistory.columns.user_id == account.user_id
        )
        current_investment = session.execute(query).fetchone()

        amount_invested = 0 if not current_investment else current_investment.amount_invested

        ret.append((amount_invested, performance.fund_value, float(performance.ts)))

    return ret