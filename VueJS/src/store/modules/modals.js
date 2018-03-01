

// used in components/Modals.vue
// to have a global service for Modals !


const modalsState = {
    modals: [], // store the list of modals currently in actions
    // Last in First out.
}

const getters = {
    modals: state => state.modals,
}

const mutations = {
    add: (state, payload = 1) => {
        state.counter += payload
    },
    del_last: state => {
        state.modals.pop()
    },
}

const actions = {
    // increment: context => {
    //     context.commit('increment')
    // }
    increment: ({ commit }, payload) => {
        commit('increment', payload)
    },
    // async on Action, not on Mutations!
    asyncIncrement: ({ commit }) => {
        setTimeout(() => commit('increment'), 1000)
    },
}

export default {
    state: modalsState,
    getters,
    mutations,
    actions,
}
