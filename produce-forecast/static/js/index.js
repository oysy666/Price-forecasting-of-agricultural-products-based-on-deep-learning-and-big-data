$(function () {
    echart_1();
    echart_2();
    echart_3();
    echart_4();
    echart_31();
    echart_5();
});

function echart_1() {
    // 基于准备好的dom，初始化echarts实例
    var chart11 = echarts.init(document.getElementById('chart_1'), 'white', {renderer: 'canvas'});

    $(
        function () {
            fetchData111(chart11);
            setInterval(fetchData111, 10000);
        }
    );

    function fetchData111() {
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:5000/pie_zhe",
            dataType: 'json',
            success: function (result) {
                chart11.setOption(result);
            }
        });
    }
}

function echart_2() {
    // 基于准备好的dom，初始化echarts实例
    var chart22 = echarts.init(document.getElementById('chart_2'), 'white', {renderer: 'canvas'});

    $(
        function () {
            fetchData(chart22);
            setInterval(fetchData, 10000);
        }
    );

    function fetchData() {
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:5000/barChart",
            dataType: 'json',
            success: function (result) {
                chart22.setOption(result);
            }
        });
    }
}

function echart_31() {
    // 基于准备好的dom，初始化echarts实例
   var chart3 = echarts.init(document.getElementById('chart_31'), 'white', {renderer: 'canvas'});

    $(
        function () {
            fetchData31(chart3);
            setInterval(fetchData31, 10000);
        }
    );

    function fetchData31() {
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:5000/map_zhejiang",
            dataType: 'json',
            success: function (result) {
                chart3.setOption(result);
            }
        });
    }
}

function echart_3() {
    // 基于准备好的dom，初始化echarts实例
   var chart2 = echarts.init(document.getElementById('chart_line'), 'black', {renderer: 'canvas'});

    $(
        function () {
            fetchData3(chart2);
            setInterval(fetchData3, 15000);
        }
    );

    function fetchData3() {
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:5000/line_zhe",
            dataType: 'json',
            success: function (result) {
                chart2.setOption(result);
            }
        });
    }
}

function echart_4() {
    // 基于准备好的dom，初始化echarts实例
           var chart4 = echarts.init(document.getElementById('chart_4'), 'white', {renderer: 'canvas'});

    $(
        function () {
            fetchData4(chart4);
            setInterval(fetchData4, 5000);
        }
    );

    function fetchData4() {
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:5000/word_zhe",
            dataType: 'json',
            success: function (result) {
                chart4.setOption(result);
            }
        });
    }
}

function echart_5() {
    // 基于准备好的dom，初始化echarts实例
    var chart5 = echarts.init(document.getElementById('chart_5'), 'white', {renderer: 'canvas'});

    $(
        function () {
            fetchData5(chart5);
            setInterval(fetchData5, 10000);
        }
    );

    function fetchData5() {
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:5000/radar_zhe",
            dataType: 'json',
            success: function (result) {
                chart5.setOption(result);
            }
        });
    }
}

