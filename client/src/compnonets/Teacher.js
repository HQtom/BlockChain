import React, { useState, useEffect} from "react";
import '../App.css';
import axios from 'axios';
import {useParams, Link } from "react-router-dom";


const Teacher = () => {
    const [chainData, setChainData] = useState(undefined);


    useEffect(() =>{
        async function fetchData(){
            try{
                const data = await axios.get('http://127.0.0.1:5000/chain');
                setChainData(data.data);
                console.log(data.data)
                
            }
            catch(e){
                // console.log(e)
            }
        }
        fetchData();

    }, []);
    return (
        <div>
            <h1 className="description_intro">
                This is the Teacher page.
            </h1>

            <h2>The block contain following chains</h2>
            <ul>
            {chainData && chainData.map((chainListData)=> 
                <li  key = {chainListData.p_hash}>
                <Link to={`/eachchain/${chainListData.hash}`}>
                    {chainListData.hash}
                </Link>
                </li>)}
            </ul>


        </div>
    );
};

export default Teacher;