<template lang="html">
    <div>
        <ui-table
            :data="books"
            :name_header="['Title', 'ISBN', 'Authors', 'Subjects']"
            :map_data="map_data"
            :axe="table"
            @click="table_clicked"
        />

        <hr>
        <transition
            name="slide-fade"
            mode="out-in"
            duration="1000">
            <router-view/>
        </transition>
    </div>
</template>

<script>
import UiTable from '../../lib/std/UiTable.vue'
import UiButton from '../../lib/std/UiButton.vue'

export default {
    components: {
        // Modal,
        UiTable,
        UiButton,
    },
    props: {
        table: {
            type: String,
            default: 'horizontal',
        },
    },
    data() {
        return {
            showModalAdd: false,
            books: [],
            show: false,
            map_data: ['title', 'isbn', this.get_authors, this.get_subjects],
            map_index: ['title', 'isbn', 'authors', 'subjects'],
        }
    },
    created() {
        this.books = this.$eventBus.books.get_books()
        this.$eventBus.books.$on('refresh', b => {
            this.books = b
        })
        this.$eventBus.books.$on('selected', this.redirect_BookEdit)
    },
    beforeDestroy() {
        this.$eventBus.books.$off('selected', this.redirect_BookEdit)
    },
    methods: {
        get_authors(book) {
            return book.authors.map(author =>
                `${author.first_name[0]}. ${author.last_name}`).join(', ')
        },
        get_subjects(book) {
            return book.subjects.map(subject => subject.subject).join(', ')
        },
        table_clicked(book, attrIndex) {
            this.$eventBus.books.selected(book, this.map_index[attrIndex])
        },
        redirect_BookEdit(obj, index) {
            this.$router.push({
                name: 'bookDetail',
                params: { id: obj.id },
            })
        },
    },
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
