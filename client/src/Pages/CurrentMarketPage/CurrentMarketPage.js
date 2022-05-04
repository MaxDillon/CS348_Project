import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import styles from "./currentMarketPage.module.css";

async function getMarkets() {
	var res = await fetch("/current/getMarket")
		.then(res => res.json())
		.then(data => {
			return data
		})
	return res
}

export default function TransactionPage() {
	const [contacts, setContacts] = useState({ 'data': [] });

	const navigate = useNavigate()

	useEffect(async () => {
		var newContacts = await getMarkets()
		setContacts(newContacts)
	}, [])

	return (
		<div className={styles.currentTable}>
			<h1>Markets:</h1>
			<table className="table1">
				<thead>
					<tr className="tr1">
						<th className="th1">Company ID</th>
						<th className="th1">Company Name</th>
						<th className="th1">Number Of Shares</th>
						<th className="th1">Current Trading Price</th>
						<th className="th1">Action </th>
					</tr>
				</thead>
				<tbody>

					{

						contacts.data.map(company => {
							return (
								<tr key={company.company_id}>
									<td className="td1">{company.company_id}</td>
									<td className="td1">{company.company_name}</td>
									<td className="td1">{company.num_shares}</td>
									<td className="td1">{company.current_trading_price}</td>
									<td> <button type="button" onClick={() => {
										navigate('/account/trade/' + company.company_id)
									}}>Buy/Sell</button></td>
								</tr>
							)
						})
					}

				</tbody>
			</table>

		</div>
	);
}
