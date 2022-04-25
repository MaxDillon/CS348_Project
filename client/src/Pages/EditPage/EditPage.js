import React from "react";
import {useState, useLayoutEffect} from 'react'
import { useNavigate } from 'react-router-dom';
import './Edit.css'
import Field from './Field.js'

export default function EditPage(props) {
    const [details, setDetails] = useState([]);
    const users = [
        {
        user: "User1",
        name: "Name1",
        money: 1234
    }, {
        user: "User2",
        name: "Name1",
        money: 1234
    }, {
        user: "User3",
        name: "Name1",
        money: 1234
    }]
    const userDetails = 
        {
        user: "User1",
        name: "Name1",
        money: 1234,
        email: "email@i1232"
    }
    const test = [];


    for(const[key, value] of Object.entries(userDetails)) {
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