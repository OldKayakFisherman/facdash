<script>
import {VDataTable} from "vuetify/labs/components";
import APIService from '../services/APIService'
import TableHeaderService from '../services/TableHeaderService'



export default {
  name: "ProcessingQueue",
  components: {VDataTable},

  data(){
    return {
      queueRecords: [],
      tableHeaders: []
    }
  },

  methods: {
    async getQueueRecords(){

      let base_url = import.meta.env.VITE_API_ENDPOINT;
      let apiService = new APIService(base_url);

      this.queueRecords = await apiService.getProcessingQueue();


      /*
      return axios.get(queue_url).
      then(response => {
        this.queueRecords = response.data
      })
       */
    },
    handleClick(value)
    {
      const targetReport = value.target.parentNode.children[0].innerHTML;
      this.$router.push({ name: 'Workflow', params: { reportid: targetReport } })
    }
  },
  beforeMount() {
    this.getQueueRecords();
    this.tableHeaders = new TableHeaderService().populateTableHeaders()

  }
}




</script>

<template>

  <h1>Processing Queue</h1>

  <div id="records0" class="mt-2">
    <v-data-table
        :items="queueRecords"
        :headers="tableHeaders"
        item-key="id"
        class="elevation-1"
        @click:row="handleClick"

    ></v-data-table>
  </div>

</template>

<style scoped>

</style>