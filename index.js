

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


// ............3/.////

  // const answerQuestions = document.querySelectorAll(".answer-question .metadata");
  // const dropDown = document.querySelector(".meta-answer")
  
  //   answerQuestions.forEach((dropUp, i) => {
  //     dropUp.addEventListener("click",()=>{
  //         dropDown.classList.toggle("f-active")
  //         const imageUpArrow = document.querySelector(".metadata img")
          
  //         if(dropDown.classList.contains("f-active")){
  //           imageUpArrow.setAttribute("src","./images/down-circle.png")
  //         }
  //         else{
  //           imageUpArrow.setAttribute("src","./images/up-circle-1.png")
  //         }
  //       })
  //   })  












// ........2......
// const answerQuestions = document.querySelectorAll(".answer-question .metadata");
// const dropDown = document.querySelectorAll(".meta-answer")

//   answerQuestions.forEach((dropUp, i) => {
//     dropUp.addEventListener("click",()=>{
//         dropDown.classList.toggle("f-active");
        
 
        
        
//         const imageUpArrow = document.querySelector(".metadata img")
        
//         if(dropDown.classList.contains("f-active")){
//           imageUpArrow.setAttribute("src","./images/down-circle.png")
//         }
//         else{
//           imageUpArrow.setAttribute("src","./images/up-circle-1.png")
//         }
//       })
//   })






  // const answerQuestions = document.querySelectorAll(".answer-question .metadata");
  // const dropDown = document.querySelector(".meta-answer")
  
  //   answerQuestions.forEach((dropUp, i) => {
  //     dropUp.addEventListener("click",()=>{
  //         dropDown.classList.toggle("f-active")
  //         const imageUpArrow = document.querySelector(".metadata img")
          
  //         if(dropDown.classList.contains("f-active")){
  //           imageUpArrow.setAttribute("src","./images/down-circle.png")
  //         }
  //         else{
  //           imageUpArrow.setAttribute("src","./images/up-circle-1.png")
  //         }
  //       })
  //   })  
    
// ..........#######

  // const answer = document.querySelector(".meta-answer")

  // const answerMenu = document.querySelector(".meta-answer")



//   const menuBtn = document.querySelector(".metadata img")

//   const menuContainer = document.querySelector(".menu-expand-container")

//   const closeMenuBtn = document.querySelector(".content-menu > img")

//   menuBtn.addEventListener("click",()=>{
//     menuContainer.style.display = "flex"
//  })
