// Suppose the 'id' attribute of element is `message_container`.
var message_ele = document.getElementById("message_js");

if (typeof message_ele !== "undefined" && message_ele.value == '') {
    setTimeout(function () {
        message_ele.style.display = "none";
    }, 3000);
    // Timeout is 3 sec, you can change it
}

