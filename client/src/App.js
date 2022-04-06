import './App.css';
import { BrowserRouter, Route, Routes, Navigate, Link, Outlet } from 'react-router-dom';

import LoginPage from './Pages/LoginPage/LoginPage'
import RegisterPage from './Pages/RegisterPage/RegisterPage'
import { useState } from 'react';
import InvestorPage from './Pages/InvestorPage/InvestorPage';

function App() {
  const [token, setToken] = useState();


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
        </Routes>

      </BrowserRouter>
    </div>
  );
}

function AccountLayout() {
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
