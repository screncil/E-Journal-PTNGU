<template>
  <div>
    <flat-pickr
        @change="setData"
        v-model="selectedDate"
        :config="config"
        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 mt-2 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
    />
  </div>
</template>

<script>
import FlatPickr from 'vue-flatpickr-component';
import 'flatpickr/dist/flatpickr.css';

export default {
  components: {
    FlatPickr
  },
  data() {
    return {
      selectedDate: null,  // Хранит выбранную дату
      config: {
        dateFormat: 'Y-m-d',  // Формат даты
      }
    };
  },
  methods: {
    setData() {
      this.$emit("updateData", this.selectedDate)
    }
  }
};
</script>

<style scoped>
/* Можете добавить дополнительные стили, если нужно */
</style>
