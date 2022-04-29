import React, {useEffect, useState} from 'react';
import "./transactions.css";
import data from './trans_data.json';


async function getContacts() {
	var res = await fetch("/transactions/getTransactions")
	.then(res => res.json())
	.then( data => {
		return data
	})

}

export default function TransactionPage() {
	const [contacts, setContacts] = useState({});

	useEffect(async() => {
		var newContacts = await getContacts()

		setContacts(newContacts)

	}, [])

	return (
		<div classname="app-container">
			<h1>Transaction History:</h1>
			<table class= "table1">
				<thead>
					<tr class = "tr1">
    					<th class="th1">Company ID</th>
    					<th class="th1">Number Of Shares</th>
						<th class="th1">Buy/Sell</th>
    					<th class="th1">Time</th>
  					</tr>
				</thead>
				<tbody>
					
						<tr>
    						<td class="td1">{contacts.companyId}</td>
    						<td class="td1">{contacts.buySell}</td>
   			 				<td class="td1">{contacts.companyId}</td>
    						<td class="td1">{contacts.sharesHeld}</td>
  						</tr>
					
				</tbody>
			</table>

		</div>
	);
}



/*<table class= "table1">
<thead>
<tr class = "tr1">
	<th class="th1">Employee ID</th>
	<th class="th1">Buy/Sell</th>
	<th class="th1">Company ID</th>
	<th class="th1">Shares Held</th>
  </tr>
</thead>
<tbody>
{contacts.map((contact)=>(
		<tr>
		<td class="td1">{contact.companyId}</td>
		<td class="td1">{contact.buySell}</td>
			<td class="td1">{contact.companyId}</td>
		<td class="td1">{contact.sharesHeld}</td>
	  </tr>
))}

</tbody>
</table>
*/