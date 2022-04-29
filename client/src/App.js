import './App.css';
import { BrowserRouter, Route, Routes, Navigate, Link, Outlet } from 'react-router-dom';

import LoginPage from './Pages/LoginPage/LoginPage'
import RegisterPage from './Pages/RegisterPage/RegisterPage'
import InvestorPage from './Pages/InvestorPage/InvestorPage';
import BuyAndSellPage from './Pages/BuyAndSellPage';
import FundInfo from './Pages/FundInfoPage/FundInfo';

function App() {

  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Navigate replace to="/login" />} />
          <Route path="account" element={<AccountLayout />} >
            <Route path="dashboard" element={<InvestorPage />} />
          </Route>
          <Route path="login" element={<LoginPage />} />
          <Route path="register" element={<RegisterPage />} />
          <Route path="trade" element={<BuyAndSellPage />} />
          <Route path="fundinfo" element={<FundInfo />} />

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
