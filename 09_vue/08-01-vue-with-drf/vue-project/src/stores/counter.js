import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
// axios는 왜 중괄호 처리 안하고 다른 것들은 중괄호 처리 하는거...

export const useCounterStore = defineStore('counter', () => {
  const articles = ref([
  ])
  const API_URL = "http://127.0.0.1:8000"

  // BRF에 article 조회 요청을 보내는 action
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`
    })
      .then((res) =>{
        // console.log(res)
        // 반응형객체이기 때문에 value해주고
        articles.value = res.data
      })
      .catch((err) =>{
        console.log(err)
      })
  }
  return {articles, API_URL, getArticles}
}, { persist: true })
