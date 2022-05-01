import React from 'react'
import { LoginPanel } from './Components/LoginPanel'
import { useLayoutEffect } from 'react'
import { useNavigate } from 'react-router-dom';
import sha256 from 'crypto-js/sha256'
import styles from './loginPage.module.css'

async function loginUser(username, password) {

	const res = await fetch('/auth/login', {
		method: 'POST',
		headers: {
		  'Content-Type': 'application/json'
		},
		body: JSON.stringify({
			'username': username,
			'password': sha256(password).toString()
		})
	})

	return res.status !== 401
}



export default function LoginPage() {
	const navigate = useNavigate()

	useLayoutEffect(() => {
		fetch('/auth/isLoggedIn')
		.then(response => response.json())
		.then(data => {
			if (data.answer === true) {
				navigate("/account/dashboard")
			}
			return data.answer
		}).then(answer => console.log(answer))
	}, [navigate])


	async function onSubmit(username, password) {
		const success = await loginUser(username, password)
		if (success) {
			navigate("/account/dashboard")
			return true
		} else {
			navigate("/login")
			return false
		}
	}


	return (
		<div className={styles.loginPage}>
			<h1>Login Page</h1>
			<LoginPanel loginUser={onSubmit} />
		</div>
	);
}

