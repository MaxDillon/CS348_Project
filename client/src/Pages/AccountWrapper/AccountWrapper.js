import React from 'react'
import { Outlet, useNavigate } from 'react-router-dom'
import { useLayoutEffect } from 'react' 
import Navbar from './Components/Navbar'

function AccountWrapper() {
  const navigate = useNavigate()

	useLayoutEffect(() => {

    fetch('/auth/isLoggedIn')
		.then(response => response.json())
		.then(data => {
			if (data.answer === false) {
				navigate("/login")
				return
			}
		})
	}, [navigate])

  return (
    <div>
      <Navbar fundName="CS348 Investing Fund"/>
      <div className="content">
        <Outlet />
      </div>
    </div>
  );
}
export default AccountWrapper