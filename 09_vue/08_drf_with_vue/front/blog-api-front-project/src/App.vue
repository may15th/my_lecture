<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
   <!-- text에서는 textinterpolation할려면 {{  }} 속성에서는  -->
   <div class="wrapper">
      <nav>
       <RouterLink :to="{ name:'main'}">Main</RouterLink>
       <RouterLink :to="{ name:'posts'}">Posts</RouterLink>
      </nav>
    </div>   
  </header>

  <RouterView />
</template>

<style scoped>
 .wrapper {
  max-width: 1200px;
  margin: 0 auto;
  padding: 1rem;
}
 nav {
  text-align: center;
  background-color: gray;
  padding: 1rem;
 }

 nav a {
  color: white;
  text-decoration: none;
  font-weight: bold;
 }
 /* rem 상대단위로 주는 게 좋아. */
 /* 브라우저 사파리 등 기본 스타일 너무 많아 상대로 하는 게 호환이 다돼. */
</style>
