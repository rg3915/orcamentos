$(function() {
    // Lê os dados, que já estão em json
    var json = function(callback){
        var json = null;
        $.ajax({
            url: "/proposal/proposal/percent_type_customer_json/",
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
        Morris.Donut({
            element: 'morris-donut-chart-percent-type-customer',
            data: dados,
            xkey: 'label',
            ykeys: ['value'],
            labels: ['value'],
            colors: ['#44AD41', '#009BDE', '#FFB819'],
            formatter: function (x) { return x + "%"},
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