<template>
  <div class="table-with-search">
    <div class="search">
      <el-select
        v-model="property"
        filterable
        placeholder="Please enter an address"
        v-on:change="handleSelect"
        style="width: 50%"
      >
        <el-option
          v-for="property in unselectedProperties"
          :key="property.index" 
          :value="property.index"
          :label="property.FULL_ADDRESS"
        >
        </el-option>
      </el-select>
    </div>
    <div class="table">
      <el-table 
        :data="selectedProperties"
        style="wdith: 100%"
      >
        <el-table-column prop="FULL_ADDRESS" label="Full Address" />
        <el-table-column prop="CLASS_DESCRIPTION" label="Class Description" />
        <el-table-column label="Delete?">
          <template #default="scope">
            <el-button 
              @click="handleDelete(scope)"
              type="danger"
            >
              Delete
            </el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
  import http from "../http-common";
  export default {
    name: "Table",
      data () {
      return {
        searchAddress: '',
        unselectedProperties: [],
        selectedProperties: [],
        loading: false,
      }
    },
    mounted() {
      this.getUnselectedProperties()
      this.getSelectedProperties()
    },
    methods: {
      async getUnselectedProperties() {
        http
        .get(`/properties?SELECTED=false`)
        .then(response => (
          this.unselectedProperties = response.data.results
        ))
      },
      async getSelectedProperties() {
        http
        .get(`/properties?SELECTED=true`)
        .then(response => (
          this.selectedProperties = response.data.results
        ))
      },
      async handleDelete(scope) {
        try {
          await http
          .put(`/properties/${scope.row.index}`, {
            "SELECTED": false
          })
        } finally {
          this.getUnselectedProperties()
          this.getSelectedProperties()
        }
      },
      async handleSelect(event) {
        try {
          await http
          .put(`/properties/${event}`, {
            "SELECTED": true
          })
        } finally {
          this.getUnselectedProperties()
          this.getSelectedProperties()
          this.value = ''
        }
      }
    },
    props: {
    },
  };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
  h1 {
    color: $primary
  }
</style>
