import React from "react";
import {useState, useLayoutEffect} from 'react'
import { useNavigate } from 'react-router-dom';



async function logout() {
	const res = await fetch('/auth/logout')
	return res
}

export default function InvestorPage() {
	const [state, setState] = useState("")
	const navigate = useNavigate()

	useLayoutEffect(() => {
		fetch('/auth/isLoggedIn')
		.then(response => response.json())
		.then(data => {
			console.log(data)
			if (data.answer === false) {
				navigate("/login")
				return
			}
			setState(data['message'])
		})
	}, [navigate])


	return (
	  <div className="App">
		  <p>{state}</p>
		  <button onClick={e => {
				e.preventDefault()
				logout()
				navigate("/login")
		  }}>Logout</button>
	  </div>
	);
 }
 
 