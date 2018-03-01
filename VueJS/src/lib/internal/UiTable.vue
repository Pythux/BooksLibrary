<template>
    <table>
        <tr v-if="table.axe">
            <th
                v-for="head in table.headers"
                :key="head"
            >{{ head }}</th>
        </tr>
        <tr
            v-for="(row, index) in table.row"
            :key="index"
        >
            <th v-if="!table.axe">{{ table.headers[index] }}</th>
            <td
                v-for="(d, index2) in row"
                :key="index2"
                @click="emit(index2, index)">{{ d }}</td>
        </tr>
    </table>
</template>


<script>
export default {
    props: { // get from < ... :data="data">
        data: {
            type: Array,
            required: true,
        },
        map_data: {// how to get the data
            type: Array,
            required: true,
        },
        name_header: {// headers name
            type: Array,
            required: true,
        },
        axe: {// 'horizontal' or 'x'
            type: String,
            default: 'x',
        },
    },
    computed: {
        table() {
            const isAxeX = ['horizontal', 'x'].includes(this.axe)
            return {
                axe: isAxeX,
                headers: this.name_header,
                row: isAxeX ?
                    this.horizontal() :
                    this.vertical(),
            }
        },
    },
    methods: {
        get(md, d) {
            if (typeof md === 'string') {
                return d[md]
            }
            // else (typeof md === 'function')
            return md(d)
        },
        vertical() {
            return this.map_data.map(md => this.data.map(d => this.get(md, d)))
        },
        horizontal() {
            return this.data.map(d => this.map_data.map(md => this.get(md, d)))
        },
        emit(x, y) {
            let sendX = x
            let sendY = y
            if (!this.table.axe) {
                [sendX, sendY] = [y, x]
            }
            this.$emit('click', this.data[sendY], sendX)
        },
    },
}

// modif() { // two way to make vuejs see the change on array/objects
//     var d = this.data[1]
//     d = Object.assign({}, d, { title: 'Updated!' }) // create new object
//     Vue.set(this.data, 1, d) // create new list
// },
</script>


<style scoped>
    table {
        font-family: arial, sans-serif;
        border-collapse: collapse;
        width: 100%;
    }

    td, th {
        border: 1px solid #9be3e6;
        text-align: left;
        padding: 8px;
    }

    tr:nth-child(even) {
        background-color: #c1d5ee;
    }
</style>
