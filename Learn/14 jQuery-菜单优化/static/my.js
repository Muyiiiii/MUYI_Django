function clickMe(self) {
    //让第一个自动展示
    $(self).next().removeClass("hide");

    //找找父亲，再找所有的兄弟，再在子孙中添加hide
    $(self).parent().siblings().find(".content").addClass("hide");
}