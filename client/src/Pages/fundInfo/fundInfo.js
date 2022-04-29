import React,{useState} from 'react';
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
	const [contacts, setContacts] = useState([]);
	useEffect(async () => {
		var newContacts = await getContacts()
		//console.log("answer: ", newContacts)
		setContacts(newContacts)

	}, [])
	return (
		<div classname="second-container">
			
			<table class="table2"  >
				<tr>
            		<td colspan = "3"  class="td2">Fund Information</td>
         		</tr>
				{contacts.map((contacter)=>(
         			<tr>
            			<td class="td2">Fund Name: </td>
            			<td class="td2">{contacter.fund_name}</td>
         			</tr>
				))}
				{contacts.map((contacter)=>(
         			<tr>
            			<td class="td2">Fund Description: </td>
						<td class="td2">value: ${contacter.fund_description}</td>
         			</tr>
				))}
				{contacts.map((contacter)=>(
         			<tr>
            			<td class="td2">Fund Value: </td>
            			<td class="td2">name: {contacter.fund_value}</td>
         			</tr>
				))}
				{contacts.map((contacter)=>(
         			<tr>
            			<td class="td2">Fund Invested: </td>
						<td class="td2">value: ${contacter.fund_invested}</td>
         			</tr>
				))}
				{contacts.map((contacter)=>(
         			<tr>
            			<td class="td2">Parent Company: </td>
            			<td class="td2">name: {contacter.parent_company}</td>
         			</tr>
				))}
				
      		</table>
		</div>
	);
}

