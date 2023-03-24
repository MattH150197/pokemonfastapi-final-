<script setup>
import UserForm from "@/components/UserForm.vue"

function login(user){
  // api request
  
}

</script>

<template>
    <div>
      
      <UserForm formType="signin" @submit="login" />
      <!-- Login page -->
    </div>
</template>

<script>


export default {
  data() {
    return {
      email: '',
      password: '',
      errorMessage: ''
    }
  },
  methods: {
    submitForm() {
      const formData = {
        email: this.email,
        password: this.password
      };
      
      axios.post('http://localhost:8000/signup', formData)
        .then(response => {
        
          if (response.status === 200) {
            
            console.log('Login successful');
          } else {
            this.$router.push('/pokemons');
          }
        })
        .catch(error => {
          console.log(error);
          this.errorMessage = 'An error occurred while processing your request';
        });
      
      this.email = '';
      this.password = '';
    }
  }
}
</script>