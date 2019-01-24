<template>
  <transition
    @before-enter="beforeEnter"
    @enter="enter"
    @after-enter="afterEnter"
    @enter-cancelled="enterCancelled"
    @leave="leave"
    @after-leave="afterLeave"
    @leave-cancelled="leaveCancelled"
  >
    <slot />
  </transition>
</template>

<script>
export default {
    methods: {
        beforeEnter (el) {
            // el._parent = el.parentNode
            el._initialStyle = {
                transition: el.style.transition,
                visibility: el.style.visibility,
                overflow: el.style.overflow,
                width: el.style.width
            }
        },
        enter (el) {
            const initialStyle = el._initialStyle
            el.style.setProperty('transition', 'none', 'important')
            el.style.visibility = 'hidden'
            const width = `${el.offsetWidth}px`
            el.style.visibility = initialStyle.visibility
            el.style.overflow = 'hidden'
            el.style.width = 0
            void el.offsetWidth // force reflow
            el.style.transition = initialStyle.transition
            el.style.transition = 'all 0.6s'

            requestAnimationFrame(() => {
                el.style.width = width
            })
        },

        afterEnter: resetStyles,
        enterCancelled: resetStyles,

        leave (el) {
            el._initialStyle = {
                overflow: el.style.overflow,
                width: el.style.width
            }
            el.style.overflow = 'hidden'
            el.style.width = `${el.offsetWidth}px`

            // Force repaint to make sure the
            // animation is triggered correctly.
            void getComputedStyle(el).width

            requestAnimationFrame(() => el.style.width = 0)
        },
        afterLeave,
        leaveCancelled: afterLeave,
    },
}
function afterLeave (el) {
    resetStyles(el)
}
function resetStyles (el) {
    el.style.overflow = el._initialStyle.overflow
    el.style.width = el._initialStyle.width
    delete el._initialStyle
}
</script>
