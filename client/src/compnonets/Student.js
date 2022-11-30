import React, { useState, useEffect } from "react";
import '../App.css';
import axios from 'axios';


const Student = () => {
    const [selectedFiles, setSelectedFiles] = useState(undefined);
    const [courseInfo, setCourseInfo] = useState(undefined);


    function selectFiles(event) {
        console.log(event.target.files)
        setSelectedFiles(event.target.files)
    }

    const submitForm = async () => {
        let inputId = document.getElementById('stuID').value;
        let courseName = document.getElementById('course').value;
        const formData = new FormData();
        let filedata = document.getElementById('textfile').files
        console.log(courseName)
        console.log(inputId)
        formData.append("file", filedata[0]);
        formData.append("studentId", inputId);
        formData.append("course", courseName);

        await axios
            .post('http://127.0.0.1:5000/uploadhomework', formData, {
                headers: {
                    "Content-Type": "multipart/form-data",
                }
            })
            .then((res) => {
                alert("File Upload success");
            })
            .catch((err) => alert(err.response.data));
    };

    const checkCourse = async () => {
        let inputId = document.getElementById('stuID').value;

        await axios.post('http://127.0.0.1:5000/course', { studentId: inputId })
                .then((res) => { setCourseInfo(res.data) })
                .catch((err) => alert('Can not find your course'));

            console.log(courseInfo)



        // .then((res) => { setCourseInfo(res.data) })
        // .catch((err) => alert("File Upload Error"));

    }

    return (
        <div>
            <h1 className="description_intro">
                Welcome to student homework submit page
            </h1>



            <p className ='Common_description'>Please enter your Sutdent ID Below:</p>
            <textarea  className ='Common_description' cols="40" rows="2" id='stuID' placeholder='Enter Your Student ID ' />

            <div>
                <button
                    className="StudentPageButton"
                    // disabled={!selectedFiles}
                    onClick={checkCourse}>
                    Check My Course
                </button>
                <div className="Common_description">
                    <ul>
                        {courseInfo && courseInfo.map((courseData) =>
                            <li key={courseData}>
                                {courseData[1]}
                            </li>)}
                    </ul>

                </div>
            </div>

            <p className="Common_description">Submit Your Homework</p>
            <select className="Common_description" id="course"  >
                <option value="none" defaultValue disabled hidden>Select Course</option>

                {courseInfo && courseInfo.map((courseData) =>
                            <option value = {courseData[1]} key={courseData}>
                                {courseData[1]}
                            </option>)}
                {/* <option value="ICSI210">ICSI210</option>
                <option value="ICSI221">ICSI221</option>
                <option value="ICSI333">ICSI333</option>
                <option value="ICSI342">ICSI342</option>
                <option value="ICSI300Z">ICSI300Z</option>
                <option value="ICSI410">ICSI410</option>
                <option value="ICSI433">ICSI433</option> */}
            </select>
            <div className="Common_description">
                <form encType="multipart/form-data">

                    <div>
                        <label >
                            <input type="file" accept="text/*" id='textfile' onChange={selectFiles} />
                        </label>
                    </div>
                </form>

                <button
                    className="speicalButton"
                    // disabled={!selectedFiles}
                    onClick={submitForm}>
                    Upload

                </button>

            </div>



        </div>
    );
};

export default Student;