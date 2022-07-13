let low = 0;
let high = 255;
let start = high;
let colorArr = [245, 229, 252];
let colorStr = ["F5", "E5", "FC"];
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

setInterval(changeColor, 1000);

window.onscroll = function(){
  changeColor();
};