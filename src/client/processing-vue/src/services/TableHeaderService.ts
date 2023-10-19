

class TableHeaderService
{
    getProcessingQueueHeaders()
    {
        return [
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
    }

    getEinSearchHeaders(){
        return [
            {
                title: 'DB Key',
                sortable: true,
                key: 'dbkey'
            },
            {
                title: 'Audit Year',
                sortable: true,
                key: 'audit_year'
            },
            {
                title: 'EIN',
                sortable: true,
                key: 'ein'
            },
            {
                title: 'Auditee Name',
                sortable: true,
                key: 'auditee_name'
            },
            {
                title: 'Report Id',
                sortable: true,
                key: 'report_id'
            }
        ];
    }
}