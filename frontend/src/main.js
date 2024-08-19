import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import BootstrapVue3 from 'bootstrap-vue-3'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'

import home from './components/home.vue'
import login from './member/login.vue'
import member from './member/member.vue'

const app = createApp(App)

app.use(BootstrapVue3)
app.use(router)

app.component('home', home)
app.component('login', login)
app.component('member', member)

app.mount('#app')

