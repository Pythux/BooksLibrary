<template lang="html">
    <div>
        <ui-table
            :data='books'
            :name_header="['Title', 'ISBN', 'Authors', 'Subjects']"
            :map_data="['title', 'isbn', get_authors, get_subjects]"
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
    import { http, eventBus } from '../../main'
    // import Modal from '../../lib/wrap/Modal.vue'
    import UiTable from '../../lib/std/UiTable.vue'
    import UiButton from '../../lib/std/UiButton.vue'

    export default {
        data() {
            return {
                showModalAdd: false,
                books: [],
                show: false,
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
            table_clicked(obj, index) {
                console.log(obj, index);
                this.$eventBus.books.$emit('selected', obj, )
            }
        },
        created() {
            console.log('App.vue created()')
            this.books = eventBus.books.get_books()
            eventBus.books.$on('refresh', b => {console.log("get_update");this.books = b})
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
