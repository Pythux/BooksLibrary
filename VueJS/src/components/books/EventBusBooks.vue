<script>
export default {
    data() {
        return {
            books: [],
            selected_book: { book: {}, attr_key: null },
        }
    },
    created() {
        this.refresh()
        // setInterval(this.refresh, 5000)
    },
    methods: {
        refresh() {
            this.$http.get('/books')
                .then(response => {
                    this.books = response.data.objects
                    this.$emit('refresh', this.books)
                })
        },
        create_book(book) {
            this.$http.post('/books', book)
                .then(() => this.refresh())
        },
        update_book(book, key, value, callbackCatch, callbackFinally) {
            console.log(`try update: ${key}:=${value}`)
            this.$http.patch(`/books/${book.id}`, {
                [key]: value,
            }).then(() => { this.refresh() })
                .catch(callbackCatch)
                .then(callbackFinally)
        },
        get_books() {
            return this.books
        },
        selected(book, attrKey) {
            this.selected_book = { book, attrKey }
            this.$emit('selected', book, attrKey)
        },
        get_selected() {
            return Object.assign({}, this.selected_book)
        },
    },
}
</script>
