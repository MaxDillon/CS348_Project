import React from "react";
import {useState, useLayoutEffect} from 'react'
import { useNavigate } from 'react-router-dom';



async function logout() {
	const res = await fetch('/auth/logout')
	return res
}

export default function InvestorPage() {
	const navigate = useNavigate()


	return (
	  <div className="App">
		  <button onClick={e => {
				e.preventDefault()
				logout()
				navigate("/login")
		  }}>Logout</button>
	  </div>
	);
 }
 
 