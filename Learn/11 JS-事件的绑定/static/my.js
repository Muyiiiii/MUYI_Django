function addCityInfo() {
    //获取输入的内容
    var txtTag = document.getElementById("txtUser");
    txt = txtTag.value;//这是用来获取输入框中的值
    //innerText只能获取中间文本
    txtTag.value = "";//清空内容

    //创建新的标签
    var newTag = document.createElement("li");
    newTag.innerText = txt;

    //不空就加入
    if (txt.length > 0) {
        //将新的标签加入
        var parentTag = document.getElementById("city");
        parentTag.appendChild(newTag);
    } else {//显示错误提示
        alert("输入不能为空！！！")
    }
}