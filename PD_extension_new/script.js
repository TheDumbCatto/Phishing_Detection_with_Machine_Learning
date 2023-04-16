const headers = new Headers();
headers.append('Content-Type', 'application/json');

// create the request body
const requestBody = JSON.stringify({
  'url': 'god damn man',
  'pred': 'pred',
  'proba': 'proba'
});

// send the POST request asynchronously
// async function sendPostRequest() {
//   try {
//     const response = await fetch('http://192.168.120.236:8090/phishing/detect', {
//       method: 'POST',
//       headers: headers,
//       body: requestBody
//     });
    
//     // handle the response
//   } catch (error) {
//     // handle the error
//   }
// }

// function sendPostRequest() {
//     try {
//       const response = fetch('http://192.168.120.236:8090/phishing/detect', {
//         method: 'POST',
//         headers: headers,
//         body: requestBody
//       });
      
//       // handle the response
//     } catch (error) {
//       // handle the error
//     }
//   }

function sendPostRequest() 
{
    fetch('http://192.168.120.236:8090/phishing/detect?url=yo', {
    method: 'GET',
    // body: requestBody,
    headers: {
      'Content-Type': 'application/json'
    }
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}  

function myFun() {
    document.getElementById('helloWorld').innerHTML = "Sup";
}
document.addEventListener('DOMContentLoaded', function() {
    //document.getElementById('submitButton').addEventListener("click", sendPostRequest);
    document.getElementById('submitButton').addEventListener("click", function(e){
        e.preventDefault();
    
        const req = new XMLHttpRequest();
        const baseUrl = "http://192.168.120.236:8090/phishing/detection";
        //const urlParams = `email=${email}&password=${pwd}`;
    
        req.open("POST", baseUrl, true);
        req.setRequestHeader("Content-type", "application/json")
        req.setRequestHeader("Origin", "*");
        req.send(requestBody);
    
        req.onreadystatechange = function() { // Call a function when the state changes.
            if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
                console.log("Got response 200!");
            }
        }
    });
});
