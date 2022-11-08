import React from "react";
import '../App.css';
import { useNavigate } from "react-router-dom";



const Main = () => {
    const navigate = useNavigate();


    const ChainPage = () =>{
        navigate('/chain');
    }

    const blockPage = () =>{
        navigate('/block');
    }

    return (
        <div>
            <h1 className="description_intro">
                This is the Main web page.
            </h1>
            <h2>What you want to do?</h2>
            <button onClick={ChainPage}>
            Check the Chain
            </button>

            <button onClick={blockPage}>
            Check the block
            </button>

        </div>
    );
};

export default Main;