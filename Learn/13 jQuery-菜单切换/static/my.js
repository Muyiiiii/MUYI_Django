function clickMe(self) {
    //找到兄弟标签,再移除样式
    //判断有无hide
    var hasHide = $(self).next().hasClass("hide")

    //简单的if
    if (hasHide) {
        $(self).next().removeClass("hide");
    } else {
        $(self).next().addClass("hide");
    }
}