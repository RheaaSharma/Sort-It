// console.log(window.location)
$(document).ready( function(){



var loc = window.location
var formData = $("#contactForm")
var msgInput = $("#file")

var buttonText = document.getElementById("myBtn")
console.log(buttonText);

var wsStart = 'ws://'
if (loc.protocol == 'https:'){
  wsStart = 'wss://'
}

var endpoint = wsStart + loc.host + loc.pathname
var socket = new WebSocket(endpoint)



socket.onmessage = function(e){
  console.log("message", e)

  if (status != "end")   {
      resultItems.append(
          "<li><div class='one'><h3>" +
          owner +
          "</h3><p>" +
          application_no +
          "</p><p>" +
          expiry_date +
          "</p></div><div class='"+ check_class +"'><img class='check-img' src=\"/static/chat/check.svg\" alt='check'></div></li><hr>")

  }

}



socket.onopen = function(e){
  console.log("open", e)


  formData.submit(function(event){
    event.preventDefault();
    var msgText = msgInput.val()
    var finalData = {
      'message': msgText
    }
    console.log(msgText)
    socket.send(JSON.stringify(finalData))
    window.location.replace("results/");


  })
}
socket.onerror = function(e){
  console.log("error", e)
}
socket.onclose = function(e){
  console.log("close", e)
}


})
