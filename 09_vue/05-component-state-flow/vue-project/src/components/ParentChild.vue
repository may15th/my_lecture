<template>
  <div>
    {{  myMsg }}
    <p>{{ dynamicProps }}</p>
    <ParentGrandChild :my-msg="myMsg" 
      @update-name ="updateName"
    />
    <button @click="$emit('someEvent')">클릭</button>
    <button @click="buttonClick">클릭2</button>
    <button @click="emitArgs">추가인자 전달</button>
  </div>
</template>

<script setup>
// defineProps(['myMsg'])

import ParentGrandChild from '@/components/parentGrandChild.vue'

// 자바스크립트는 카멜케이스 사용
// html에서 카멜사용하거나, js에서 케밥 사용하면 안되나? 실험 ㄱㄱ
// 2. 객체 선언 방식
defineProps({
  myMsg: String,
  dynamicProps: String,
})

const emit = defineEmits(['someEvent', 'emitArgs', 'updateName'])

// emit선언
const buttonClick = function () {
  emit('someEvent')
}
const emitArgs = function () {
  emit('emitArgs', 1,2,3)
}

const updateName = function() {
  emit('updateName')
}
// 타입과 리콰이어드 유효성 검사가 목적.
// 객체선언방식을 권장.

// defineProps의 리턴 값이 있음!!
// const props = defineProps({
//   myMsg: String
// })
// console.log(props)



</script>

<style scoped>

</style>