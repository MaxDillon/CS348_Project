import React, { useEffect, useState } from 'react';
import "./fund_Info.css";
import values from './fundData.json';

async function getContacts() {
	var res = await fetch("/fundInfo/getFunds")
		.then(res => res.json())
		.then(data => {
			return data
		})
	return res
}

export default function FundInfo() {
	const [contacts, setContacts] = useState({});
	useEffect(() => {
		getContacts()
		.then(data => {
			setContacts(data)
		})

	}, [])
	return (
		<div className="second-container">

			<table className="table2"  >
				<tbody>
					<tr>
						<td colSpan="3" className="td2">Fund Information</td>
					</tr>
					<tr>
						<td className="td2">Fund Name: </td>
						<td className="td2">{contacts.fund_name}</td>
					</tr>
					<tr>
						<td className="td2">Fund Description: </td>
						<td className="td2">{contacts.fund_description}</td>
					</tr>
					<tr>
						<td className="td2">Fund Value: </td>
						<td className="td2">{contacts.fund_value}</td>
					</tr>
					<tr>
						<td className="td2">Fund Invested: </td>
						<td className="td2">{contacts.fund_invested}</td>
					</tr>
					<tr>
						<td className="td2">Parent Company: </td>
						<td className="td2">{contacts.parent_company}</td>
					</tr>
				</tbody>

			</table>
		</div>
	);
}
