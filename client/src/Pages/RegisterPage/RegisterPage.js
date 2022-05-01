import React from 'react'
import { RegisterPanel } from './Components/RegisterPanel';
import { useState, useLayoutEffect } from 'react'
import { useNavigate } from 'react-router-dom';
import sha256 from 'crypto-js/sha256'
import loginStyles from '../LoginPage/loginPage.module.css'


async function registerUser(email, username, password) {
	const res = await fetch('/auth/register', {
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
	const [canDisplay, setCanDisplay] = useState(false);

	useLayoutEffect(() => {
		fetch('/auth/isLoggedIn')
		.then(response => response.json())
		.then(data => {
			if (data.answer === true) {
				navigate("/account/dashboard")
			} else {
				setCanDisplay(true)
			}
		})
	}, [])

	async function onSubmit(email, username, password) {
		const success = await registerUser(email, username, password)

		if (success) {
			navigate("/account/dashboard")
			return true
		} else {
			navigate("/register")
			return false
		}
	}


	return (
	<>{ canDisplay ? 
		<div className={loginStyles.loginPage}>
			<h1>Login Page</h1>
			<RegisterPanel registerUser={onSubmit} />
		</div>

		: <></>
	}</>


	);
}

