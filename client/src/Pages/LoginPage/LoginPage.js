import React from 'react'
import { LoginPanel } from './Components/LoginPanel'
import {useState, useEffect} from 'react'
import { useNavigate } from 'react-router-dom';
import sha256 from 'crypto-js/sha256'

async function loginUser(username, password) {

	const res = await fetch('/login/login', {
		method: 'POST',
		headers: {
		  'Content-Type': 'application/json'
		},
		body: JSON.stringify({
			'username': username,
			'password': sha256(password).toString()
		})
	})

	return res.status != 401
}



export default function LoginPage() {
	const navigate = useNavigate()

	async function onSubmit(username, password) {
		const success = await loginUser(username, password)
		if (success) {
			navigate("/dashboard")
			return true
		} else {
			navigate("/login")
			return false
		}
	}


	return (
		<div>
			<h1>Login Page</h1>
			<LoginPanel loginUser={onSubmit} />
		</div>
	);
}

