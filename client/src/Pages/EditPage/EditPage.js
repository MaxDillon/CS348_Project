import React from "react";
import {useState, useLayoutEffect} from 'react'
import { useNavigate } from 'react-router-dom';
import './Edit.css'
export default function EditPage() {
    const users = [{
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
    const userDetails = {
        user: "User1",
        name: "Name1",
        money: 1234
    }
    const userList = users.map(user => (<li>
        <div className={"stackIt"}>{user.user} button</div>
        <div className={"stackIt"}>{user.name} button</div>
        <div className={"stackIt"}>{user.money} button</div>
        </li>))
    return (
        <div> <h1>Your Profile</h1> 
            <ul>
                {userList}
            </ul>
        </div>

    );
}