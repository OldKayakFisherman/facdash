import axios from "axios";

interface QueueRecord
{
    report_id: string;
    audit_year: number;
    dbkey: number;
    auditee_name: string;
    city: string;
    state: string;
    sflag: number;
    date_received: any;

}

interface WorkflowRecord extends QueueRecord
{
     street: string;
     zipcode: string;
     ein: string
}

interface EinSearchRecord
{
    report_id: string;
    audit_year: number;
    dbkey: number;
    auditee_name: string;
    ein: string
}


export default class APIService
{

    readonly baseurl:string = null;

    constructor(baseUrl: string) {
        this.baseurl = baseUrl
    }

    async getProcessingQueue(){

        let result:QueueRecord[] = []

        await axios.get<QueueRecord[]>(`${this.baseurl}/processing_queue`).
        then(response => {
            result = response.data;
        })

        return result;
    }

    async getWorkflowRecord(report_id: string){
        let result:WorkflowRecord;

        await axios.get<WorkflowRecord>(`${this.baseurl}/workflow_record/${report_id}`).
        then(response => {
            result = response.data;
        })

        return result;

    }

    async getEINSearchRecords(ein: string){
        let result:EinSearchRecord;

        await axios.get<EinSearchRecord>(`${this.baseurl}/einsearch/${ein}`).
        then(response => {
            result = response.data;
        })

        return result;

    }

}