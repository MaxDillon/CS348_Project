import React from 'react';
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import {useState, useEffect} from 'react'
import PropTypes from 'prop-types';



export function RegisterPanel({registerUser}) {
	const [username, setUsername] = useState("")
	const [password, setPassword] = useState("")
	const [email, setEmail] = useState("")
	const [toggleFailure, setToggleFailure] = useState("")

	function validateForm() {
		return username.length > 0 && password.length > 0 && email.length > 0
	}

	return (
		<div>
			{toggleFailure && 
			<p>
				The Username or Password you entered was Incorrect!
			</p>
			}
			<Form.Group size="lg" controlId="email">
				<Form.Label>Email</Form.Label>
				<Form.Control 
					autoFocus
					type="email"
					value={email}
					onChange={(e) => setEmail(e.target.value)}
				/>
			</Form.Group>
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
					const success = registerUser(email, username, password).then(success => {
						if (!success) {
							setToggleFailure(true)
							setUsername("")
							setPassword("")
							setEmail("")
						}
					})

				}}>
					Login
				</Button>
			</Form.Group>
		</div>
	)
}


RegisterPanel.propTypes = {
	registerUser: PropTypes.func.isRequired,
 }