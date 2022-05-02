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
                <Field name="Username" field="username" value={details.username}/>
                <Field name="First Name" field="first_name" value={details.first_name}/>
                <Field name="Last Name" field="last_name" value={details.last_name}/>
                <Field name="Email" field="email" value={details.email}/>
                <Field name="Phone Number" field="phone" value={details.phone}/>

            </ul>
        </div>
        </div>

    );
}