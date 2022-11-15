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

    return (
        <div>
            <h1 className="description_intro">
                This is the Main web page.
            </h1>
            <h2>Where you wan to go?</h2>
            <button onClick={student}>
            Go to Students page
            </button>

            <button onClick={teacher}>
            Go to Teacher page
            </button>

        </div>
    );
};

export default Main;