import React, { useState, useEffect} from "react";
import '../App.css';
import axios from 'axios';
import { useParams } from "react-router-dom";



const Eachpage = () => {
    const [chainData, setChainData] = useState(undefined);
    const params = useParams();


    useEffect(() =>{
        async function fetchData(){
            try{
                let studentID = params.id;  
                const data = await axios.get('http://127.0.0.1:5000/chain');
                setChainData(data.data[studentID]);
                console.log(data.data[studentID])
                
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
                This is the Homework detials:
            </h1>

            <p className ='Common_description'>Student's ID : {chainData&&chainData[0]}</p>
            <p className ='Common_description'>Course Number: {chainData&&chainData[1]} </p>
            <p className ='Common_description'>Homework: </p>
            <p className ='Common_description'>{chainData&&chainData[2]}</p>
        </div>
    );
};

export default Eachpage;