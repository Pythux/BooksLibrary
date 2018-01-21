<template lang="html">
  <div class="container">
      <p>Detail of Book id: {{ $route.params.id }}</p>

      <div v-show="to_edit_str != null">
          <textarea
              rows="2" style="width:100%;"
              v-model="to_edit_str"
          ></textarea>
          <br>
          <ui-button
                type='warning'
                i='cloud-upload'
                @click="edit"
          >edit</ui-button>
          <ui-alert
              type="error"
              @dissmiss='hide=true'
              v-if='!hide'
          >error</ui-alert>
      </div>

      <div class="3-col">
          <pre>{{ book }}</pre>
      </div>
  </div>
</template>

<script>
    import UiButton from '../../lib/std/UiButton.vue'
    import UiAlert from '../../lib/std/UiAlert.vue'
    export default {
        components: {
            UiButton,
            UiAlert
        },
        data() {
            return {
                book: {},
                attr_key: null,
                to_edit_str: null,
                hide: true
            }
        },
        methods: {
            selected(book, i) {
                console.log('listner selected of detail')
                this.book = book
                this.attr_key = i
                // this.to_edit_str = JSON.stringify(this.book[this.attr_key])
                this.to_edit_str = this.book[this.attr_key]

                // if Object or Array, don't handle it
                if(this.to_edit_str === Object(this.to_edit_str))
                    this.to_edit_str = null
            },
            edit() {
                console.log(`edit ${this.to_edit_str} -> ${this.attr_key}`)
                this.$eventBus.books.update_book(
                    this.book, this.attr_key, this.to_edit_str)
            }
        },
        created() {
            this.$eventBus.books.$on('selected', this.selected)
            // get book id:
            this.book = this.$eventBus.books.get_books().filter(
                b => b.id == this.$route.params.id)
        },
        beforeDestroy() {
            console.log('destroyed detail')
            this.$eventBus.books.$off('selected', this.selected)
        }
    }
</script>
