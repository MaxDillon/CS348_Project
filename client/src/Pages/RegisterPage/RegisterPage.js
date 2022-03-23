import React from 'react'
import { RegisterPanel } from './Components/RegisterPanel';
import {useState, useEffect} from 'react'
import { useNavigate } from 'react-router-dom';
import sha256 from 'crypto-js/sha256'

async function registerUser(email, username, password) {
	const res = await fetch('/login/register', {
		method: 'POST',
		headers: {
		  'Content-Type': 'application/json'
		},
		body: JSON.stringify({
			'email': email,
			'username': username,
			'password': sha256(password).toString()
		})
	})

	return res.status < 400 || res.status >= 500
}



export default function RegisterPage() {
	const navigate = useNavigate()

	async function onSubmit(email, username, password) {
		const success = await registerUser(email, username, password)

		if (success) {
			navigate("/abc")
			return true
		} else {
			navigate("/register")
			return false
		}
	}


	return (
		<div>
			<h1>Login Page</h1>
			<RegisterPanel registerUser={onSubmit} />
		</div>
	);
}

