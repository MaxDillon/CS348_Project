import React, { useEffect } from "react";
import {useState, useLayoutEffect} from 'react'
import { useNavigate } from 'react-router-dom';
import './Edit.css'
export default function Field(props) {
    const[newField, setNewfield] = useState('');
    const [isEditing, setEditing] = useState(false);
    const [fieldValue, setFieldValue] = useState(props.value);
   
    async function update() {
        const res = await fetch('/edit/update', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                'id': props.id,
                'fieldName': props.field,
                'fieldVal': newField
            })
        })
    
        return res.status < 400 || res.status >= 500
    }

    useEffect(() => {setFieldValue(props.value)}, [props.value])


    function handleChange(e) {
        setNewfield(e.target.value);
    }
    function handleSubmit(e) {
        e.preventDefault();
        setEditing(false);
        update();
        console.log(newField);
        setFieldValue(newField)
        setNewfield('');
    }

    function editingFun() {
        return (
            <div className={"stackIt"}>

                <p>{props.name}</p>
                <input type="text" onChange={handleChange} value={newField} ></input>
                <p>
                    <button className={"button"} onClick={handleSubmit}>Save</button>
                    <button className={"button"} onClick={() => setEditing(false)}>Cancel</button>

                </p>
            </div>

        )
    }

    function viewFun() {
        return (
            <div className={"stackIt"}>
                <p>{props.name}</p> 
                <p>{fieldValue}</p> 
                <p><button className={"button"} onClick={() => setEditing(true)}>Edit</button></p>
            </div>
        )
    }
        

    return <div key={props.name}>{isEditing ? editingFun() : viewFun()}</div>;

}
