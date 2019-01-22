import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import Axios from 'axios'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faBook, faSearch, faTimes
} from '@fortawesome/free-solid-svg-icons'

import { faVuejs } from '@fortawesome/free-brands-svg-icons'

import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import router from './router'
import store from './store'

Vue.config.productionTip = false

Vue.prototype.$http = Axios.create({ baseURL: 'http://localhost:5000/api' })

library.add(faBook, faSearch, faTimes, faVuejs)
Vue.component('font-awesome-icon', FontAwesomeIcon)

new Vue({
    router,
    store,
    render: h => h(App),
}).$mount('#app')
