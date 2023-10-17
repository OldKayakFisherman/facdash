<script>
import {VDataTable} from "vuetify/labs/components";
import axios from "axios";
import APIService from '../services/APIService'



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
    populateTableHeaders(){
      this.tableHeaders = [
        {
          title: 'Report Id',
          sortable: true,
          key: 'report_id'
        },
        {
          title: 'Audit Year',
          sortable: true,
          value: 'audit_year'
        },
        {
          title: 'Db Key',
          sortable: true,
          value: 'dbkey'
        },
        {
          title: 'Auditee Name',
          sortable: true,
          value: 'auditee_name'
        },
        {
          title: 'City',
          sortable: true,
          value: 'city'
        },
        {
          title: 'State',
          sortable: true,
          value: 'state'
        },
        {
          title: 'SFlag',
          sortable: true,
          value: 'sflag'
        },
        {
          title: 'Date Received',
          sortable: true,
          value: 'date_received'
        },
      ];
    },
    handleClick(value)
    {
      const targetReport = value.target.parentNode.children[0].innerHTML;
      this.$router.push({ name: 'Workflow', params: { reportid: targetReport } })
    }
  },
  beforeMount() {
    this.getQueueRecords();
    this.populateTableHeaders();
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