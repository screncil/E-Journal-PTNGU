<script>

import NotFound from '../components/NotFound.vue'

export default {
  name: 'Users',
  props: {
    user: {}
  },
  components: { NotFound }
}

</script>

<template>
<p v-if="user.is_staff">
  users page
</p>
  <p v-else>
    <NotFound />
  </p>
</template>

<style scoped>

</style>