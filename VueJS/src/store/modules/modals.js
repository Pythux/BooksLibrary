

// used in components/Modals.vue
// to have a global service for Modals ;)


const modalsState = {
    modals: [], // store the list of modals currently in actions
    // Last in First out.
}

const getters = {
    modals: state => state.modals,
}

const mutations = {
    add: (state, modal) => {
        state.modals.push(Object
            .assign({ ref: state.modals.length }, modal))
    },
    del_current: state => {
        state.modals.pop()
    },
}

const actions = {
    add: ({ commit }, modal) => {
        commit('add', modal)
        // this.$eventBus.modals.add(modal)
        // no event bus outside VueJS components
    },
    del_current: ({ commit }) => {
        commit('del_current')
    },
}

export default {
    state: modalsState,
    mutations,
    actions,
    getters,
}
