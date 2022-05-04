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

function Navbar({ fundName }) {
   const navigate = useNavigate()

   const [sidebar, setSidebar] = useState(false);

   function toggleSidebar() {
      setSidebar(!sidebar)
   }

   return (
      <div>
         <div className={styles.menu_bar}>
            <Link to="#" className={styles.menu_icon}>
               <FaIcons.FaBars onClick={toggleSidebar} />
            </Link>
            <span>{fundName}</span>

         </div>

         <nav className={sidebar ? styles.menu_dropdown : cx(styles.menu_dropdown, styles.hidden)}>
            <ul className={styles.menu_items}>
               <li className={styles.exit_button}>
                  <Link to="#" className="menu-bars" >
                     <AiIcons.AiOutlineClose onClick={toggleSidebar} size={40} color="white" />
                  </Link>
               </li>
               <Navlink Icon={FaIcons.FaDoorOpen} onClick={() => { logout(navigate) }} text="Logout" />
               <Navlink Icon={FaIcons.FaDesktop} path="/account/dashboard" text="Dashboard" />
               <Navlink Icon={AiIcons.AiOutlineClose} path="/account/fundInfo" text="Fund Info" />
               <Navlink Icon={AiIcons.AiOutlineClose} path="/account/fundgraph" text="Fund Graph" />
               <Navlink Icon={AiIcons.AiOutlineClose} path="/account/transaction" text="Transaction" />
               <Navlink Icon={AiIcons.AiOutlineClose} path="/account/current" text="Current Market" />
            </ul>
         </nav>
      </div>
   )
}

export default Navbar



function Navlink({ Icon, path, text, onClick }) {
   const [isHover, setIsHover] = useState(false);
   const navigate = useNavigate()

   return (
      <>
         <li onClick={e => {
            e.preventDefault()
            if (onClick) { onClick() }
            else if (path) { navigate(path) }

         }} className={isHover ? cx(styles.menu_item, styles.hover) : styles.menu_item}
            onMouseOver={() => setIsHover(true)}
            onMouseOut={() => setIsHover(false)}>
            <Icon />
            <span>{text}</span>
         </li>
      </>
   )
}