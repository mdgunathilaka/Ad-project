const content = document.querySelector('div')
const Mcount = document.getElementById('Mcount');
const Fcount = document.getElementById('Fcount');
const F18_38 = document.getElementById('18-38F');
const F39_59 = document.getElementById('39-59F');
const F60_80 = document.getElementById('60-80F');
const M18_38 = document.getElementById('18-38M');
const M39_59 = document.getElementById('39-59M');
const M60_80 = document.getElementById('60-80M');
const Daytime = document.getElementById('Daytime');
const Season = document.getElementById('Season');
const Day = document.getElementById('Day');

setInterval(changer, 5000);

function changer(){
    console.log("at changer");
    $.get("http://127.0.0.1:5000/predict", function(response){
        console.log(response);
        Mcount.innerText = response.male;
        Fcount.innerText = response.female;
        F18_38.innerText = response.F18_38;
        F39_59.innerText = response.F39_59;
        F60_80.innerText = response.F60_80;
        M18_38.innerText = response.M18_38;
        M39_59.innerText = response.M39_59;
        M60_80.innerText = response.M60_80;
        Daytime.innerText = response.Daytime;
        Season.innerText = response.Season;
        Day.innerText = response.Day;
        const imgnum = response.Label;
        content.innerHTML = `<img src=${imgnum}.jpg>`;
    });
};