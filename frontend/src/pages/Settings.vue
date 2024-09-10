<script>


export default {
  name: 'Settings',
  props: { user: {} },
  created() {
    console.log(this.user)
  }
}
</script>

<template>
  Settings Page
</template>
