import './App.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom';

import LoginPage from './Pages/LoginPage/LoginPage'
import RegisterPage from './Pages/RegisterPage/RegisterPage'
import { useState } from 'react';
import InvestorPage from './Pages/InvestorPage/InvestorPage';

function App() {
  const [token, setToken] = useState();


  return (
    <div className="App">
      <h1>Application</h1>
      <BrowserRouter>
        <Routes>
          <Route path="/login" element={<LoginPage/>} />
          <Route path="/dashboard" element={<InvestorPage/>} />
          <Route path="/register" element={<RegisterPage/>} />
        </Routes>

      </BrowserRouter>
    </div>
  );
}

export default App;
