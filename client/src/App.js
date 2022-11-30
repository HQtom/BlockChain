import logo from './logo.svg';
import './App.css';
import Main from './compnonets/Main';
import Eachpage from './compnonets/Eachpage';
import Teacher from './compnonets/Teacher';
import Student from './compnonets/Student';
import Regist from './compnonets/Regist';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';



function App() {
  return (
    <Router>
      <Routes>
        <Route path = '/' element = {<Main />} />
        <Route path = '/student' element = {<Student />} />
        <Route path = '/teacher' element = {<Teacher />} />
        <Route path = '/regist' element = {<Regist />} />
        <Route path = '/eachchain/:id' element = {<Eachpage />} />






      </Routes>

    </Router>

  );
}

export default App;
