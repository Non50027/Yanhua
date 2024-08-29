import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import BootstrapVue3 from 'bootstrap-vue-3'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'

import home from './components/home.vue'
import login from './member/login.vue'
import member from './member/member.vue'
import shop from './shop/shop.vue'
import add from './shop/add/add.vue'
import go from './activity/go.vue'
import yanhua from './components/yanhua.vue'
import huh from './components/huh.vue'
import tto from './components/tto.vue'
import done from './components/done.vue'
import { getMemberData } from './services/getData'

const app = createApp(App)

app.use(BootstrapVue3)
app.use(router)

app.component('home', home)
app.component('login', login)
app.component('shop', shop)
app.component('add', add)
app.component('member', member)
app.component('go', go)
app.component('yanhua', yanhua)
app.component('huh', huh)
app.component('tto', tto)
app.component('done', done)
app.component('getMemberData', getMemberData)

app.mount('#app')

