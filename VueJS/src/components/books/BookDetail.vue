<template lang="html">
  <div class="container" v-if="display">
      <p>Detail of Book id: {{ $route.params.id }}</p>

      <textarea v-model="to_edit_str" rows="2" style="width:100%;"></textarea>
      <br>
      <ui-button
            type='warning'
            i='cloud-upload'
      >edit</ui-button>

      <div class="3-col">
          <pre>{{ book }}</pre>
      </div>
  </div>
</template>

<script>
    import UiButton from '../../lib/std/UiButton.vue'
    export default {
        components: {
            UiButton
        },
        data() {
            return {
                book: {},
                attr_key: null,
                display: false,
            }
        },
        filters: {
            pretty: function(str_json) {
                return JSON.stringify(JSON.parse(str_json), null, 2)
            }
        },
        computed: {
            to_edit_str() {
                return JSON.stringify(this.book[this.attr_key])
            },
        },
        methods: {
            selected(book, i) {
                console.log('listner selected of detail')
                this.book = book
                this.attr_key = i
                if (!this.display) {
                    this.display = true
                }
            }
        },
        // beforeCreate() {  // data and methods doesn't exist
        //     var { book, attr_key } = this.$eventBus.books.get_selected()
        //     console.log('beforeCreate detail')
        //     if (!attr_key) {
        //         this.$router.push({ name: 'books' })  // NO NO NO
        //     }
        // },
        created() {  // this.selected is undefined at `beforeCreate`, cf lifecycle
            // this.$router.push({ name: 'books' })  // NO NO NO
            // is it a bug ???
            var { book, attr_key } = this.$eventBus.books.get_selected()
            this.book = book
            this.attr_key = attr_key
            console.log(`created detail with: ${this.attr_key}`)
            this.$eventBus.books.$on('selected', this.selected)
        },
        // mounted() {  // is it a bug ???
        //     if (this.attr_key) {
        //         this.display = true
        //     }
        //     else {
        //         console.log('route to books!')
        //         this.$router.push({ name: 'books' })
        //     }
        // },
        beforeDestroy() {
            console.log('destroyed detail')
            this.$eventBus.books.$off('selected', this.selected)
        }
    }
</script>
