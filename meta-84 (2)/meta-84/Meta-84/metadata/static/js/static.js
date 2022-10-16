
var x = document.getElementsByClassName('index-hero-main')
var dot = document.getElementsByClassName('circle')
var vid = document.querySelector('video')
/*var timeOut = 5000;

if(!(vid.ended) || !(vid.paused)){
    timeOut = vid.duration
    timeOut = parseInt(timeOut * 1000)
    console.log (vid.currentTime)
} */


var index = 1;
myShows(index)

function myCurrent(n){
   myShows(index = n)
}
setInterval( 
    function myTimer(){
        index++
        myShows(index)
    },5000)
function myShows(){
   if (index > (x.length)) {index = 1}
   if (index < 1) {index = x.length}
   for(let i = 0; i < x.length; i++)
   {
    x[i].style.display = 'none'
   }
   x[index-1].style.display = 'flex';
   for(let i = 0; i < dot.length; i++)
   {
      dot[i].style.backgroundColor = ''
   }
   dot[index-1].style.backgroundColor = 'var(--primary-blue-active-focus)'
   
}
var urlsSplit = (window.location.href).split('/')
var urlName = urlsSplit[urlsSplit.length - 1].split('.')[0]
var navLinks = document.querySelectorAll('.nav-link')
var linkName = [], linkLen = navLinks.length;

for (let i =0; i < linkLen; i++){
    linkName.push(navLinks[i].getAttribute('title').toLowerCase())
    console.log(linkName)
}

var linkToHighlight = linkName.indexOf(urlName)
function myHighLight(){
    //this checks if the name exists in the array, because if you use index of where the item doesn't exist, it returns -1
    if(linkToHighlight !== -1){
        navLinks[linkToHighlight].style.color = 'var(--secondary-brown-hover)'
    }
    
}

window.onload = myHighLight()
var reviews = document.getElementsByClassName('review')
var reviewImage = document.getElementsByClassName('review-image')
var reviewImageLen = reviewImage.length
var reviewLen = reviews.length, hh=[];

var indexTwo = 2;
myReview(indexTwo)
function myPresentDiv(n){
    myReview(indexTwo = n)
}

function myReview(){
    for (let i = 0; i < reviewLen; i++){
        reviews[i].style.opacity = ''
    }
    reviews[indexTwo-1].style.opacity = '1'
    for (let i = 0; i < reviewImageLen; i++){
        reviewImage[i].style.height = ''
        reviewImage[i].style.width = ''
    }
    reviewImage[indexTwo-1].style.height = '50%'
    reviewImage[indexTwo-1].style.width = '50%'
}









