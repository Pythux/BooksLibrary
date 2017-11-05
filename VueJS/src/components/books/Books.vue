<template lang="html">
    <div>
        <ui-table
            :data='books'
            :name_header="['Title', 'ISBN', 'Authors', 'Subjects']"
            :map_data="map_data"
            :axe='table'
            @click='table_clicked'
        />

        <hr>
        <transition name="slide-fade" mode="out-in" duration="1000">
            <router-view></router-view>
        </transition>
    </div>
</template>

<script>
    import { http } from '../../main'
    import UiTable from '../../lib/std/UiTable.vue'
    import UiButton from '../../lib/std/UiButton.vue'

    export default {
        data() {
            return {
                showModalAdd: false,
                books: [],
                show: false,
                map_data: ['title', 'isbn', this.get_authors, this.get_subjects],
                map_index: ['title', 'isbn', 'authors', 'subjects']
            }
        },
        props: {
            table: {
                type: String,
                default: 'horizontal'
            },
        },
        components: {
            // Modal,
            UiTable,
            UiButton,
        },
        methods: {
            get_authors(book) {
                return book.authors.map(author =>
                    author.first_name[0] + '. ' + author.last_name
                ).join(', ')
            },
            get_subjects(book) {
                return book.subjects.map(subject => subject.subject).join(', ')
            },
            table_clicked(book, attr_index) {
                console.log(`select: ${book}, ${attr_index}`)
                this.$eventBus.books.selected(book, this.map_index[attr_index])
            },
            redirect_BookEdit(obj, index) {
                this.$router.push({
                    name: 'bookDetail',
                    params: { id: obj.id }
                })
            }
        },
        created() {
            this.books = this.$eventBus.books.get_books()
            this.$eventBus.books.$on('refresh', b => {
                console.log("get_update");this.books = b
            })
            this.$eventBus.books.$on('selected', this.redirect_BookEdit)
        },
        beforeDestroy() {
            this.$eventBus.books.$off('selected', this.redirect_BookEdit)
        }
    }
</script>

<style scoped>
    /*transition: */
    .bounce-enter-active {
      animation: bounce-in .2s;
    }
    .bounce-leave-active {
      animation: bounce-in .5s reverse;
    }
    @keyframes bounce-in {
      0% {
        transform: scale(0);
      }
      50% {
        transform: scale(1.5);
      }
      100% {
        transform: scale(1);
      }
    }
</style>
