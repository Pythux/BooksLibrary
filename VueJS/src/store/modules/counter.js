

const counterState = {
    counter: 0,
}

const getters = {
    doubleCounter: state => state.counter * 2,
    counter: state => state.counter,
}

const mutations = {
    increment: (state, payload = 1) => {
        state.counter += payload
    },
    decrement: state => { state.counter -= 1 },
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
    state: counterState,
    getters,
    mutations,
    actions,
}
