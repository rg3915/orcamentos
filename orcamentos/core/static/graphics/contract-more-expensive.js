$(function() {
    // Lê os dados, que já estão em json
    var json = function(callback){
        var json = null;
        $.ajax({
            url: "/proposal/proposal/contract_more_expensive_json/",
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
        Morris.Bar({
            element: 'morris-bar-chart',
            data: dados,
            xkey: 'proposal__work__name_work',
            ykeys: ['proposal__price'],
            labels: ['Preço'],
            hideHover: 'auto',
            resize: true,
            gridTextSize: 9,
        });
    };
    // Chamando a função para gerar o gráfico
    json(grafico);
    // Caso queira imprimir os dados no console
    json(function(json){
        console.log(json)
    }); 

});