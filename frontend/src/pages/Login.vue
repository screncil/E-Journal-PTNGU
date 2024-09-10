<script>

import { EyeIcon, EyeSlashIcon } from "@heroicons/vue/16/solid/index.js";

import { login } from '../api/api.js'

export default {
  components: { EyeIcon, EyeSlashIcon },
  data() {
    return {
      username: "",
      password: "",
      passwordFieldType: "password",
    }
  },
  computed: {
    isAuthenticated() {
      return localStorage.getItem("token") !== null;
    }
  },
  created() {
    if (this.isAuthenticated) {
      location.href = "/"
    }
  },
  methods: {
    switchVisibilityPassword() {
      this.passwordFieldType = this.passwordFieldType === "password" ? "text" : "password";
    },
    loginUser() {
      login(this.username, this.password)
          .then(res => {
            localStorage.setItem("token", res.data.token)
            location.href = "/"
          })
          .catch(err => {
            if (err.status === 401) {
              const alert = document.getElementById("alert");
              alert.innerHTML = "<div class=\"p-4 mb-4 text-sm text-red-500 rounded-xl bg-red-50 font-normal\" role=\"alert\">\n" +
                  "      <span class=\"font-semibold mr-2\">Невірне ім'я користувача або пароль</span>\n" +
                  "      </div>"
            }
          });

    }
  }
}
</script>


<template>
  <div v-if="!this.isAuthenticated" class="flex min-h-full h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <h2 class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Увійдіть у свій акаунт</h2>
    </div>
    <div class="mt-3 sm:mx-auto sm:w-full sm:max-w-sm text-center" id="alert">
    </div>
    <div class="mt-3 sm:mx-auto sm:w-full sm:max-w-sm">
      <div class="space-y-6">
        <div>
          <label for="username" class="block text-sm font-medium leading-6 text-gray-900">Ім'я користувача</label>
          <div class="relative mt-2">
            <input id="username" placeholder="Ім'я" @focus="usernameFocus = true" @blur="usernameFocus = false" v-model="username" name="username" type="text" required="" class="block w-full indent-3 rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-500 focus:outline-0 sm:text-sm sm:leading-6" />
          </div>
        </div>
        <div>
          <div class="flex items-center justify-between">
            <label for="password" class="block text-sm font-medium leading-6 text-gray-900">Пароль</label>
          </div>
          <div class="relative mt-2">
            <EyeIcon v-if="passwordFieldType === 'text'" aria-hidden="true" class="absolute right-3 top-1/2 transform -translate-y-1/2 w-6 h-6 bg-transparent fill-blue-400 focus:outline-none" @click="switchVisibilityPassword"/>
            <EyeSlashIcon v-else aria-hidden="true" class="absolute right-3 top-1/2 transform -translate-y-1/2 w-6 h-6 bg-transparent fill-gray-500 focus:outline-none" @click="switchVisibilityPassword"/>
            <input v-model="password" placeholder="••••••••••••••••" id="password" name="password" :type="passwordFieldType" autocomplete="current-password" required class="block w-full indent-3 rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-500 focus:outline-0 sm:text-sm sm:leading-6" />
          </div>
        </div>
        <div>
          <button type="submit" class="flex w-full justify-center rounded-md bg-blue-500 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-blue-400 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600" @click="loginUser">Увійти</button>
        </div>
      </div>
    </div>
  </div>

</template>
