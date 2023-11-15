<script setup>
import TodoForm from '@/components/TodoForm.vue';
import TodoList from '@/components/TodoList.vue';

</script>

<template>
  <div>
    <h1>Todo Project</h1>
    <h2>완료된 Todo: {{ store.doneTodosCount  }}</h2>
    <TodoList />
    <TodoForm />

  </div>
</template>

<style scoped>

</style>
