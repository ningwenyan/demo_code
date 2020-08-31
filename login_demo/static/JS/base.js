/**
 * Created by kning on 20-8-30.
 */

$(function () {
    $('#ver_code').click(function(){
        $(this).attr('src', "/common/graph_capture/" + '?' + Math.random());
    });
    $('#flush').click(function () {
        $('#ver_code').attr('src', "/common/graph_capture/" + '?' + Math.random())
    })
})