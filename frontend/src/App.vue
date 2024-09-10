<script>
import Header from "./components/Header.vue";
import Footer from "./components/Footer.vue";
import Settings from "./pages/Settings.vue";
import { getUser } from "./api/api.js";

export default {
  name: "MainApp",
  components: { Header, Footer, Settings },
  computed: {
    isAuthenticated() {
      return localStorage.getItem("token") !== null;
    },
  },
  methods: {
    getUser() {
      if (this.isAuthenticated) {
        getUser(localStorage.getItem("token"))
            .then((response) => {
                this.user = response.data;
            })
      }
    }
  },
  data() {
    return {
      user: {}
    }
  },
  mounted() {
    this.getUser();
  }
}
</script>

<template>
  <header>
    <Header :isAuth="isAuthenticated" :user="user"/>
  </header>
  <main>
    <RouterView :user="user"/>
  </main>
</template>