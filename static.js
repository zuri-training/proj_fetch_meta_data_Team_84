
/*This section gets title from the body of the page and 
compares with the array of page titles and highlights 
the current page in the nav bar */
var bodyTitle = document.querySelector('body')
var bodyTitleAttr = bodyTitle.getAttribute('title')
var navLinks = document.querySelectorAll('.nav-link')
var linkName = [], linkLen = navLinks.length;

for (let i =0; i < linkLen; i++){
    linkName.push(navLinks[i].getAttribute('title').toLowerCase())
    console.log(linkName)
}
var linkToHighlight = linkName.indexOf(bodyTitleAttr)
function myHighLight(){
    //this checks if the name exists in the array, because if you use index of where the item doesn't exist, it returns -1
    if(linkToHighlight !== -1){
        navLinks[linkToHighlight].style.color = 'var(--secondary-brown-hover)'
    }
    
}
window.onload = myHighLight()
const faqHeaders = document.querySelectorAll(".answer-question .metadata");

console.log(document.querySelectorAll(".answer-question .metadata"));
faqHeaders.forEach((header, i) => {
  header.addEventListener("click", () => {
    header.nextElementSibling.classList.toggle("f-active");
    console.log(header.nextElementSibling);
    
    const open = header.querySelector(".open");
    const close = header.querySelector(".close");

    if (header.nextElementSibling.classList.contains("f-active")) {
      open.classList.remove("f-active");
      close.classList.add("f-active");
    } else {
      open.classList.add("f-active");
      close.classList.remove("f-active");
    }
  });
});


/* This section creates the logic for changing slides on the landing page hero section*/
var hamburger = document.getElementById('hamburger')
var menu = document.getElementById('navMenu')
var navBtn = document.getElementById('navBtn')
var profile = document.getElementById('profile')

hamburger.addEventListener('click', ()=>{
    if (navBtn.classList.contains('active')){
        profile.click()
        }
 
    hamburger.classList.toggle('click-small')
    menu.classList.toggle('active-small')
  
})

profile.addEventListener('click', ()=>{
    if (menu.classList.contains('active-small')){
        hamburger.click()
    }
    navBtn.classList.toggle('active')

})

var x = document.getElementsByClassName('index-hero-main')
var dot = document.getElementsByClassName('circle')


var index = 1;
myShows(index)

function myCurrent(n){
   myShows(index = n)
}

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

/*VIDEO*/

var vid = document.getElementById('vidHero')
var vidPop = document.querySelector('#videoPop')
var overLay = document.getElementById('vidWrap')
var closeVid = document.getElementById('close')
var indexHero = document.getElementById('indexHeader')
var indexMain = document.getElementById('indexMain')
var vidDuration = vid.duration;

/*if user clicks on video thumbnail, video appears in pop up
 and background gets blurred to account for slideshow in the background and not to interrupt slide timing*/
vid.onclick = ()=>{
    vidPop.play()
    overLay.style.display = 'flex';
    indexHero.classList.add('blur')
    indexMain.style.display = 'none'
    indexMain.nextElementSibling.style.display = 'none'
}

closeVid.onclick = ()=> {
    vidPop.pause()
    overLay.style.display = 'none';
    indexHero.classList.remove('blur')
    indexMain.style.display = 'block'
    indexMain.nextElementSibling.style.display = 'flex'
    
}

/*VIDEO END*/

var slideInterval = setInterval( 
    function myTimer(){
        index++
        myShows(index)
    },10000)


window.onscroll = () => {
    if (overLay.style.display == 'flex'){
        vidPop.pause()
    }
}

/*This section creates the collapsible menu controls*/


/*This section is for the review section on landing page */
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
        reviewImage[i].style.width = ''
    }
    reviewImage[indexTwo-1].style.width = '50%'
}







