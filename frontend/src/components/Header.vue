<template>
  <header class="bg-white">
    <nav class="mx-auto flex max-w-7xl items-center justify-between p-6 lg:px-8" aria-label="Global">
      <div class="flex lg:flex-1">
        <a href="/" class="-m-1.5 p-1.5">
          <span class="sr-only">Your Company</span>
          <img class="h-8 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=blue&shade=500" alt="" />
        </a>
      </div>
      <div class="flex lg:hidden">
        <button type="button" class="-m-2.5 inline-flex items-center justify-center rounded-md p-2.5 text-gray-700" @click="mobileMenuOpen = true">
          <span class="sr-only">Open main menu</span>
          <Bars3Icon class="h-6 w-6" aria-hidden="true" />
        </button>
      </div>
      <PopoverGroup class="hidden lg:flex lg:gap-x-12">
        <Popover class="relative">
          <PopoverButton class="flex items-center gap-x-1 text-sm font-semibold leading-6 text-gray-900">
            Product
            <ChevronDownIcon class="h-5 w-5 flex-none text-gray-400" aria-hidden="true" />
          </PopoverButton>

          <transition enter-active-class="transition ease-out duration-200" enter-from-class="opacity-0 translate-y-1" enter-to-class="opacity-100 translate-y-0" leave-active-class="transition ease-in duration-150" leave-from-class="opacity-100 translate-y-0" leave-to-class="opacity-0 translate-y-1">
            <PopoverPanel class="absolute -left-8 top-full z-10 mt-3 w-screen max-w-md overflow-hidden rounded-3xl bg-white shadow-lg ring-1 ring-gray-900/5">
              <div class="p-4">
                <div v-for="item in products" :key="item.name" class="group relative flex items-center gap-x-6 rounded-lg p-4 text-sm leading-6 hover:bg-gray-50">
                  <div class="flex h-11 w-11 flex-none items-center justify-center rounded-lg bg-gray-50 group-hover:bg-white">
                    <component :is="item.icon" class="h-6 w-6 text-gray-600 group-hover:text-indigo-600" aria-hidden="true" />
                  </div>
                  <div class="flex-auto">
                    <a :href="item.href" class="block font-semibold text-gray-900">
                      {{ item.name }}
                      <span class="absolute inset-0" />
                    </a>
                    <p class="mt-1 text-gray-600">{{ item.description }}</p>
                  </div>
                </div>
              </div>
              <div class="grid grid-cols-2 divide-x divide-gray-900/5 bg-gray-50">
                <a v-for="item in callsToAction" :key="item.name" :href="item.href" class="flex items-center justify-center gap-x-2.5 p-3 text-sm font-semibold leading-6 text-gray-900 hover:bg-gray-100">
                  <component :is="item.icon" class="h-5 w-5 flex-none text-gray-400" aria-hidden="true" />
                  {{ item.name }}
                </a>
              </div>
            </PopoverPanel>
          </transition>
        </Popover>

        <a href="#" class="text-sm font-semibold leading-6 text-gray-900">Features</a>
        <a href="#" class="text-sm font-semibold leading-6 text-gray-900">Marketplace</a>
        <a href="#" class="text-sm font-semibold leading-6 text-gray-900">Company</a>
      </PopoverGroup>
      <div v-if="!isAuth" class="hidden lg:flex lg:flex-1 lg:justify-end">
        <a href="/login" class="text-sm font-semibold leading-6 text-gray-900">Увійти <span aria-hidden="true">&rarr;</span></a>
      </div>
      <div v-else class="hidden lg:flex lg:flex-1 lg:justify-end">
        <StudentMenuDropdown v-if="user.status === 'student'" :first_name="user.first_name" :last_name="user.last_name" :group="user.group" :isAuth="isAuth" />
        <TeacherMenuDropdown v-else :first_name="user.first_name" :last_name="user.last_name" :is_staff="user.is_staff" />
      </div>
    </nav>
    <Dialog class="lg:hidden" @close="mobileMenuOpen = false" :open="mobileMenuOpen">
      <div class="fixed inset-0 z-10" />
      <DialogPanel class="fixed inset-y-0 right-0 z-10 w-full overflow-y-auto bg-white px-6 py-6 sm:max-w-sm sm:ring-1 sm:ring-gray-900/10">
        <div class="flex items-center justify-between">
          <a href="#" class="-m-1.5 p-1.5">
            <span class="sr-only">Your Company</span>
            <img class="h-8 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=blue&shade=500" alt="" />
          </a>
          <button type="button" class="-m-2.5 rounded-md p-2.5 text-gray-700" @click="mobileMenuOpen = false">
            <span class="sr-only">Close menu</span>
            <XMarkIcon class="h-6 w-6" aria-hidden="true" />
          </button>
        </div>
        <div class="mt-6 flow-root">
          <div class="-my-6 divide-y divide-gray-500/10">
            <div class="space-y-2 py-6">
              <a href="#" class="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50">Features</a>
              <a href="#" class="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50">Marketplace</a>
              <a href="#" class="-mx-3 block rounded-lg px-3 py-2 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50">Company</a>
            </div>
            <div class="py-6">
              <a v-if="!isAuth" href="/login" class="-mx-3 block rounded-lg px-3 py-2.5 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50">Увійти <span aria-hidden="true">&rarr;</span></a>
              <Disclosure v-else as="div" class="-mx-3" v-slot="{ open }">
                <DisclosureButton class="flex w-full items-center justify-between rounded-lg py-2 pl-3 pr-3.5 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50">
                  Профіль
                  <ChevronDownIcon :class="[open ? 'rotate-180' : '', 'h-5 w-5 flex-none']" aria-hidden="true" />
                </DisclosureButton>
                <DisclosurePanel class="mt-2 space-y-2">
                  <DisclosureButton v-if="user.status === 'student'" v-for="item in student_cards" :key="item.name" as="a" :href="item.href" class="rounded-lg py-2 pl-6 pr-3 text-sm font-semibold leading-7 text-gray-900 hover:bg-gray-50 flex flex-row items-center">
                    <component :is="item.icon" class="w-5 h-5 mr-1.5" />
                    {{ item.name }}
                  </DisclosureButton>
                  <DisclosureButton v-else-if="user.status === 'teacher'" v-for="item in teacher_cards" :key="item.name" as="a" :href="item.href" class="rounded-lg py-2 pl-6 pr-3 text-sm font-semibold leading-7 text-gray-900 hover:bg-gray-50 flex flex-row items-center">
                    <component :is="item.icon" class="w-5 h-5 mr-1.5" />
                    {{ item.name }}
                  </DisclosureButton>
                  <DisclosureButton as='a' href="/users" v-if="user.status === 'teacher' && user.is_staff" class="rounded-lg py-2 pl-6 pr-3 text-sm font-semibold leading-7 text-gray-900 hover:bg-gray-50 flex flex-row items-center">
                    <UsersIcon 
                      class="w-5 h-5 mr-1.5"
                      aria-hidden="true"
                    />
                    Користувачі
                  </DisclosureButton>
                  <DisclosureButton as="a" href="/settings" class="rounded-lg py-2 pl-6 pr-3 text-sm font-semibold leading-7 text-gray-900 hover:bg-gray-50 flex flex-row items-center">
                      <Cog6ToothIcon 
                        class="w-5 h-5 mr-1.5"
                      />
                      Налаштування
                  </DisclosureButton>
                  <DisclosureButton class="rounded-lg py-2 pl-6 pr-3 text-sm font-semibold leading-7 text-gray-900 hover:bg-gray-50 flex flex-row items-center" @click="LogoutUser">
                    <ArrowRightEndOnRectangleIcon 
                      class="w-5 h-5 mr-1.5"
                    />
                    Вихід
                  </DisclosureButton>
                </DisclosurePanel>
              </Disclosure>
            </div>
          </div>
        </div>
      </DialogPanel>
    </Dialog>
  </header>
