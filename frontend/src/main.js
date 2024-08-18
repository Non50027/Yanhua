import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

import home from './components/home.vue'
import login from './member/login.vue'
import member from './member/member.vue'

const app = createApp(App)
app.component('home', home)
app.component('login', login)
app.component('member', member)

app.mount('#app')

