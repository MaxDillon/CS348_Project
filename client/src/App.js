
import { BrowserRouter, Route, Routes, Navigate, Link, Outlet } from 'react-router-dom';

import LoginPage from './Pages/LoginPage/LoginPage'
import RegisterPage from './Pages/RegisterPage/RegisterPage'
import InvestorPage from './Pages/InvestorPage/InvestorPage';
import EditPage from './Pages/EditPage/EditPage';
import { useLayoutEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import Navbar from './Pages/AccountWrapper/Components/Navbar';
import AccountWrapper from './Pages/AccountWrapper/AccountWrapper';


function App() {

  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Navigate replace to="/login"/>} />
          <Route path="account" element={<AccountWrapper />} >
            <Route path="dashboard" element={<InvestorPage/>} />
            <Route path="test" element={<div style={{'text-align': 'center'}}> Test Stuff </div>} />
            <Route path="edit" element={<EditPage />} />
          </Route>
          <Route path="login" element={<LoginPage/>} />
          <Route path="register" element={<RegisterPage/>} />
        </Routes>

      </BrowserRouter>
    </div>
  );
}


export default App;
