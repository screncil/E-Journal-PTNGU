<template>
  <div class=" top-16 w-56 text-right">
    <Menu as="div" class="relative inline-block text-left">
      <div>
        <MenuButton
            class="inline-flex justify-center rounded-full bg-blue-500 px-2 py-2 text-sm font-medium text-white hover:bg-blue-400/80 focus:outline-none focus-visible:ring-2 focus-visible:ring-white/75"
        >
          <UserCircleIcon
              class="w-5"
          />
        </MenuButton>
      </div>

      <transition
          enter-active-class="transition duration-100 ease-out"
          enter-from-class="transform scale-95 opacity-0"
          enter-to-class="transform scale-100 opacity-100"
          leave-active-class="transition duration-75 ease-in"
          leave-from-class="transform scale-100 opacity-100"
          leave-to-class="transform scale-95 opacity-0"
      >
        <MenuItems
            class="absolute select-none right-0 mt-2 w-56 origin-top-right divide-y divide-gray-100 rounded-md bg-white shadow-lg ring-1 ring-black/5 focus:outline-none"
        >
          <div class="px-1 py-1">
            <MenuItem>
              <p class="p-3 text-gray-600 cursor-default">
                {{ first_name }} {{ last_name }}<br>
                <p class="text-xs">
                  {{ staffText }}
                </p>
              </p>
            </MenuItem>
          </div>
          <div class="px-1 py-1">
            <MenuItem v-slot="{ active }">
              <button
                  @click="this.goTo('/profile')"
                  :class="[
                  active ? 'bg-blue-500 text-white' : 'text-gray-900',
                  'group flex w-full items-center rounded-md px-2 py-2 text-sm',
                ]"
              >
                <UserIcon
                    :active="active"
                    class="mr-2 h-5 w-5 text-blue-400"
                    aria-hidden="true"
                />
                Профіль
              </button>
            </MenuItem>
            <MenuItem v-slot="{ active }">
              <button
                  @click="this.goTo('/grades')"
                  :class="[
                  active ? 'bg-blue-500 text-white' : 'text-gray-900',
                  'group flex w-full items-center rounded-md px-2 py-2 text-sm',
                ]"

              >
                <BookOpenIcon
                    :active="active"
                    class="mr-2 h-5 w-5 text-blue-400"
                    aria-hidden="true"
                />
                Оцінки
              </button>
            </MenuItem>
            <MenuItem v-slot="{ active }">
              <button
                  @click="this.goTo('/groups')"
                  :class="[
                  active ? 'bg-blue-500 text-white' : 'text-gray-900',
                  'group flex w-full items-center rounded-md px-2 py-2 text-sm',
                ]"

              >
                <UserGroupIcon
                    :active="active"
                    class="mr-2 h-5 w-5 text-blue-400"
                    aria-hidden="true"
                />
                Групи
              </button>
            </MenuItem>
          </div>
          <div v-if="is_staff" class="px-1 py-1">
            <MenuItem v-slot="{ active }">
              <button
                  @click="this.goTo('/users')"
                  :class="[
                  active ? 'bg-blue-500 text-white' : 'text-gray-900',
                  'group flex w-full items-center rounded-md px-2 py-2 text-sm',
                ]"
              >
                <UsersIcon
                    :active="active"
                    class="mr-2 h-5 w-5 text-blue-400"
                    aria-hidden="true"
                />
                Користувачі
              </button>
            </MenuItem>
          </div>
          <div class="px-1 py-1">
            <MenuItem v-slot="{ active }">
              <button
                  @click="this.goTo('/settings')"
                  :class="[
                  active ? 'bg-blue-500 text-white' : 'text-gray-900',
                  'group flex w-full items-center rounded-md px-2 py-2 text-sm',
                ]"
              >
                <Cog6ToothIcon
                    :active="active"
                    class="mr-2 h-5 w-5 text-blue-400"
                    aria-hidden="true"
                />
                Налаштування
              </button>
            </MenuItem>
            <MenuItem v-slot="{ active }">
              <button
                  :class="[
                  active ? 'bg-blue-500 text-white' : 'text-gray-900',
                  'group flex w-full items-center rounded-md px-2 py-2 text-sm',
                ]"
                  @click="LogoutTeacher()"
              >
                <ArrowRightEndOnRectangleIcon
                    :active="active"
                    class="mr-2 h-5 w-5 text-blue-400"
                    aria-hidden="true"
                />
                Вихід
              </button>
            </MenuItem>
          </div>
        </MenuItems>
      </transition>
    </Menu>
  </div>
</template>

<script>
import { Menu, MenuButton, MenuItems, MenuItem } from '@headlessui/vue'
import {
  Cog6ToothIcon,
  PencilSquareIcon,
  ArrowRightEndOnRectangleIcon,
  ChevronDownIcon,
  UserCircleIcon,
  UserIcon,
  UserGroupIcon,
  UsersIcon,
  BookOpenIcon
} from "@heroicons/vue/16/solid/index.js";

import { logout } from "../../api/api.js";


export default {
  name: "UserMenuDropdown",
  components: {
    UsersIcon,
    Menu,
    MenuButton,
    MenuItems,
    MenuItem,
    Cog6ToothIcon,
    PencilSquareIcon,
    ArrowRightEndOnRectangleIcon,
    ChevronDownIcon,
    UserCircleIcon,
    UserIcon,
    UserGroupIcon,
    BookOpenIcon
  },
  props: {
    first_name: String,
    last_name: String,
    is_staff: Boolean
  },
  methods: {
    LogoutTeacher() {
      logout()
          .then(() => {
            localStorage.removeItem("token")
            location.href = "/login"
          })
          .catch(err => console.error(err))
    },
    goTo(link) {
      location.href = link;
    }
  },
  computed: {
    staffText() {
      return this.is_staff ? "Викладач • Адмiнiстратор" : "Викладач"
    }
  }
}
</script>
