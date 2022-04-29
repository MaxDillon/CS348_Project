import React, { useEffect, useState } from 'react';
import "./transactions.css";
import data from './trans_data.json';


async function getContacts() {
	var res = await fetch("/transactions/getTransactions")
		.then(res => res.json())
		.then(data => {
			return data
		})
		return res
}

export default function TransactionPage() {
	const [contacts, setContacts] = useState([]);

	useEffect(async () => {
		var newContacts = await getContacts()
		console.log("answer: ", newContacts)
		setContacts(newContacts)

	}, [])

	return (
		<div className="app-container">
			<h1>Transaction History:</h1>
			<table className="table1">
				<thead>
					<tr class="tr1">
						<th class="th1">Company ID</th>
						<th class="th1">Number Of Shares</th>
						<th class="th1">Buy/Sell</th>
						<th class="th1">Time</th>
					</tr>
				</thead>
				<tbody>

					{

						contacts.map(company => {
							return (
								<tr key={company.company_id}>
									<td class="td1">{company.company_id}</td>
									<td class="td1">{company.num_shares}</td>
									<td class="td1">{company.buy_or_sell}</td>
									<td class="td1">{company.time_executed}</td>
								</tr>
							)
						})
					}

				</tbody>
			</table>

		</div>
	);
}

