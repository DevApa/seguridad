$(function() {
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
            {"data": "id"},
            {"data": "name"},
            {"data": "description"},
            {"data": "options"},
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

// $(document).ready(function() {
//     $("#inventory").DataTable({
//         language: {
//             url: '/static/evaluations/language.json',
//         },
//         responsive:true,
//         autoWidth: false,
//         destroy:true,
//         deferRender: true,
//         ajax:{
//             url:window.location.pathname,
//             type:'',
//             data: {
//                 'action': 'searchdata'
//             },
//             dataSrc:''
//         },
//         columns:[
//             {"data": "id"},
//             {"data": "name"},
//             {"data": "description"},
//             {"data": "options"},
//         ],
//         columnDefs: [
//             {
//                 targets:[-1],
//                 class:'text-center',
//                 orderable:false,
//                 render:function (data, type, row) {
//                     return data;
//                 }
//
//             }
//         ],
//         initComplete: function (settings, json) {
//
//         }
//
//     }).$(".dataTables_length select").addClass("form-select form-select-sm");
// });
