<template>
  <div>
    TodoForm
    <form @submit.prevent="createTodo(todoText)" ref="formElem">
      <input type="text" v-model="todoText">
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter';

const formElem = ref(null)
const todoText = ref('')
const store = useCounterStore()
const createTodo = function  (todoText) {
  store.addTodo(todoText.value)
  formElem.value.reset()
}
</script>

<style scoped>

</style>