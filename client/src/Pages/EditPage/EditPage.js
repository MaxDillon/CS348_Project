import React from 'react';
import {useState, useEffect} from 'react'
import { useNavigate } from 'react-router-dom';
import './Edit.css'
import Field from './Field.js'

async function getUserdetails() {
	var res = await fetch("/edit/getUser")
	.then(res => res.json())
	.then( data => {
		return data
	})

}

export default function EditPage(props) {
    const [details, setDetails] = useState({});

    useEffect(async () => {
        var details = await fetch("/edit/getUser")
        .then(res => res.json())
        .then( data => {
            setDetails(data)
        })

    }, [])
    
    return (
        <div> <h1>Your Profile</h1> 
        <div>
    
            <ul className={"verticalSpace"}>
                <Field name="Username" field="user_id" id={details.user_id} value={details.username}></Field>
                <Field name="First Name" field="first_name" id={details.user_id} value={details.first_name}></Field>
                <Field name="Last Name" field="last_name" id={details.user_id} value={details.last_name}></Field>
                <Field name="Email" field="email" id={details.user_id} value={details.email}></Field>
                <Field name="Phone Number" field="phone" id={details.user_id} value={details.phone}></Field>
                <Field name="Money Invested" field="money_invested" id={details.user_id} value={details.money_invested}></Field>

            </ul>
        </div>
        </div>

    );
}