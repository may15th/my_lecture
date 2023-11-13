<template>
  <div>
    
    <ParentChild 
      my-msg="message" 
      :dynamic-props="name" 
      @some-event="someCallback"
      @emit-args="getNumbers"
      @update-name = "updateName"
    />
    <!-- html속성값은 camel안쓰고 (-)하이픈으로 이어가 -->
  </div>
</template>

<script setup>
import ParentChild from '@/components/parentChild.vue';
import {ref} from 'vue'

const someCallback = function () {
  console.log('ParentChild가 발신한 emit 이벤트를 수신')
}
const name = ref('Alice')
const getNumbers = function (...args) {
  console.log(args)
}

const updateName = function() {
  name.value = 'Bella'
}
</script>

<style scoped>

</style>