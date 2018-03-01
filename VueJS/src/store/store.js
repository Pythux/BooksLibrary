import Vue from 'vue'
import Vuex from 'vuex'

import counter from './modules/counter'
import modals from './modules/modals'
import actions from './actions'
import * as mutations from './mutations'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        value: 'val',
    },
    getters: {
        value: ({ value }) => value,
    },
    mutations,
    actions,
    modules: {
        // counter // no namespace (on old VueJS)
        namespace: counter, // new way "namespacing"
        // store.state.namespace -> `namespace`´s state
        // a: modals, // modals namespace
        modals: {
            // avoid: [vuex] duplicate getter key: counter
            namespaced: true,
            // state: { counter: 0 },
            // mutations: {
            //     value: (state, newValue) => {
            //         state.counter = newValue
            //     },
            // },
            state: modals.state,
            mutations: modals.mutations,
            actions: modals.actions,
            getters: modals.getters,
        },
        second_counter: {
            // avoid: [vuex] duplicate getter key: counter
            namespaced: true,
            state: { counter: 0 },
            getters: {
                counter: state => state.counter,
                sum: (state, getters, rootState, rootGetters) =>
                    getters.counter + rootGetters.counter,
            },
            mutations: {
                value: (state, newValue) => {
                    state.counter = newValue
                },
            },
        },
    },
})

// more info on vueX´s namespace:
// https://vuex.vuejs.org/en/modules.html
