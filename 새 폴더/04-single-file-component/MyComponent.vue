<template>
  <div class="greeting">{{ msg }}</div>
</template>

<script setup>
import { ref } from 'vue'

const msg = ref('Hello World')
</script>

<!-- 나중에 컴포넌트 트리가 구성됨. -->
<!-- 스코프드는 이 vue 컴포넌트 파일에만 이 스타일을 적용한다는 걸 의미함. -->
<style scoped>
.greeting {
  color: red;
}
</style>
