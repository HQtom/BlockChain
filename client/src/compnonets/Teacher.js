import React, { useState, useEffect } from "react";
import '../App.css';
import axios from 'axios';
import { useParams, Link } from "react-router-dom";


const Teacher = () => {
    const [chainData, setChainData] = useState(undefined);


    


    useEffect(() => {
        async function fetchData() {
            try {
                const data = await axios.get('http://127.0.0.1:5000/chain');
                setChainData(data.data);
                console.log(data.data)

            }
            catch (e) {
                // console.log(e)
            }
        }
        fetchData();

    }, []);

    const setDeadline = async () => {
        
        let inputDate = document.getElementById('new_date').value;
        let inputTime = document.getElementById('new_time').value;
        
 

        await axios.post('http://127.0.0.1:5000/settime', {Date:inputDate,Time: inputTime} )
                .then((res) => { alert("Time Set success")})
                .catch((err) => alert('Can not set this time'));

    }


    return (
        <div>
            <h1 className="description_intro">
                This is the Teacher page.
            </h1>

            <p className="Common_descriptionT"> POST A NEW DEADLINE:</p>
            <div className="Common_descriptionT">
                <div>
                    <label for="new_order_date" id="dateInfo">Choose a date:</label>
                    <input type="text" id="new_date" name="date"></input>


                </div>
            </div>

            <div className="Common_descriptionT" >
                <div>

                    <label for="new_order_time" id="timeInfo">Choose a time:</label>
                        <input type="time" id="new_time" name="time"
                            required />
                        </div>
                </div>

                <button
                    className="StudentPageButton"
                    // disabled={!selectedFiles}
                    onClick={setDeadline}>
                    Post a homework Deadline
                </button>

                <h2 className="Common_descriptionT">The Homework information student upload</h2>
                <ul className="Common_descriptionT">
                    {chainData && chainData.map((chainListData) =>
                        <li className="listInfo" key={chainListData}>
                            <Link to={`/eachchain/${chainData.indexOf(chainListData)}`}>
                                {chainListData[0]}
                            </Link>
                        </li>)}
                </ul>


            </div>
            );
};

            export default Teacher;