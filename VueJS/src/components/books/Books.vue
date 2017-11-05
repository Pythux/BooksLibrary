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

        <!-- <button @click="showModalAdd = true">Add a Book</button> -->

        <!-- <modal v-if="showModalAdd" @close="showModalAdd = false">
            <h3 slot="header">Add a Book</h3>
            <div slot="body">
                    <label>ISBN: <input v-model="add.isbn"
                           type="text" name="isbn" value="">
                    </label><br>
                    <label>Title: <input v-model="add.title"
                           type="text" name="title" value="">
                    </label><br>
                    <label>Description: <textarea v-model="add.description"
                              ame="description" rows="6" cols="30"></textarea>
                    </label>
                </form>
            </div>
            <div slot="footer">
                <button @click="create_book">
                  Create
                </button>
            </div>
        </modal> -->
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
