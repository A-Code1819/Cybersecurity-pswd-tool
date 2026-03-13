let terminal = document.getElementById("terminal")

let input = document.getElementById("command")

function print(text){

terminal.innerHTML += "<div>> "+text+"</div>"

terminal.scrollTop = terminal.scrollHeight

}

input.addEventListener("keydown", function(e){

if(e.key === "Enter"){

let cmd = input.value

print(cmd)

processCommand(cmd)

input.value=""

}

})


function processCommand(cmd){

if(cmd.startsWith("entropy")){

let pass = cmd.split(" ")[1]

fetch("http://localhost:5000/entropy",{

method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({password:pass})

})

.then(res=>res.json())
.then(data=>{

print("Entropy: "+data.entropy)

})

}

else if(cmd.startsWith("hash")){

let pass = cmd.split(" ")[1]

fetch("http://localhost:5000/hash",{

method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({password:pass})

})

.then(res=>res.json())
.then(data=>{

print("SHA256: "+data.hash)

})

}

else if(cmd.startsWith("pwned")){

let pass = cmd.split(" ")[1]

fetch("http://localhost:5000/pwned",{

method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({password:pass})

})

.then(res=>res.json())
.then(data=>{

if(data.breached)

print("BREACHED "+data.count+" times")

else

print("No breach found")

})

}

else{

print("Unknown command")

}

}