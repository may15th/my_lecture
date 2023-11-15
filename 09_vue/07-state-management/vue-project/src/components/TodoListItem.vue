<template>
  <div>
    <div>
      TodoListItem
      <span @click="store.updateTodo(todo.id)"
      :class="{'is-done': todo.isdone}">
        {{ todo.text }}
        <button @click="store.deleteTodo(todo.id)"></button>
      </span>   
     </div>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';

defineProps({
  todo: Object
})

const store = useCounterStore()
</script>

<style scoped>
 .is-done {
  text-decoration: line-through;
 }
</style>