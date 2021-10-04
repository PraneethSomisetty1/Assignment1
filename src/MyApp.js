import Table from './Table';
import Form from './Form';
import axios from 'axios';
import React, { useState, useEffect } from 'react';

function MyApp() {
  const [characters, setCharacters] = useState([]);

  async function makePostCall(person) {
    try {
      const response = await axios.post('http://localhost:5000/users', person);
      return response.data;
    } catch (error) {
      console.log(error);
      return false;
    }
  }

  async function fetchAll() {
    try {
      const response = await axios.get('http://localhost:5000/users');
      console.log(response.data.users_list);
      return response.data.users_list;   
   }
   catch (error){
      //We're not handling errors. Just logging into the console.
      console.log(error); 
      return false;         
   }
  }

  async function deleteperson(person) {
    try {
      // const requestOptions = {
      //   method: "DELETE",
      //   headers: { "Content-Type": "application/json" },
      //   body: JSON.stringify({id: person.id, name: person.name, job: person.job})
      // };
      await axios.delete('http://localhost:5000/users/' + person.id, person);
      return true;
    } catch (error) {
      console.log(error)
      return false;
    }
  }
  function removeOneCharacter(index) {
    const updated = characters.filter((character, i) => {
      return i !== index
    });

    const person = characters[index]
    deleteperson(person)
    setCharacters(updated);
  }

  function updateList(person) {   
    makePostCall(person).then(result => {
      if(result) {
        console.log(result.id);
        setCharacters([...characters, result])
      }
    });

  }

  useEffect(() => {
    fetchAll().then( result => {
       if (result)
          setCharacters(result);
     });
 }, [] );

  console.log(characters);

  return (
    <div className="container">
      <Table characterData={characters} removeCharacter={removeOneCharacter} />
      <Form handleSubmit={updateList} />
    </div>
  )
}

export default MyApp;