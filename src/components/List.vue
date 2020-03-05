<template>
  <div class="list">
    <Cell v-for="(item, i) in items"
          :item="item"
          :rate="rate"
          :country="country"
          :key="i" />
  </div>
</template>

<script>
import Cell from './Cell.vue'
export default {
  name: 'List',
  components: {
    Cell
  },
  props: {
    rate: Number,
    items: Array,
    country: String
  }
}
</script>

<style lang="scss">
.list {
  height: calc(100vh - 106px);
  overflow-y: scroll;
}
</style>
