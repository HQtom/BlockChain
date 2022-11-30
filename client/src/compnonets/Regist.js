import React, { useState, useEffect } from "react";
import '../App.css';
import axios from 'axios';


const Regist = () => {
    const [courseInfo, setCourseInfo] = useState(undefined);
    const [studnetInputID, setStudentInputID] = useState(undefined);


    const checkCourse = async () => {
        setCourseInfo(undefined)
        let inputId = document.getElementById('stuID').value;
        setStudentInputID(inputId);
        await axios.post('http://127.0.0.1:5000/course', { studentId: inputId })
            .then((res) => { setCourseInfo(res.data) })
            .catch((err) => alert('Can not find your course'));
    }

    const dropCourse = async (info) => {
        setCourseInfo(undefined)
        let inputId = document.getElementById('stuID').value;
        let dropdata = await axios.post('http://127.0.0.1:5000/drop', { id: inputId, courseName: info  })
        .then((res) => { setCourseInfo(res.data) })

    }

    const registNewCourse = async () =>{
        setCourseInfo(undefined)
        let inputId = document.getElementById('stuID').value;
        let info = document.getElementById('course').value;
        await axios.post('http://127.0.0.1:5000/regist', { id: inputId, courseName: info })
        .then((res) => { setCourseInfo(res.data) })
    }


    return (
        <div>
            <h1 className="description_intro">
                This is the Regist page.
            </h1>
            <p className ='Common_description'>Please enter your Sutdent ID Below:</p>
            <textarea className ='Common_description' cols="40" rows="1" id='stuID' placeholder='Enter Your Student ID ' />

            <div >
                <button
                    className="StudentPageButton"
                    // disabled={!selectedFiles}
                    onClick={checkCourse}>
                    Check My Course
                </button>
            </div>

            <div>
                <ul>

                    {courseInfo && courseInfo.map((courseData) =>
                        <div>
                            <p key={courseData} >
                                {courseData[1]}
                            </p>
                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                            <button onClick={() =>dropCourse(courseData[1])}>drop</button>
                        </div>
                    )
                    }
                </ul>

            </div>

            <div>
                <p className ='Common_description'>Regist a new course</p>
                <select className ='Common_description' id="course"  >
                    <option value="none" defaultValue disabled hidden>Select Course</option>
                    <option value="ICSI210">ICSI210</option>
                    <option value="ICSI221">ICSI221</option>
                    <option value="ICSI333">ICSI333</option>
                    <option value="ICSI342">ICSI342</option>
                    <option value="ICSI300Z">ICSI300Z</option>
                    <option value="ICSI410">ICSI410</option>
                    <option value="ICSI433">ICSI433</option>
                </select>

                <button onClick={registNewCourse}>regist</button>

            </div>

        </div>
    );
};

export default Regist;