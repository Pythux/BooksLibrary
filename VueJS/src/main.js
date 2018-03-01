import Vue from 'vue'
import VueRouter from 'vue-router'

import Axios from 'axios'

// icones:
import 'font-awesome/scss/font-awesome.scss'

import 'bootstrap/dist/css/bootstrap.css'

import App from './App.vue'
import routes from './routes'
// VueX
import store from './store/store'

// Event Bus of Books:
import EventBusBooks from './components/books/EventBusBooks.vue'

// API REST
const http = Axios.create({ baseURL: 'http://localhost:5000/api' })
Vue.prototype.$http = http

// connect router to VueJS
Vue.use(VueRouter)

// ES6: for objects that have same name key: value
const router = new VueRouter({
    routes,
    mode: 'history', // hash vs history
})

// order is important,
// we create eventBus before components
const $eventBus = new Vue({
    data: {
        books: new Vue(EventBusBooks),
    },
})
// we could use it by:
// this.$eventBus.$on(...)
// this.$eventBus.books.$on(...)
// .$off() -> remove all listeners from the selected eventBus
// .$off('event') -> remove all listeners of the event
// .$off('event', <fun>) -> remove the specifice listener <fun>
// .$once(...) -> listen for the first emission of an event
// .$emit('event', data)


// global eventBus:
Vue.prototype.$eventBus = $eventBus

// Vue on index.html -> id="app"
/* eslint-disable no-new */
// make side effect
new Vue({
    el: '#app',
    store, // VueX
    router,
    render: h => h(App),
})
/* eslint-enable no-new */
