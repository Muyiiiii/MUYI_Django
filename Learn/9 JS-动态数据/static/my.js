var cityList = ["北京", "上海", "深圳"];

for (var idx in cityList) {
    var text = cityList[idx];

    //将文本和li结合
    //创建了li标签
    var tag = document.createElement("li");
    tag.innerText = text;

    //添加到ul里
    var parentTag = document.getElementById("city");
    parentTag.appendChild(tag);
}