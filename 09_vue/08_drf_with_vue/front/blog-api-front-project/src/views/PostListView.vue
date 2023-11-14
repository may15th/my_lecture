<template>
  <div>
    <h1>게시글 목록 페이지</h1>
  </div>
</template>

<!-- 컴포지션 형식 setup방식
별도의 라사훅x -->
<script setup>
//store에 정의한 actions가져와서 실행하기
// onMounted의 쓰임. created만된 순간, mount되기 전에는 vue instance가 index.html에 부착되기 전
// 인스턴스 안에서 dom에 들어있는 내용물에 접근할 수 없다>? 
// mount한 이후에도 직접적으로 dom에 접근하는 형식은 하지 않을 것.

import { onMounted } from 'vue';
import { usePostStore } from '../stores/post';
const store = usePostStore()
onMounted(()=>{
  store.getPostList()
})
store.getPostList()
// 현재 컴포넌트가 마운트 되고난 후에, axios 요청 보낼 것.

</script>

<style scoped>

</style>