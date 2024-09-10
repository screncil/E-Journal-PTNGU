<script>

import AddGradeModel from "../components/Modals/AddGradeModel.vue";

export default {
  name: 'Grades',
  props: {
    user: {}
  },
  components: {
    AddGradeModel,
  }
}

</script>

<template>
<div class="ml-10 mt-5 w-1/6" v-if="user.status === 'teacher'">
  <div v-if="user.status === 'teacher'" id="model_button">
    <AddGradeModel />
  </div>
  <div class="">

  </div>
</div>
</template>

<style scoped>

</style>