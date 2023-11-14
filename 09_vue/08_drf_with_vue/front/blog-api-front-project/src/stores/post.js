import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const usePostStore = defineStore('post', () => {
  // 백엔드 서버에 post 전체 목록 GET 요청 
  // axios가 필요하다
  const getPostList = function () {
  axios({
    method: 'get',
    url: 'http://127.0.0.1:8000/api/v1/posts/'
  })
    .then(res => {
      console.log(res)
    })
    .catch(err => {
      console.log(err)
    })
  }
  return {
    getPostList,
  }
})
