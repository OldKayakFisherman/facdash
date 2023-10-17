<script>


import APIService from "../services/APIService";

export default {
  name: "DBKeyWorkflow",
  base_url: import.meta.env.VITE_API_ENDPOINT,
  data() {
    return {
      workflowItem: {},
      einSearchRecords: []
    }
  },
  methods:{
    async populateWorkflowRecord(){
      let apiService = new APIService(this.base_url);
      let reportId = this.$route.params.reportid;
      this.workflowItem = await apiService.getWorkflowRecord(reportId)
      console.log(this.workflowItem);
    },
    async doEINSearch(){
      let apiService = new APIService(this.base_url);
        
    }

  },
  async beforeMount() {
    await this.populateWorkflowRecord();

  }

}
</script>

<template>
  <div class="row mt-5 mb-2">
    <div class="col"><h5 class="underline">Audit Info</h5></div>
  </div>

  <div class="row row-cols-lg-auto g-3 align-items-center">

    <div class="col">
      <span class="audit_info_label">Report:</span>
      <span class="ms-1">{{this.workflowItem.report_id}}</span>
    </div>

    <div class="col">
      <span class="audit_info_label">Audit Year:</span>
      <span class="ms-1">{{this.workflowItem.audit_year}}</span>
    </div>

    <div class="col">
      <span class="audit_info_label">EIN:</span>
      <span class="ms-1">{{ this.workflowItem.ein }}</span>
    </div>

    <div class="col">
      <span class="audit_info_label">Name:</span>
      <span class="ms-1">{{this.workflowItem.auditee_name}}</span>
    </div>

  </div>

  <div class="row row-cols-lg-auto g-3 align-items-center">

    <div class="col">
      <span class="audit_info_label">Street:</span>
      <span class="ms-1">{{this.workflowItem.street}}</span>
    </div>

    <div class="col">
      <span class="audit_info_label">City:</span>
      <span class="ms-1">{{this.workflowItem.city}}</span>
    </div>

    <div class="col">
      <span class="audit_info_label">Zip:</span>
      <span class="ms-1">{{this.workflowItem.zipcode}}</span>
    </div>


  </div>

  <div class="row mt-5 mb-2">
    <div class="col"><h5 class="underline">Search Criteria</h5></div>
  </div>

  <div class="row row-cols-lg-auto g-3 align-items-center">
    <div class="col">
      <span for="txtSearchName" class="audit_info_label">Name:</span>
        <input id="txtSearchName" type="text" class="ms-2" placeholder="Name" />
    </div>
    <div class="col">
      <span for="txtSearchDbKey" class="audit_info_label">DbKey:</span>
        <input id="txtSearchDbKey" type="text" class="ms-2" placeholder="DbKey" />
    </div>
    <div class="col">
      <input type="button" class="btn btn-primary" value="Search"/>
    </div>

  </div>

  <div class="row row-cols-lg-auto g-3 align-items-center mt-3">
    <table class="table table-striped table-hover">
      <thead>
      <tr>
        <th>DbKey</th>
        <th>Audit Year</th>
        <th>EIN</th>
        <th>Auditee Name</th>
        <th>Report Id</th>
      </tr>
      </thead>
      <tbody>
      <tr>
        <td>234567</td>
        <td>2019</td>
        <td>659875656125</td>
        <td>Company ABC</td>
        <td>CEN-234567-2019</td>
      </tr>
      <tr>
        <td>234567</td>
        <td>2020</td>
        <td>659875656125</td>
        <td>Company ABC</td>
        <td>CEN-234567-2020</td>
      </tr>
      <tr>
        <td>234567</td>
        <td>2021</td>
        <td>659875656125</td>
        <td>Company ABC</td>
        <td>CEN-234567-2021</td>
      </tr>
      <tr>
        <td>234567</td>
        <td>2022</td>
        <td>659875656125</td>
        <td>Company ABC</td>
        <td>CEN-234567-2022</td>
      </tr>
      </tbody>
    </table>

  </div>

  <div class="row row-cols-lg-auto g-3 align-items-center mt-3">
    <input type="button" class="btn btn-secondary" value="Assign Db Key">
    <input type="button" class="btn btn-secondary ms-2" value="Create Db Key">
    <input type="button" class="btn btn-secondary ms-2" value="No Db Key Match">
    <input type="button" class="btn btn-secondary ms-2" value="Reject Submission">
    <input type="button" class="btn btn-danger ms-5" value="Reset">
  </div>



</template>

<style scoped>

  .audit_info_label{
    font-weight: 700;
  }

  .underline {
    text-decoration-line: underline;
  }


</style>