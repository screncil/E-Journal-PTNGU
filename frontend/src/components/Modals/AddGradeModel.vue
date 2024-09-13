<template>
  <div class="inset-0 flex items-center">
    <button
        type="button"
        @click="openModal"
        class="rounded-md px-3 py-2 text-sm font-medium border-2 border-blue-500/50 hover:text-white hover:bg-blue-500 focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500/75 group flex items-center"
    >
      <PencilSquareIcon
          class=" h-5 w-5 text-blue-400"
          aria-hidden="true"
      />
    </button>
  </div>
  <TransitionRoot appear :show="isOpen" as="template">
    <Dialog as="div" @close="closeModal" class="relative z-10">
      <TransitionChild
          as="template"
          enter="duration-300 ease-out"
          enter-from="opacity-0"
          enter-to="opacity-100"
          leave="duration-200 ease-in"
          leave-from="opacity-100"
          leave-to="opacity-0"
      >
        <div class="fixed inset-0 bg-black/25" />
      </TransitionChild>

      <div class="fixed inset-0 overflow-y-auto">
        <div
            class="flex min-h-full items-center justify-center p-4 text-center"
        >
          <TransitionChild
              as="template"
              enter="duration-300 ease-out"
              enter-from="opacity-0 scale-95"
              enter-to="opacity-100 scale-100"
              leave="duration-200 ease-in"
              leave-from="opacity-100 scale-100"
              leave-to="opacity-0 scale-95"
          >
            <DialogPanel
                class="w-full max-w-md overflow-hidden rounded-2xl bg-white p-6 text-left align-middle shadow-xl transition-all divide-y divide-gray-200"
            >
              <DialogTitle
                  as="h3"
                  class="flex flex-row items-center select-none text-lg font-medium leading-6 text-gray-900 mb-5"
              >
                Поставити оцінку
                <PencilSquareIcon
                    class="h-5 w-5 ml-2"
                    aria-hidden="true"
                />
                <XMarkIcon
                  class="w-5 h-5 align ml-auto fill-red-500 hover:bg-gray-500/20 rounded-md"
                  aria-hidden="true"
                  @click="closeModal"
                />
              </DialogTitle>
              <div>
                <div class="mt-4">
                  <label for="groups" class="text-sm select-none text-gray-500 flex flex-row">
                    <UserGroupIcon
                        class="w-5 h-5 mr-1.5"
                    />
                    Виберіть групу
                  </label>
                  <MyListBox class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 mt-2 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" id="groups" :is_students="false" :items="groups" listbox_name="Групи" @updateData="setGroupData"/>
                </div>
                <div class="mt-2">
                  <label for="students" class="text-sm select-none text-gray-500 flex flex-row">
                    <UserIcon
                      class="w-5 h-5 mr-1.5"
                    />
                    Виберіть студента
                  </label>
                  <MyListBox class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 mt-2 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" id="students" @updateData="setStudentId" :is_students="true" :items="students" listbox_name="Студенти"/>
                </div>
                <div class="mt-2 mb-5">
                  <label for="subjects" class="text-sm select-none text-gray-500 flex flex-row">
                    <BookOpenIcon
                        class="w-5 h-5 mr-1.5"
                    />
                    Виберіть предмет
                  </label>
                  <MyListBox id="subjects" @updateData="setSubjectId" :is_students="false" :items="subjects" listbox_name="Предмети" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 mt-2 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"/>
                </div>
              </div>
              <div>
              <div class="mt-3">
                <label for="theme" class="mb-2 select-none text-sm text-gray-500 dark:text-white flex flex-row items-center">
                  <DocumentTextIcon
                    class="w-5 h-5 mr-1.5"
                  />
                  Вкажіть тему
                </label>
                <input v-model="themee" type="text" id="theme" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 mt-2 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Наприклад: Контрольна робота" required />
              </div>
                <div class="mt-3 select-none">
                  <label for="datepicker" class="mb-2 text-sm text-gray-500 dark:text-white flex flex-row items-center">
                    <CalendarDaysIcon
                      class="w-5 h-5 mr-1.5"
                    />
                    Вкажіть дату
                  </label>
                  <input type="date" id="date" v-model="date" @updateData="setDate" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 mt-2 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"/>
                </div>
                <div class="mt-3">
                  <label for="grade" class="mb-2 select-none text-sm text-gray-500 dark:text-white">Вкажіть оцінку</label>
                  <input type="number" id="grade" v-model="grade" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 mt-2 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="1 / 5 або 1 / 12"/>
                </div>
              </div>
              <div class="mt-4">
                <button v-if="!loading"
                    type="button"
                    class="w-full mt-5 inline-flex justify-center rounded-md border border-transparent bg-blue-300 px-4 py-2 text-sm font-medium text-blue-900 hover:bg-blue-200 focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-2"
                    @click="setupGrade"
                >
                  Поставити
                  <ArrowLongRightIcon
                    class="w-5 h-5 ml-2 fill-current"
                  />
                </button>
                <button v-else
                    type="button"
                    disabled
                    class="w-full mt-5 inline-flex justify-center rounded-md border border-transparent bg-blue-200 px-4 py-2 text-sm font-medium text-blue-900 focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-2"
                    @click="setupGrade"
                >
                  <Loading />
                </button>
              </div>
            </DialogPanel>
          </TransitionChild>
        </div>
      </div>
    </Dialog>
  </TransitionRoot>
