import React, { useState, useEffect } from "react";
import '../App.css';
import axios from 'axios';


const Student = () => {
    const [chainData, setChainData] = useState(undefined);
    const [Fname, setFName] = useState("");
    const [selectedFile, setSelectedFile] = useState(null);
    const [selectedFiles, setSelectedFiles] = useState(undefined)


    // useEffect(() => {
    //     async function fetchData() {
    //         try {
    //             const data = await axios.get('http://127.0.0.1:5000/chain');
    //             setChainData(data.data);
    //             console.log(data.data)

    //         }
    //         catch (e) {
    //             // console.log(e)
    //         }
    //     }
    //     fetchData();

    // }, []);

    function selectFiles(event) {
        console.log(event.target.files)
        setSelectedFiles(event.target.files)
      }

    const submitForm = () => {
        const formData = new FormData();
        let filedata = document.getElementById('textfile').files
        console.log(filedata[0])
        formData.append("file", filedata[0]);
        console.log(formData)

        axios
            .post('http://127.0.0.1:5000/test', formData, {          headers: {
                "Content-Type": "multipart/form-data",
              }})
            .then((res) => {
                alert("File Upload success");
            })
            .catch((err) => alert("File Upload Error"));
    };

    return (
        <div>
            <h1 className="description_intro">
                This is the Sutdent page.
            </h1>

            <p>Please enter your Sutdent ID Below:</p>
            <textarea cols="40" rows="1" id='newsTitle' name='newTitle' placeholder='Enter Your Student ID ' />

            <form encType="multipart/form-data">

                <div>
                    <label >
                        <input type="file" accept="text/*" id='textfile' onChange={selectFiles} />
                    </label>
                </div>
            </form>

            <button
                className="btn btn-success btn-sm"
                // disabled={!selectedFiles}
                onClick={submitForm}>
                Upload
             </button>



        </div>
    );
};

export default Student;