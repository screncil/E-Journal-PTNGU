<script>

export default {
  name: 'MainPage',
  data() {
    return {

    }
  },
  props: { user: {} },
  computed: {
    isAuthenticated() {
      return localStorage.getItem("token") !== null;
    }
  },
  created() {
    if (!this.isAuthenticated) {
      location.href = '/login'
    }
  }
}
</script>

<template>
  <div class="h-f">
    <div class="" v-if="user.status === 'student'">
      Main Page Student
    </div>
    <div class="" v-else>
      Main Page Teacher
    </div>
  </div>
</template>