</template>

<script>

import MyListBox from "../ListBox.vue";

import { allGroups, studentsByGroup, subjectsByCourse, addGrade } from "../../api/api.js";

import Loading from '../Loading.vue'

import {
  TransitionRoot,
  TransitionChild,
  Dialog,
  DialogPanel,
  DialogTitle,
} from '@headlessui/vue'

import {
    PencilSquareIcon,
    BookOpenIcon,
    UserIcon,
    UserGroupIcon,
    CalendarDaysIcon,
    ArrowLongRightIcon,
    DocumentTextIcon,
    XMarkIcon
} from '@heroicons/vue/24/outline'

import { Cog6ToothIcon } from "@heroicons/vue/16/solid/index.js";
import Datepicker from "../Datepicker.vue";


export default {
  name: 'AddGradeModal',
  components: {
    Datepicker,
    Loading,
    Cog6ToothIcon,
    TransitionRoot,
    TransitionChild,
    Dialog,
    DialogPanel,
    DialogTitle,
    PencilSquareIcon,
    MyListBox,
    BookOpenIcon,
    UserIcon,
    UserGroupIcon,
    CalendarDaysIcon,
    ArrowLongRightIcon,
    DocumentTextIcon,
    XMarkIcon
  },
  data() {
    return {
      isOpen: false,
      groups: [],
      subjects: [],
      students: [],
      group_id: null,
      student_id: null,
      subject_id: null,
      grade: null,
      themee: "",
      loading: false,
      date: ""
    }
  },
  methods: {
    closeModal() {
      this.resetListBoxFields()
      this.isOpen = false;
    },
    setDate(data) {
      this.date = data;
    },
    setupGrade() {
      this.loading = true;
      setTimeout(() => {
        if (!Number.isInteger(this.group_id)) {
          document.getElementById("groups").classList.replace("border-gray-300","border-red-500");
          this.loading = false;
        } else {
          document.getElementById("groups").classList.replace("border-red-500","border-gray-300");
        }

        if (!Number.isInteger(this.student_id)) {
          document.getElementById("students").classList.replace("border-gray-300","border-red-500");
          this.loading = false;
        } else {
          document.getElementById("students").classList.replace("border-red-500","border-gray-300");
        }

        if (this.subject_id === null) {
          document.getElementById("subjects").classList.replace("border-gray-300","border-red-500");
          this.loading = false;
        } else {
          document.getElementById("subjects").classList.replace("border-red-500","border-gray-300");
        }

        if (!Number.isInteger(this.grade)) {
          document.getElementById("grade").classList.replace("border-gray-300","border-red-500");
          this.loading = false;
        } else {
          document.getElementById("grade").classList.replace("border-red-500","border-gray-300");
        }

        if (this.themee === '') {
          document.getElementById("theme").classList.replace("border-gray-300","border-red-500");
          this.loading = false;
        } else {
          document.getElementById("theme").classList.replace("border-red-500","border-gray-300");
        }

        if (this.date === '') {
          document.getElementById("date").classList.replace("border-gray-300","border-red-500");
          this.loading = false;
        } else {
          document.getElementById("date").classList.replace("border-red-500","border-gray-300");
        }
      }, 300)
      addGrade(this.grade, this.themee, this.student_id, this.subject_id, this.date)
          .then(resp => {
            this.loading = false;
            this.resetListBoxFields()
            this.isOpen = false;
          })
    },
    resetListBoxFields() {
      this.date = "";
      this.themee = "";
      this.subject_id = null;
      this.grade = null;
      this.groups = [];
      this.students = [];
      this.subjects = [];
      document.getElementById("theme").value = null;
      document.getElementById("grade").value = null;
    },
    openModal() {
      this.isOpen = true;
      this.getAllGroups()
    },
    setGroupData(data) {
      this.group_id = data;
      this.getStudents();
      this.getSubjectsOfCourse();
    },
    setStudentId(data) {
      this.student_id = data;
    },
    setSubjectId(data) {
      this.subject_id = data;
    },
    getSubjectsOfCourse() {
      subjectsByCourse(localStorage.getItem("token"), this.group_id).then(resp => {
        this.subjects = resp.data;
      })
    },
    getAllGroups() {
      allGroups(localStorage.getItem("token"))
          .then((res) => {
            this.groups = res.data;
          })
    },
    getStudents() {
      studentsByGroup(localStorage.getItem("token"), this.group_id)
          .then((res) => {
            this.students = res.data;
          })
    }
  }
}
</script>
