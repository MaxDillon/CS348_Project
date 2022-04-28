import React from "react";
import {useState, useLayoutEffect} from 'react'
import { useNavigate } from 'react-router-dom';
import './Edit.css'
export default function Field(props) {
    const[newField, setNewfield] = useState('');
    const [isEditing, setEditing] = useState(false);

    async function update() {
        const res = await fetch('/edit/update', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                'id': props.id,
                'fieldName': props.details[0],
                'fieldVal': newField
            })
        })
    
        return res.status < 400 || res.status >= 500
    }


function handleChange(e) {
    setNewfield(e.target.value);
}
function handleSubmit(e) {
    e.preventDefault();
    setEditing(false);
    update();
    console.log(newField);
    setNewfield('');
  }
const view = ( <div className={"stackIt"}>
    <p>{props.details[0]}</p> 
    <p>{props.details[1]}</p> 
    <p><button className={"button"} onClick={() => setEditing(true)}>Edit</button></p>
    </div>
);

const editing = (
        <div className={"stackIt"}>

<p>{props.details[0]}</p>
    <input type="text" onChange={handleChange} value={newField} ></input>
<p>
    <button className={"button"} onClick={handleSubmit}>Save</button>
    <button className={"button"} onClick={() => setEditing(false)}>Cancel</button>

</p>
</div>
);

return <div key={props.details[0]}>{isEditing ? editing : view}</div>;

}