import logo from './logo.svg';
import './App.css';
import Main from './compnonets/Main';
import Block from './compnonets/Block';
import Chain from './compnonets/Chain';
import Eachpage from './compnonets/Eachpage';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';



function App() {
  return (
    <Router>
      <Routes>
        <Route path = '/' element = {<Main />} />
        <Route path = '/chain' element = {<Chain />} />
        <Route path = '/block' element = {<Block />} />
        <Route path = '/eachchain/:id' element = {<Eachpage />} />






      </Routes>

    </Router>

  );
}

export default App;