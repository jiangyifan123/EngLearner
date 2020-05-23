(function (para) {
    var p = para.sdk_url, n = para.name, w = window, d = document, s = 'script', x = null, y = null;
    if (typeof (w['sensorsDataAnalytic201505']) !== 'undefined') {
        return false;
    }
    w['sensorsDataAnalytic201505'] = n;
    w[n] = w[n] || function (a) { return function () { (w[n]._q = w[n]._q || []).push([a, arguments]); } };
    var ifs = ['track', 'quick', 'register', 'registerPage', 'registerOnce', 'trackSignup', 'trackAbtest', 'setProfile', 'setOnceProfile', 'appendProfile', 'incrementProfile', 'deleteProfile', 'unsetProfile', 'identify', 'login', 'logout', 'trackLink', 'clearAllRegister', 'getAppStatus'];
    for (var i = 0; i < ifs.length; i++) {
        w[n][ifs[i]] = w[n].call(null, ifs[i]);
    }
    if (!w[n]._t) {
        x = d.createElement(s), y = d.getElementsByTagName(s)[0];
        x.async = 1;
        x.src = p;
        x.setAttribute('charset', 'UTF-8');
        w[n].para = para;
        y.parentNode.insertBefore(x, y);
    }
})({
    sdk_url: '//code.kmf.com/dist/libs/sensors@1.14.5/sensorsdata.min.js',
    heatmap_url: '//code.kmf.com/dist/libs/sensors@1.14.5/heatmap.min.js',
    name: 'kmfSensors',
    server_url: 'https://sensorsdata.talbrain.com:8080/sa?project=Glo_KMF',
    show_log: false,
    batch_send:{
        datasend_timeout: 5000,  //一次请求超过多少秒的话自动取消，防止请求无响应。
        send_interval: 2000,    //间隔几秒发一次数据。
        one_send_max_length: 6  //一次请求最大发送几条数据，防止数据太大
    },
});

if (window.kmfSensorsConf.passport_id != '0'){
    kmfSensors.login(window.kmfSensorsConf.passport_id);
}
kmfSensors.quick('autoTrack', window.kmfSensorsConf.params);