import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
export const useCounterStore = defineStore('counter', () => {
  let id =0
  const todos = ref([
    { id: id++, text: '할 일 1', isDone: false },
    { id: id++, text: '할 일 2', isDone: false },
  ])

  const addTodo = function () {
    todos.value.push({
      id: id++,
      text: todoText,
      isDone: false
    })

  }

// 삭제
const deleteTodo = function (todoId) {
  // todos 배열에서 몇 번째 인덱스가 삭제되었는지 검색
  const index = todos.value.findIndex((todo)=> todo.id === todoId)
  // 찾은 인덱스 값을 통해 배열에서 요소 제거 후 원본 배열 업데이트
  todos.value.splice(index, 1)
}
//수정
const updateTodo = function (todoId) {
  todos.value = todos.value.map((todo) => {
    if (todo.id === todoId ) {
      todo.isDone = !todo.isDone
    }
    return todo
  })

}

//계산
const doneTodoCount = computed(() => {
  return todos.value.filter((todo) => todo.isDone).length
})


  return { todos,addTodo, deleteTodo, updateTodo, doneTodoCount }

  // const doubleCount = computed(() => count.value * 2)
  // function increment() {
  //   count.value++
  // }

  return { count, doubleCount, increment }
})




