/*** Created by A.J on 2019/10/30.*/$(document).ready(function(){var jlos = jLos.open(0,100);if($("#nawr").val() == 'n'){jlos.set('nawr', 'n');}var nawr = jlos.get('nawr');if(nawr == 'n' && $("#nawr").val() != 'n'){$("#nawr").val('n');}$("#submit").on("click", function(){var subobj = $(this);subobj.children("i").removeClass("d-none");$.post("", subobj.parents("form").serialize(),function(data){subobj.children("i").addClass("d-none");if(data == "ok"){var obj = $.alert({title: "",content: $("#regok").html(),buttons: {confirm: {text: $('#queding').text(),btnClass: 'btn-info',keys: ['enter'],action: function () {window.location.href = $("#logurl").text();}}}});setTimeout(function(){obj.close();window.location.href = $("#logurl").text();},2000);}else if(data == "eok"){$.alert({title: "",content: $("#mailok").html(),buttons: {confirm: {text: $('#queding').text(),btnClass: 'btn-info',keys: ['enter'],action: function () {window.location.href = $("#logurl").text();}}}});}else{$.alert({title: $('#chucuo').text(),content: data,buttons: {confirm: {text: $('#queding').text(),btnClass: 'btn-info',keys: ['enter']}}});}});});});