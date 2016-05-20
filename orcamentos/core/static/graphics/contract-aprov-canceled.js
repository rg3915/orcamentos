$(function() {
    // Lê os dados, que já estão em json
    var json = function(callback){
        var json = null;
        $.ajax({
            url: "/proposal/proposal/contract_aprov_canceled_json/",
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
            element: 'morris-donut-chart-contratos-aprov-cancel',
            data: dados,
            xkey: 'uf',
            ykeys: ['quant'],
            labels: ['quant'],
            colors: ['#254DEA', '#DE2121'],
            hideHover: 'auto',
            resize: true,
        });
    };
    // Chamando a função para gerar o gráfico
    json(grafico);
    // Caso queira imprimir os dados no console
    /* json(function(json){
        console.log(json)
    }); */
});