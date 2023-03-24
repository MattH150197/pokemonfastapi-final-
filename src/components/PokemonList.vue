<template>
    <div class="flex flex-col space-y-4">
        <Pokemon :pokemon="pokemon" v-for="(pokemon, index) in pokemons" :key="index" />
    </div>
</template>

<script setup>
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
