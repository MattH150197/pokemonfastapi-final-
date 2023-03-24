<template>
<<<<<<< HEAD
    <div class="flex flex-col space-y-6">
       <h1 class="text-6xl text-gray-900 font-semibold">{{pokemonDetails.name }}</h1>
        <img :src="image" :alt="pokemonDetails?.name" class="w-full h-full rounded-lg" />
    <div>
        <div class="flex items-center space-x-4">
            <span> Primary Type</span>
            <span> {{ pokemonDetails?.type1 }}</span>
       </div>

       <div class="flex items-center space-x-4" v-if="pokemonDetails?.type2">
            <span> Secondary Type</span>
            <span> {{ pokemonDetails?.type2 }}</span>
       </div>
    </div>

    <div>
        <div class="flex items-center space-x-4">
            <span> Weight</span>
            <span>{{ pokemonDetails?.stats?.weight_kg }} kg</span>
        </div>

        <div class="flex items-center space-x-4">
            <span>Height</span>
            <span>{{ pokemonDetails?.stats?.height_m }} m</span>
        </div>
    </div>

    </div>
    </template>

=======
  <div class="flex flex-col space-y-6">
    <h1 class="text-6xl text-gray-900 font-semibold">
      {{ pokemonDetails?.name }}
    </h1>
    <img :src="image" :alt="pokemonDetails?.name" class="w-full h-full rounded-lg" />
    <div>
      <div class="flex items-center space-x-4">
        <span> Primary Type</span>
        <span> {{ pokemonDetails?.type1 }} </span>
      </div>

      <div class="flex items-center space-x-4" v-if="pokemonDetails?.type2">
        <span> Secondary Type</span>
        <span> {{ pokemonDetails?.type2 }} </span>
      </div>
    </div>


     <div>
      <div class="flex items-center space-x-4">
        <span> Weight</span>
        <span> {{ pokemonDetails?.stats?.weight_kg }} Kg </span>
      </div>

      <div class="flex items-center space-x-4">
        <span> Height</span>
        <span> {{ pokemonDetails?.stats?.height_m }} m </span>
      </div>
    </div>
  </div>
</template>
>>>>>>> cbd4b2a7b8918cf3acaad8dfeaeceef16282ba4d

<script setup>
import { useRoute } from "vue-router";
import pokemons from "@/assets/sampledataset.json";
import { onMounted, ref } from "vue";

<<<<<<< HEAD
import {useRoute} from "vue-router"
import pokemons from "@/assets/sampledataset.json"

import {onMounted, ref} from "vue";
=======
>>>>>>> cbd4b2a7b8918cf3acaad8dfeaeceef16282ba4d
import axios from "axios";

const route = useRoute();

const pokemonDetails =ref({})

const image = ref("")

onMounted(()=>{
    pokemonDetails.value = pokemons.filter((item) => item.name.toLowerCase() == route.params.name.toLowerCase())[0];

    axios.get(`https://pokeapi.co/api/v2/pokemon/${pokemonDetails.value.name.toLowerCase()}`)
    .then(data =>{image.value = data.data.sprites.other['official-artwork'].front_default})
    
    
})

// passing name as route parameter. Check router/index.js for more details
<<<<<<< HEAD

=======
const pokemonDetails = ref({});
>>>>>>> cbd4b2a7b8918cf3acaad8dfeaeceef16282ba4d

const image = ref("")

onMounted(() => {
  pokemonDetails.value = pokemons.filter(
    (item) => item.name.toLowerCase() == route.params.name.toLowerCase()
  )[0];


  axios.get(`https://pokeapi.co/api/v2/pokemon/${pokemonDetails.value.name.toLowerCase()}`).then(data =>{
     image.value = data.data.sprites.other['official-artwork'].front_default
  })  


});
</script>
