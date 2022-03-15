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
		async function getTestRequired() {
			const res = await fetch('/login/testRequired')
			if (res.status === 401) {
				navigate("/login")
				return
			}
		
			const data = await res.json()
			setState(data['question'])
		}
		getTestRequired()

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
 
 