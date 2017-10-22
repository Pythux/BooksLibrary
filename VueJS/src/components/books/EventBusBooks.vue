
<script>
    import { http } from '../../main'

    export default {
        data() {
            return {
                books: [],
            }
        },
        methods: {
            refresh() {
                http.get('/books')
                    .then(response => {
                        this.books = response.data.objects
                        this.$emit('refresh', this.books)
                    })
                    .catch(error => console.log(error))
            },
            create_book(book) {
                http.post('/books', book)
                    .then(response => this.refresh())
                    .catch(error => console.log(error))
            },
            get_books() {
                return this.books
            },
        },
        created() {
            console.log('eventBus Books created()')
            this.refresh()
            // setInterval(this.refresh, 5000)
        }
    }
</script>
