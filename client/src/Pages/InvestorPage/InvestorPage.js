import React from "react";
import {useState, useEffect} from 'react'
import { useNavigate } from 'react-router-dom';



async function logout() {
	const res = await fetch('/login/logout')
	return res
}

export default function InvestorPage() {
	const [state, setState] = useState("")
	const navigate = useNavigate()

	useEffect(() => {
		fetch('/login/isLoggedIn')
		.then(response => response.json())
		.then(data => {
			console.log(data)
			if (data.answer === false) {
				navigate("/login")
				return
			}
			setState(data['message'])
		})
	}, [])


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
 
 