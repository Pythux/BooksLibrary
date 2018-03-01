<template lang="html">
    <div class="container">
        <p>Detail of Book id: {{ $route.params.id }}</p>

        <div v-show="to_edit_str != null">
            <textarea
                v-model="to_edit_str"
                rows="2"
                style="width:100%;"
            />
            <br>
            <ui-button
                type="warning"
                i="cloud-upload"
                @click="edit"
            >edit</ui-button>
            <ui-alert
                v-if="!hide"
                type="error"
                @dissmiss="hide=true"
            >error</ui-alert>
        </div>

        <div class="3-col">
            <pre>{{ book }}</pre>
        </div>
    </div>
</template>

<script>
import { createNamespacedHelpers } from 'vuex'
import UiButton from '../../lib/std/UiButton.vue'
import UiAlert from '../../lib/std/UiAlert.vue'

const modals = createNamespacedHelpers('modals')
export default {
    components: {
        UiButton,
        UiAlert,
    },
    data() {
        return {
            book: {},
            attr_key: null,
            to_edit_str: null,
            hide: true,
        }
    },
    created() {
        this.$eventBus.books.$on('selected', this.selected)
        // get book id:
        this.book = this.$eventBus.books.get_books()
            .filter(b => b.id === this.$route.params.id)
    },
    beforeDestroy() {
        this.$eventBus.books.$off('selected', this.selected)
    },
    methods: {
        ...modals.mapActions(['add']),
        selected(book, i) {
            this.book = book
            this.attr_key = i
            // this.to_edit_str = JSON.stringify(this.book[this.attr_key])
            this.to_edit_str = this.book[this.attr_key]

            // if Object or Array, don't handle it
            if (this.to_edit_str === Object(this.to_edit_str)) { this.to_edit_str = null }
        },
        edit() {
            const callbackCatch = err => {
                console.log(JSON.stringify(err.response.data, null, 4))
                this.add({
                    icon: 'error',
                    title: `Can't update: ${err.response.statusText}`,
                    msg: err.response.data.validation_errors,
                    button: "That's fine!",
                })
            }
            const callbackFinally = () => {
                console.log('finish calling')
            }
            this.$eventBus.books.update_book(
                this.book, this.attr_key,
                this.to_edit_str, callbackCatch, callbackFinally,
            )
        },
    },
}
</script>
