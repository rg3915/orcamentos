$(function() {
    // Lê os dados, que já estão em json
    var json = function(callback){
        var json = null;
        $.ajax({
            url: "/proposal/proposal/contract_total_per_month_json/",
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                json = data;
                callback(data);
            }
        });
        return json;
    };
    // Gera o gráfico
    var grafico = function(dados) {
        Morris.Area({
            element: 'morris-area-chart-contract-total-per-month',
            data: dados,
            xkey: 'month',
            ykeys: ['total'],
            labels: ['Total'],
            hideHover: 'auto',
            resize: true,
        });
    };
    // Chamando a função para gerar o gráfico
    json(grafico);
    // Caso queira imprimir os dados no console
    json(function(json){
        console.log(json)
    }); 

});