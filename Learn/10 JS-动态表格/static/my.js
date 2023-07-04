var dataList = [
    { id: 1, name: "ha", age: 19 },
    { id: 2, name: "haha", age: 19 },
    { id: 3, name: "hahaha", age: 19 },
    { id: 4, name: "hahahaha", age: 19 },
];

for (var idx in dataList) {
    var info = dataList[idx];

    var tr = document.createElement("tr");
    for (var key in info) {
        var text = info[key];

        td = document.createElement('td');
        td.innerText = text;

        tr.appendChild(td);
    }

    var body = document.getElementById("body");
    body.appendChild(tr);
}
