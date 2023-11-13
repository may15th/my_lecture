<template>
  <div>
    <h1>UserView</h1>
    <!-- $는 내장 기본 속성을 의미 emit에서 사용
    route속성 객체임. -->
    <h2>{{ $route }}번 페이지</h2>
    <h2>{{ $route.params.id }}번 페이지</h2>
    <h2>{{ userId }}번 페이지</h2>
    <button @click="goHome" >홈으로!</button>
    <button @click="routeUpdate">100번 유저 홈페이지</button>
    
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import { useRoute, useRouter, onBeforeRouteLeave, onBeforeRouteUpdate } from 'vue-router'

  const route = useRoute()
  const userId = ref(route.params.id)
  // const userId = ref(route.)

  const router = useRouter()












  
  ///아래부터는 홈 이동 등에 대한 것들
  const goHome = function() {
    // router.push({ name : 'home' })
    router.replace({ name: 'home' })
  }
  // In-component Guard
  // 1.
  onBeforeRouteLeave((to, from) => {
    const answer = window.confirm('정말 떠나실 건가요?')
    if (answer === false ) {
      return false
    }
  })

  const routeUpdate = function () {
    router.push({name: 'user', params: {id: 100}})
  }
  onBeforeRouteUpdate((to, from) => {
    userId.value = to.params.id

  })
  // 확인시 to로 취소시 from 
  // confirm의 내장값이 있어 t/f값을 to/from으로 



  

</script>

<style scoped>

</style>