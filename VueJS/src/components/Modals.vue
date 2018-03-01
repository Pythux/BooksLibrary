<template lang="html">
    <div>
        <!-- <sweet-modal
            v-for="modal in modals"
            :key="modal.ref"
            :ref="modal.ref"
            :icon="modal.icon"
            :title="modal.title"
            @close="modal_close(modal.ref)">
            This is an error…
            <sweet-modal-tab
                id="tab1"
                :icon="ic"
                title="Tab 1<b>yo</b>"
            >C<b>ontents</b> of Tab 1</sweet-modal-tab>
            <sweet-modal-tab
                id="tab2"
                title="Tab 2"
            >Contents of Tab 2</sweet-modal-tab>
        </sweet-modal> -->
        <sweet-modal
            v-for="modal in modals"
            :key="modal.ref"
            :ref="modal.ref"
            :icon="modal.icon"
            :title="modal.title"
            @close="modal_close(modal.ref)">
            {{ modal.msg }}

            <ui-button
                v-if="modal.hasOwnProperty('button')"
                slot="button"
                @click="$refs[modal.ref][0].close()"
            >{{ modal.button }}</ui-button>

        </sweet-modal>
    </div>

</template>

<script>
import { createNamespacedHelpers } from 'vuex'
import { SweetModal, SweetModalTab } from 'sweet-modal-vue'
import UiButton from '../lib/std/UiButton.vue'

const modalsNamespace = createNamespacedHelpers('modals')

export default {
    components: {
        SweetModal,
        SweetModalTab,
        UiButton,
    },
    data() {
        return {
            ic: 'Y<b>oo<b>!',
        }
    },
    computed: {
        ...modalsNamespace.mapGetters({
            modals: 'modals',
        }),
        // modals() {
        //     return this.$store.getters['modals/modals']
        // },
    },
    updated() {
        this.modals.forEach(m => {
            this.$refs[m.ref][0].open()
        })
    },
    methods: {
        ...modalsNamespace.mapActions([
            'del_current',
        ]),
        modal_close(ref) {
            console.log(`closing modal ref: ${ref}`)
            this.del_current()
        },
    },
}
</script>

<style lang="css">
</style>
