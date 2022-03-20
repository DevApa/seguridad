$(function() {
    console.log(data);
    $('#inventory').DataTable( {
       responsive:true,
        autoWidth: false,
        destroy:true,
        deferRender: true,
        ajax:{
            url:window.location.pathname,
            type:'',
            data: {
                'action': 'searchdata'
            },
            dataSrc:''
        },
        columns:[
            {'data': 'id'},
            {'data': 'name'},
            {'data': 'description'},
            {'data': 'options'},
        ],
        columnDefs: [
            {
                targets:[-1],
                class:'text-center',
                orderable:false,
                render:function (data, type, row) {
                    return data;
                }

            }
        ],
        initComplete: function (settings, json) {

        }
    });
} );