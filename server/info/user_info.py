

from datetime import datetime
import sys
from sqlalchemy.orm import Session
from sqlalchemy import alias, select, func
from database.schema import Account, t_paymenthistory, t_companyhistory



def get_time_range(session: Session, account: Account, time_start: int, time_end: int):

	time_created = t_paymenthistory.columns.time_created
	earliest_query = select(func.min(time_created)).where(t_paymenthistory.columns.user_id == account.user_id).having(func.min(time_created) >= time_start)
	start_time = session.execute(earliest_query).one_or_none()

	latest_query = select(func.max(time_created)).where(t_paymenthistory.columns.user_id == account.user_id).having(func.max(time_created) <= time_end)
	end_time = session.execute(latest_query).one_or_none()

	return (start_time, end_time)

def get_past_holding_dump(session: Session, account: Account, time_start: datetime, time_end: datetime):
	
	start_time, end_time = get_time_range(session, account, time_start, time_end)
	if start_time is None or end_time is None:
		return None
	
	time_created = t_paymenthistory.columns.time_created
	amount_invested = t_paymenthistory.columns.amount_invested
	user_id = t_paymenthistory.columns.user_id
	time_fetched = t_companyhistory.columns.time_fetched

	query = select(time_fetched)# .where(time_fetched >= start_time, time_fetched <= end_time)
	print(query, file=sys.stderr)

	times = session.execute(query).all()

	print("values", start_time, end_time, times, file=sys.stderr)



	
	
	return []

