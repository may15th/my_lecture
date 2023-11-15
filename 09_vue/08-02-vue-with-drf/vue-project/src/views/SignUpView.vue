<template>
  <div>
    <h1>signup</h1>
    <form @submit.prevent="signup">
      <input type="text" v-model.trim="username">
      <input type="password" v-model.trim="password1">
      <input type="password" v-model.trim="password2">
      <input type="submit">

    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store =useCounterStore()
const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)

const signup = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
  }
  store.signup(payload)
}

</script>

<style>

</style>
