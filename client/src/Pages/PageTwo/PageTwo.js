import React,{useState} from 'react';
import "./second.css";
import values from './second_data.json';
export default function PageTwo() {
	const [contacts, setContacts] = useState(values);
	return (
		<div classname="second-container">
			
			<table class="table2" >
			{contacts.map((contacter)=>(
         		<tr>
            		<td class="td2">Amount: ${contacter.Amount} </td>
         		</tr>
			))}
      		</table>
			<table class="table2"  >
				<tr>
            		<td colspan = "3"  class="td2">Fund Information</td>
         		</tr>
				{contacts.map((contacter)=>(
         			<tr>
            			<td class="td2">Name: </td>
            			<td class="td2">name: {contacter.Name}</td>
         			</tr>
				))}
				{contacts.map((contacter)=>(
         			<tr>
            			<td class="td2">Value: </td>
						<td class="td2">value: ${contacter.Value}</td>
         			</tr>
				))}
				
      		</table>
		</div>
	);
}

