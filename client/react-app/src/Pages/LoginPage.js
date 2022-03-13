import React from 'react'
import { LoginPrompt } from '../Components/LoginPrompt/LoginPrompt'
import {useState, useEffect} from 'react'

export const LoginPage = () => {
	const [state, setState] = useState([])
 
	useEffect(() => {
	  fetch('/getDate').then(response => {
		 if (response.status === 200) {
			return response.json()
		 }
	  }).then(data => setState(data))
	}, [])

	return (
		<div>
			<LoginPrompt data={state}/>
		</div>
	);
}