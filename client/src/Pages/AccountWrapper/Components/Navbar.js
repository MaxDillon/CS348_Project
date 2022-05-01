import React from 'react'
import styles from '../accountWrapper.module.css'
import { Link, useNavigate } from 'react-router-dom'
import * as FaIcons from 'react-icons/fa'
import * as AiIcons from 'react-icons/ai'
import { useState } from 'react'
import cx from 'classnames'

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
         <div className={styles.menu_bar}>
            <Link to="#" className={styles.menu_icon}>
               <FaIcons.FaBars onClick={toggleSidebar}/>
            </Link>
         </div>
         
         <nav className={sidebar ? styles.menu_dropdown : cx(styles.menu_dropdown, styles.hidden)}>
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
      const [isHover, setIsHover] = useState(false);
      return (
         <>
            <li className={isHover ? cx(styles.menu_item, styles.hover): styles.menu_item } 
               onMouseOver={() => setIsHover(true)} 
               onMouseOut={() => setIsHover(false)}>
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