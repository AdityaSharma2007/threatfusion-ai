async function analyzeEmail(){

const text =
document.getElementById("emailtext").value

document.getElementById("loading").style.display="block"

const response = await fetch("/predict",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
text:text
})

})

const data = await response.json()

document.getElementById("loading").style.display="none"

document.getElementById("resultBox").style.display="block"

document.getElementById("prediction")
.innerText="Prediction: "+data.prediction

document.getElementById("probability")
.innerText="Probability: "+data.probability

document.getElementById("score")
.innerText="Threat Score: "+data.threat_score+"/100"

document.getElementById("level")
.innerText="Threat Level: "+data.threat_level


let percent=data.threat_score

const meter=document.getElementById("meterFill")

meter.style.width=percent+"%"


const box=document.getElementById("resultBox")

if(data.prediction.includes("SAFE")){

box.className="safe"

}

else{

box.className="threat"

}



let words=""

if(data.prediction.includes("THREAT") && data.suspicious_words.length>0){

words="<h3>Suspicious Words</h3><ul>"

data.suspicious_words.forEach(w=>{
words+="<li>"+w+"</li>"
})

words+="</ul>"

}

document.getElementById("suspicious").innerHTML=words


let links=""

if(data.urls.length>0){

links="<h3>Detected Links</h3><ul>"

data.urls.forEach(l=>{
links+="<li>"+l+"</li>"
})

links+="</ul>"

}

document.getElementById("urls").innerHTML=links


let exp=""

if(data.prediction.includes("THREAT")){

exp="<h3>Threat Analysis</h3><ul>"

data.explanation.forEach(e=>{
exp+="<li>"+e+"</li>"
})

exp+="</ul>"

}

document.getElementById("explanation").innerHTML=exp

}