import React, { useEffect, useState } from 'react';
import "./currentMarketPage.css";

async function getMarkets() {
	var res = await fetch("/current/getMarket")
		.then(res => res.json())
		.then(data => {
			return data
		})
	return res
}

export default function TransactionPage() {
	const [contacts, setContacts] = useState([]);

	useEffect(async () => {
		var newContacts = await getMarkets()
		setContacts(newContacts)
	}, [])

	return (
		<div className="app-container">
			<h1>Markets:</h1>
			<table className="table1">
				<thead>
					<tr class="tr1">
						<th class="th1">Company ID</th>
						<th class="th1">Company Name</th>
						<th class="th1">Number Of Shares</th>
						<th class="th1">Current Trading Price</th>
						
					</tr>
				</thead>
				<tbody>

					{

						contacts.map(company => {
							return (
								<tr key={company.company_id}>
									<td class="td1">{company.company_id}</td>
									<td class="td1">{company.company_name}</td>
									<td class="td1">{company.num_shares}</td>
									<td class="td1">{company.current_trading_price}</td>
								</tr>
							)
						})
					}

				</tbody>
			</table>

		</div>
	);
}
