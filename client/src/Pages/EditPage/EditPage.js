import React from "react";
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
    const [details, setDetails] = useState([]);
    useEffect(async () => {
		var details = await getUserdetails()
		setDetails(details)

    }, [])
    
    const userDetails = 
        {
        user: "User1",
        name: "Name1",
        money: 1234,
        email: "email@i1232"
    }
    const test = [];
    console.log(details)

    for(const[key, value] of Object.entries(details)) {
        console.log(key, value)
        test.push([key, value]);
    }

    const userList = test.map(field => (
        <div className={"stackIt"}>{field[0]} {field[1]} button</div>
        
        )
        )

    const users1 = test.map(field => (
        <Field details={field} id={field[0]}/>        
        )
    )

    return (
        <div> <h1>Your Profile</h1> 
        <div >
    
                 <ul className={"verticalSpace"}>
                {users1}
                </ul>
        </div>
        </div>

    );
}