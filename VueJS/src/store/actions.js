
import * as space from './namespace'
// old way namespacing:
export default {
    [space.updateValue]: ({ commit }, newVal) => commit('updateValue', newVal),
}

// export const updateValue = ({commit}, new_val) => commit('updateValue', new_val)
