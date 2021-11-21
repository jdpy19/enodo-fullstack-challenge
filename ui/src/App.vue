<template>
  <div>
    <h1>Enodo Challenge</h1>
    <Search />
    <Table />
  </div>
</template>

<script>

import Table from "./components/Table.vue";

export default {
  name: "App",
  components: {
    Table
  },
};
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: $primary;
  margin-top: 60px;
}
</style>
