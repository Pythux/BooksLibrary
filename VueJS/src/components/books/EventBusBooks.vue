<script>
    export default {
        data() {
            return {
                books: [],
                selected_book: { book: {}, attr_key: null }
            }
        },
        methods: {
            refresh() {
                this.$http.get('/books')
                    .then(response => {
                        this.books = response.data.objects
                        this.$emit('refresh', this.books)
                    })
                    .catch(error => console.log(error))
            },
            create_book(book) {
                this.$http.post('/books', book)
                    .then(response => this.refresh())
                    .catch(error => console.log(error))
            },
            update_book(book, key, value) {
                console.log(`update book: ${book} key: ${key} with value: ${value}`)
                this.$http.patch(`/books/${book.id}`, {
                    [key]: value
                }).then(response => {
                    console.log('updated!')
                    this.refresh()
                }).catch(error => { console.log(error.response) })
            },
            get_books() {
                return this.books
            },
            selected(book, attr_key) {
                this.selected_book = { book, attr_key }
                this.$emit('selected', book, attr_key)
            },
            get_selected() {
                return Object.assign({}, this.selected_book)
            }
        },
        created() {
            this.refresh()
            // setInterval(this.refresh, 5000)
        }
    }
</script>
