<template>
  <div v-if="is_students">
    <select @change="setData" v-model="selected" class="w-full bg-transparent outline-none">
      <option selected disabled>{{ listbox_name }}</option>
      <option v-for="item in items" :value="item.id">{{ item.first_name }} {{ item.last_name }}</option>
    </select>
  </div>
  <div v-else>
    <select @change="setData" v-model="selected" class="w-full bg-transparent outline-none">
      <option selected disabled>{{ listbox_name }}</option>
      <option v-for="item in items" :value="item.id">{{ item.name }}</option>
    </select>
  </div>
</template>

<script>
export default {
  props: {
    items: [],
    listbox_name: String,
    disabled: Boolean,
    is_students: Boolean
  },
  data() {
    return {
      selected: ""
    }
  },
  methods: {
    setData() {
      this.$emit("updateData", this.selected)
    }
  }
}
</script>