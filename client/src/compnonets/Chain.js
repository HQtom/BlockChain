import React, { useState, useEffect} from "react";
import '../App.css';
import axios from 'axios';


const Chain = () => {
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
                This is the block Web page.
            </h1>

            <h2></h2>


        </div>
    );
};

export default Chain;