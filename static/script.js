document.addEventListener("DOMContentLoaded",()=>{

const fileInput=
document.getElementById("xray-file");

const btn=
document.getElementById("diagnose-btn");

const preview=
document.getElementById("image-preview");

const result=
document.getElementById("result-text");

let selectedFile=null;


fileInput.addEventListener(
"change",
(e)=>{

selectedFile=
e.target.files[0];

if(selectedFile){

preview.src=
URL.createObjectURL(
selectedFile
);

}

}
);


btn.addEventListener(
"click",

async()=>{

if(!selectedFile){

alert(
"Upload Image First"
);

return;

}

const formData=
new FormData();

formData.append(
"file",
selectedFile
);

result.innerText=
"Analyzing...";

try{

const response=
await fetch(
"/predict",
{
method:"POST",
body:formData
}
);

const data=
await response.json();

result.innerText=
data.prediction;

}

catch{

result.innerText=
"Prediction Failed";

}

}

);

});