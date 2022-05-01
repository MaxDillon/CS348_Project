import React from 'react'
import { Outlet, useNavigate } from 'react-router-dom'
import { useState, useLayoutEffect } from 'react' 

import Navbar from './Components/Navbar'

function AccountWrapper() {
  const navigate = useNavigate()
  const [canDisplay, setCanDisplay] = useState(false);

	useLayoutEffect(() => {

    fetch('/auth/isLoggedIn')
		.then(response => response.json())
		.then(data => {
			if (data.answer === false) {
				navigate("/login")
				
			} else {
        setCanDisplay(true)
      }
		})
	}, [])

  return (
  
    <>
      {canDisplay ?
        <div>
          <Navbar fundName="CS348 Investing Fund"/>
          <div className="content">
            <Outlet />
          </div>
        </div>
      : <></>}

    </>
  );
}
export default AccountWrapper