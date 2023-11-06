import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import axios from "axios"


const app = createApp(App)

axios.defaults.withCredentials=true
axios.defaults.baseURL='http://localhost:5000'

app.use(router)

app.mount('#app')
