import Vue from 'vue'
import VueRouter from 'vue-router'

import Axios from 'axios'

// icones:
import 'font-awesome/scss/font-awesome.scss'

import 'bootstrap/dist/css/bootstrap.css'

import App from './App.vue'
import { routes } from './routes'

// EVENT BUS:
import EventBusBooks from './components/books/EventBusBooks.vue'

// Vuex
import { store } from './store/store'

// API REST
export var http = Axios.create({baseURL: 'http://localhost:5000/api'})

// connect router to VueJS
Vue.use(VueRouter)

// ES6: for objects that have same name key: value
const router = new VueRouter({
    routes,
    mode: 'history' // hash vs history
})

// order is important!
// we create eventBus before components
export const $eventBus = new Vue({
    data: {
        books: new Vue(EventBusBooks)
    }
})
// could use it by:
// this.$eventBus.$on(...)
// this.$eventBus.books.$on(...)

// global eventBus:
Vue.prototype.$eventBus = $eventBus


new Vue({
  el: '#app',
  store,
  router,
  render: h => h(App)
})