</template>

<script>
import { ref } from 'vue'
import {
  Dialog,
  DialogPanel,
  Disclosure,
  DisclosureButton,
  DisclosurePanel,
  Popover,
  PopoverButton,
  PopoverGroup,
  PopoverPanel,
} from '@headlessui/vue'
import {
  ArrowPathIcon,
  Bars3Icon,
  ChartPieIcon,
  CursorArrowRaysIcon,
  FingerPrintIcon,
  SquaresPlusIcon,
  XMarkIcon,
  UserIcon,
  BookOpenIcon,
  Cog6ToothIcon,
  ArrowRightEndOnRectangleIcon,
  UsersIcon,
  UserGroupIcon
} from '@heroicons/vue/24/outline'
import { ChevronDownIcon, PhoneIcon, PlayCircleIcon } from '@heroicons/vue/20/solid'
import StudentMenuDropdown from "./MenuDropdown/StudentMenuDropdown.vue";
import TeacherMenuDropdown from "./MenuDropdown/TeacherMenuDropdown.vue";

import { logout } from '../api/api.js';
 

export default {
  name: 'Header',
  components: {
    Dialog,
    DialogPanel,
    Disclosure,
    DisclosureButton,
    DisclosurePanel,
    Popover,
    PopoverButton,
    PopoverGroup,
    PopoverPanel,
    ArrowPathIcon,
    Bars3Icon,
    ChartPieIcon,
    CursorArrowRaysIcon,
    FingerPrintIcon,
    SquaresPlusIcon,
    XMarkIcon,
    ChevronDownIcon,
    PhoneIcon,
    PlayCircleIcon,
    StudentMenuDropdown,
    TeacherMenuDropdown,
    UserIcon,
    BookOpenIcon,
    Cog6ToothIcon,
    ArrowRightEndOnRectangleIcon,
    UsersIcon,
    UserGroupIcon
  },
  data() {
    return {
      student_cards: [
        { name: 'Сторінка', href: '/profile', icon: UserIcon },
        { name: 'Мої оцінки', href: '/grades', icon: BookOpenIcon }
      ],
      teacher_cards: [
        { name: 'Сторінка', href: '/profile', icon: UserIcon },
        { name: 'Оцінки', href: '/grades', icon: BookOpenIcon },
        { name: 'Групи', href: '/groups', icon: UserGroupIcon }
      ],
      mobileMenuOpen: ref(false),
    }
  },
  props: ['user', 'isAuth'],
  methods: {
    LogoutUser() {
      logout(localStorage.getItem("token"))
          .then(() => {
            localStorage.removeItem("token")
            location.href = "/login"
          })
          .catch(err => console.error(err))
    },
  }
}
</script>