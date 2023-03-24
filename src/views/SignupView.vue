<template>
    <div class="form-container">
      <h1>Sign Up</h1>
      <form>
        <label for="name">Name</label>
        <input type="text" id="name" v-model="name">
        
        
        
        <label for="email">Email</label>
        <input type="email" id="email" v-model="email">
        
        <label for="password">Password</label>
        <input type="password" id="password" v-model="password">
        
        <button @click.prevent="submitForm">Submit</button>
      </form>
    </div>
  </template>
  
  <style>
  .form-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 20px;
  }
  
  form {
    display: flex;
    flex-direction: column;
    width: 80%;
    max-width: 500px;
    padding: 20px;
    border: 1px solid lightgray;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
  }
  
  label {
    margin-bottom: 5px;
  }
  
  input {
    padding: 10px;
    margin-bottom: 15px;
    border-radius: 5px;
    border: 1px solid lightgray;
    font-size: 16px;
  }
  
  button {
    padding: 10px 20px;
    background-color: blue;
    color: #fff;
    border: none;
    border-radius: 5px;
    font-size: 16px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: darkblue;
  }
  </style>

<script>

import axios from 'axios';

export default {
  data() {
    return {
      name: '',
      
      email: '',
      password: '',      
    }
  },
  methods: {
    submitForm() {      
      const formData = {
        name: this.name,
        
        email: this.email,
        password: this.password
      };
      
      
      axios.post(`http://localhost:8000/signup`,formData)
      .then(response => {
          console.log(response.data);
        })
        .catch(error => {
          console.log(error);
        });
      
      
      this.name = '';
      
      this.email = '';
      this.password = '';
    }
  }
}
</script>