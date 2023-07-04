function getInfo() {
    //获取input的值
    var username = $("#txtUser").val();
    var email = $("#txtEmail").val();

    //拼接字符串
    var dataString = username + " - " + email;

    //创建li标签
    var newLi = $("<li>").text(dataString);

    $("#view").append(newLi);
}