<template>
    <ui-table
        :data='data'
        :name_header="name_header"
        :map_data="map_data"
        :axe='axe'
        @click="(a, b) => $emit('click', a, b)"
    />
</template>


<script>
    import UiTable from '../internal/UiTable.vue'

    export default {
        props: { // get from < ... :data="data">
            data: {
                type: Array,
                required: true
            },
            map_data: {// how to get the data
                type: Array,
                required: true
            },
            name_header: {// headers name
                type: Array,
                required: true
            },
            axe: {// 'horizontal' or 'x'
                type: String,
                default: 'x'
            },
        },
        components: {
            UiTable,
        }
    }
</script>
