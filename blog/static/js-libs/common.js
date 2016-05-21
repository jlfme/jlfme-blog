/**
 * 根据客户端的时间来输出google-code-prettify代码风格
 * @param daytime
 * @param night
 */
function getCodePrettifyConfig(daytime, night) {
    daytime = daytime || 'cmd';            // 白天默认主题
    night = night || 'sons-of-obsidian';   // 晚上默认主题

    var codeSkin = daytime;
    var hours = new Date().getHours();
    //如果晚上19点到早上7点,就用'sons-of-obsidian'主题
    if (hours>=19 || hours <=7){
        codeSkin = night;
    }
    var jsSrc = "/static/google-code-prettify/loader/run_prettify.js?autoload=true&amp;lang=css&amp;skin=" + codeSkin;
    document.write("<script src=" + jsSrc + " defer='defer'></script>");

    /****
     * src="/static/google-code-prettify/loader/run_prettify.js?autoload=true&amp;skin=cmd&amp;lang=css"
     */
}


/**
 * 发送ajax请求
 * @param url
 * @param data
 */
function ajax_post(url, data) {
    data = data || {'data': 'data'};
    url = url || 'http://10.10.10.4:2222/api/v1/article/1/';
    $.ajax({
        type: "get",
        cache: false,
        data: data,
        url: url,
        dataType: "json",
        success: function (json) {
            // var pub = document.createElement('textarea');
            // pub.value = "dddd";
            var pub = document.getElementById("comment");
            pub.select();
            tag = document.execCommand('Copy');
            alert(tag);
        }
    });

}


/**********************************run********************************/
// 获取文章markdown文件
$(function() {
    $('#share-article').click(function(){
        ajax_post();
    });

});

//获取配置
getCodePrettifyConfig();
