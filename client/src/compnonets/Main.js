import React from "react";
import '../App.css';
import { useNavigate } from "react-router-dom";



const Main = () => {
    const navigate = useNavigate();


    const student = () =>{
        navigate('/student');
    }

    const teacher = () =>{
        navigate('/teacher');
    }

    const regist = () =>{
        navigate('/regist');
    }

    return (
        <div>
            <h1 className="description_intro">
                Welcome to BlockChain Homework Center
            </h1>
            <h2 className = 'description_intro'>Where you wan to go?</h2>
            <div className="ButtonArea">
            <button className="mainButton" onClick={student}>
            Go to Students page
            </button>

            <button className="mainButton"  onClick={teacher}>
            Go to Teacher page
            </button>
            </div>

            <p className="regist_intro">Need to regist or drop your course?</p>

            <button className = 'MainRegistButton' onClick={regist}>
            Course Change
            </button>

        </div>
    );
};

export default Main;