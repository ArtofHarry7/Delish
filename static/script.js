// let menu = document.querySelector('#menu-bar');
// let navbar = document.querySelector('.navbar');

// menu.onclick = () =>{

//   menu.classList.toggle('fa-times');
//   navbar.classList.toggle('active');

// }

// window.onscroll = () =>{

//   menu.classList.remove('fa-times');
//   navbar.classList.remove('active');

//   if(window.scrollY > 60){
//     document.querySelector('#scroll-top').classList.add('active');
//   }else{
//     document.querySelector('#scroll-top').classList.remove('active');
//   }

// }

// function loader(){
//   document.querySelector('.loader-container').classList.add('fade-out');
// }

// function fadeOut(){
//   setInterval(loader, 3000);
// }

// window.onload = fadeOut();

// let colors = "red";

// colors = ["red", "green", "pink", "blue", "yellow", "cyan", "purple"];

// colors = ["#E27D60", "#85DCB0", "#E8A87C", "#C38D9E", "#41B3A3", "#7b3e19", "#b28b84", "#F5E5FC", "#8ae1fc", "#48b8d0"];
// colors = ["#d4bfa0", "#c3a592", "#b28b84", "#d4b8c0", "#e5cfde", "#f5e5fc", "#DBE4FC", "#C0E3FC", "#8AE1FC", "#A0C8D6"]
// colors = [
//   "#EA6B6B",
//   "#DF7E69",
//   "#E09677",
//   "#FAB769",
//   "#FAB769",
//   "#D6F08A",
//   "#B7F08A",
//   "#8CF08A",
//   "#8AF0B9",
//   "#8AEAF0",
//   "#8ACBF0",
//   "#8AADF0",
//   "#8A94F0",
//   "#988AF0",
//   "#C38AF0",
//   "#E88AF0",
//   "#F08ACD",
//   "#F08A9C",
// ]
let low = 0;
let high = 255;
let start = high;
let colorArr = [start, start, start];
let colorStr = ["FF", "FF", "FF"];
for(let i = 0; i < 3; i++)
  colorStr[i] = parseInt(colorArr[i], 10).toString(16);
let colorUp = [false, false, false];
let ind = Math.floor(Math.random()*3);

function changeColor(){
  if(colorUp[ind]){
    colorArr[ind]++;
    colorStr[ind] = parseInt(colorArr[ind], 10).toString(16);
    color = "#" + colorStr.join('');
    if(colorArr[ind] == high)
      colorUp[ind] = false;
  }
  else{
    colorArr[ind]--;
    colorStr[ind] = parseInt(colorArr[ind], 10).toString(16);
    color = "#" + colorStr.join('');
    if(colorArr[ind] == low || colorArr[0]+colorArr[1]+colorArr[2] <= 500)
      colorUp[ind] = true;
  }
  ind = Math.floor(Math.random()*3);
  document.body.style.backgroundColor = color;
}

setInterval(changeColor, 1);