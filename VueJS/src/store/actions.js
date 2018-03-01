
import * as space from './namespace'
// old way namespacing:
export default {
    [space.updateValue]: ({commit}, new_val) => commit('updateValue', new_val)
}

// export const updateValue = ({commit}, new_val) => commit('updateValue', new_val)
