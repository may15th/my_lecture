
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import PiniaPluginPersistedstate from 'PiniaPluginPersistedstate'

const app = createApp(App)
const pinia = createPinia()

pinia.use(PiniaPluginPersistedstate)
app.use(createPinia())
app.use(pinia)
app.mount('#app')
