// function userAction() {
//     const requestBody = JSON.stringify({
//         url: 'god damn man',
//         pred: 'pred',
//         proba: 'proba'
//     });
//     const url=document.getElementById('in_url');
//     const response = fetch('http://192.168.120.236:8090/phishing/detect', {
//     method: 'POST',
//     headers: {
//         'accept': 'application/json',
//         'content-type': 'application/json'
//     },
//     body: requestBody
//     });
//     const myJson = response.json(); //extract JSON from the http response
//     console.log(myJson)
// }
// console.log('It worked');
// btn = document.getElementById("submitButton");
// if (btn) {
//     btn.addEventListener("click", userAction, false);
// }
function myFunc(){   
    document.getElementById("helloWorld").innerHTML = "It worked dawg";
    console.log('It worked');
}

window.onload=function(){
    var btn = document.getElementById("submitButton");
    btn.addEventListener("click", userAction, true);
}