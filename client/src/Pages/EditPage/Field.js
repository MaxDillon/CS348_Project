import React, { useEffect } from "react";
import {useState, useLayoutEffect} from 'react'
import { useNavigate } from 'react-router-dom';
import './Edit.css'

   
async function update( field, value ) {

    const res = await fetch('/edit/update', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'fieldName': field,
            'fieldVal': value
        })
    })

    return res.status < 400 || res.status >= 500
}



export default function Field({ name, field, value }) {

    const [isEditing, setEditing] = useState(false);
    const [fieldValue, setFieldValue] = useState(value);

    useEffect(() => setFieldValue(value), [value])
    
    function handleSubmit(newValue) {

        setEditing(false);
        setFieldValue(newValue)
        update(field, newValue);
    
    }

    return (
        <div key={name} className={"verticalSpace"}>
            {isEditing ? 
                <Edit onSave={handleSubmit} onCancel={() => setEditing(false)} name={name} /> : 
                <View value={fieldValue} onEdit={() => setEditing(true)} name={name} />
            }
        </div>
    );


}


function Edit({ onSave, onCancel, name }) {
    const [value, setValue] = useState("")
    return (
        <div className={"stackIt"}>
            <div>{name}</div>
            <input type="text" onChange={e => setValue(e.target.value)} value={value} ></input>

            <div>
            <button className={"button"} onClick={e => {
                e.preventDefault()
                onSave(value)
            }}>Save</button>

            <button className={"button"} onClick={ e => {
                e.preventDefault()
                onCancel()
            }}>Cancel</button>
            </div>

        </div>

    )
}

function View({ value, onEdit, name }) {
    return (
        <div className={"stackIt"}>
            <div>{name}</div>
            <div>{value}</div> 
            <button className="button" onClick={e => {
                e.preventDefault()
                onEdit()
            }}>Edit</button>
        </div>
    )
}