
import { BrowserRouter, Route, Routes, Navigate, Link, Outlet } from 'react-router-dom';

import LoginPage from './Pages/LoginPage/LoginPage'
import RegisterPage from './Pages/RegisterPage/RegisterPage'
import InvestorPage from './Pages/InvestorPage/InvestorPage';
import BuyAndSellPage from './Pages/BuyAndSellPage';
import FundGraph from './Pages/FundInfoPage/FundInfo';
import FundInfo from './Pages/fundInfo/fundInfo'
import TransactionPage from './Pages/transactionPage/transactionPage'
import EditPage from './Pages/EditPage/EditPage';
import CurrentMarketPage from "./Pages/CurrentMarketPage/CurrentMarketPage";
import AccountWrapper from './Pages/AccountWrapper/AccountWrapper';


function App() {

  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Navigate replace to="/login" />} />
          <Route path="account" element={<AccountWrapper />} >
            <Route path="dashboard" element={<InvestorPage />} />
            <Route path="edit" element={<EditPage />} />
            <Route path="fundinfo" element={<FundInfo />} />
            <Route path="fundgraph" element={<FundGraph />} />
            <Route path="trade/:companyID" element={<BuyAndSellPage />} />
            <Route path="transaction" element={<TransactionPage />} />
            <Route path="current" element={<CurrentMarketPage />} />
          </Route>
          <Route path="login" element={<LoginPage />} />
          <Route path="register" element={<RegisterPage />} />
        </Routes>

      </BrowserRouter >
    </div >
  );
}


export default App;
