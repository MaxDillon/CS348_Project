import './App.css';
import {useState, useEffect} from 'react'
import { LoginPage } from './Components/LoginPage/LoginPage'

function App() {

  const [initialState, setState] = useState([])
  const url = '/api'

  useEffect(() => {
    fetch(url).then(response => {
      if (response.status === 200) {
        return response.json()
      }
    }).then(data => setState(data))
  }, [])

  return (
    <div className="App">
        <p>Doing Something</p>
        <LoginPage data={initialState}/>
    </div>
  );
}

export default App;
