import './App.css';
import { BrowserRouter, Route, Routes, Navigate, Link, Outlet } from 'react-router-dom';

import LoginPage from './Pages/LoginPage/LoginPage'
import RegisterPage from './Pages/RegisterPage/RegisterPage'
import InvestorPage from './Pages/InvestorPage/InvestorPage';
import EditPage from './Pages/EditPage/EditPage';
import BuyAndSellPage from './Pages/BuyAndSellPage';
import FundInfo from './Pages/FundInfoPage/FundInfo';
import { useLayoutEffect } from 'react';
import { useNavigate } from 'react-router-dom';


function App() {

  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Navigate replace to="/login"/>} />
          <Route path="account" element={<AccountLayout />} >
            <Route path="dashboard" element={<InvestorPage/>} />
          </Route>
          <Route path="login" element={<LoginPage/>} />
          <Route path="register" element={<RegisterPage/>} />
          <Route path="edit" element={<EditPage />} />
        </Routes>

      </BrowserRouter>
    </div>
  );
}

function AccountLayout() {
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
		})
	}, [navigate])

  return (
    <div>
      <h1>Welcome to the app!</h1>
      <nav>
        <Link to=""></Link>
        <Link to=""></Link>
      </nav>
      <div className="content">
        <Outlet />
      </div>
    </div>
  );
}

export default App;
