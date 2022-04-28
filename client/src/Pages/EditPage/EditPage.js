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
    const [details, setDetails] = useState({});

    useEffect(async () => {
        var details = await fetch("/edit/getUser")
        .then(res => res.json())
        .then( data => {
            setDetails(data)
        })
		//setDetails(details)

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
    const userId = test.filter(field => field[0] == "user_id");
    //console.log(userId[0][1])

    const users1 = test.map(field => (
        <Field details={field} id={userId[0][1]}/>        
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