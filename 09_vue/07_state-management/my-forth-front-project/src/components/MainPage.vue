<template>
  <div>
    <h1>피니아 연습하기</h1>
    <ParentPage 
      v-for="info in store.familyInfos"
      :key="info.familyName"
      :info="info"
    />
  </div>
</template>

<script setup>
  import ParentPage from './ParentPage.vue';
  import { useFamilyStore } from '../stores/family';
  const store = useFamilyStore()
  // const { familyInfos } = store
  // const familyInfos = store.familyInfos
</script>

<style scoped>

</style>