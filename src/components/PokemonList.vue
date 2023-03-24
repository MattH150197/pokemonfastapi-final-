<template>
    <div class="flex flex-col space-y-4">
        <Pokemon :pokemon="pokemon" v-for="(pokemon, index) in pokemons" :key="index" />
    </div>
</template>

<script setup>
<<<<<<< HEAD
=======
// import pokemons from "@/assets/sampledataset.json"
>>>>>>> cbd4b2a7b8918cf3acaad8dfeaeceef16282ba4d
import Pokemon from "./Pokemon.vue"
import {ref, onMounted} from "vue"
import client from "@/assets/apiclient.js"

// mount and then make api call
const pokemons = ref({})

onMounted(()=>{
    client.get("/pokemon").then(res=>{
        console.log("response received",res.data)
        pokemons.value=res.data
    }).catch(errors =>{
        console.log("error", errors)
    })
})
</script>
