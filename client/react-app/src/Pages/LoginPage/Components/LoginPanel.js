import React from 'react'
import styles from '../loginPage.module.css'
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import {useState, useEffect} from 'react'
import PropTypes from 'prop-types';



export function LoginPanel({loginUser}) {
	const [username, setUsername] = useState("")
	const [password, setPassword] = useState("")
	const [toggleFailure, setToggleFailure] = useState(false)

	function validateForm() {
		return username.length > 0 && password.length > 0
	}

	return (
		<div className={styles.loginPanel}>
			{toggleFailure && 
			<p className={styles.errorMessage}>
				The Username or Password you entered was Incorrect!
			</p>
			}
			<Form.Group size="lg" controlId="username">
				<Form.Label>Username</Form.Label>
				<Form.Control 
					autoFocus
					type="username"
					value={username}
					onChange={(e) => setUsername(e.target.value)}
				/>
			</Form.Group>
			<Form.Group size="lg" controlId="password">
				<Form.Label>Password</Form.Label>
				<Form.Control 
					autoFocus
					type="password"
					value={password}
					onChange={(e) => setPassword(e.target.value)}
				/>
			</Form.Group>
			<Form.Group>
				<Button size="lg" type="submit" disabled={!validateForm()} onClick={e => {
					e.preventDefault()
					const success = loginUser(username, password).then(success => {
						if (!success) {
							setToggleFailure(true)
							setUsername("")
							setPassword("")
						}
					})

				}}>
					Login
				</Button>
			</Form.Group>
		</div>
	)
}


LoginPanel.propTypes = {
	loginUser: PropTypes.func.isRequired,
 }