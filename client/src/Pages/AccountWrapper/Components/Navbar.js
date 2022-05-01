import React from 'react'
import styles from '../accountWrapper.module.css'
import { Link, useNavigate } from 'react-router-dom'
import * as FaIcons from 'react-icons/fa'
import * as AiIcons from 'react-icons/ai'
import { useState } from 'react'

async function logout(navigate) {
	await fetch('/auth/logout')
   .then(() => navigate("/login"))
}

function Navbar() {
   const navigate = useNavigate()

   const [sidebar, setSidebar] = useState(false);
   
   function toggleSidebar() {
      setSidebar(!sidebar)
   }

   return (
      <div>
         <div>
            <Link to="#" className="menu-bars">
               <FaIcons.FaBars onClick={toggleSidebar}/>
            </Link>
         </div>
         
         <nav className={sidebar ? "nav-menu active" : "nav-menu"}>
            <ul className="nav-menu-items">
               <li className="navbar-toggle">
                  <Link to="#" className="menu-bars" >
                     <AiIcons.AiOutlineClose onClick={toggleSidebar}/>
                  </Link>
               </li>
               <Navlink Icon={AiIcons.AiOutlineClose} onClick={()=>{logout(navigate)}} text="Logout"/>
               <Navlink Icon={AiIcons.AiOutlineClose} onClick={()=>{logout(navigate)}} text="Logout"/>
               <Navlink Icon={AiIcons.AiOutlineClose} onClick={()=>{logout(navigate)}} text="Logout"/>
               <Navlink Icon={AiIcons.AiOutlineClose} onClick={()=>{logout(navigate)}} text="Logout"/>

            </ul>
         </nav>
      </div>
      )
   }
   
   export default Navbar



   function Navlink({ Icon, nav, text, onClick}) {

      return (
         <>
            <li>
               {onClick ? 
                  <div onClick={e => {
                     e.preventDefault()
                     onClick()
                  }}>
                  <Icon />
                  <span>{text}</span>
                  </div>:
                  <Link to={nav}>
                  <Icon />
                  <span>{text}</span>
                  </Link>
               }
            </li>
         </>
      )
   }