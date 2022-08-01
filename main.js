document.querySelectorAll(".drop-zone__input").forEach((inputElement) => {
    const dropZoneElement = inputElement.closest(".drop-zone");
  
    dropZoneElement.addEventListener("click", (e) => {
      inputElement.click();
    });
  
    inputElement.addEventListener("change", (e) => {
      if (inputElement.files.length) {
        updateThumbnail(dropZoneElement, inputElement.files[0]);
      }
    });
  
    dropZoneElement.addEventListener("dragover", (e) => {
      e.preventDefault();
      dropZoneElement.classList.add("drop-zone--over");
    });
  
    ["dragleave", "dragend"].forEach((type) => {
      dropZoneElement.addEventListener(type, (e) => {
        dropZoneElement.classList.remove("drop-zone--over");
      });
    });
  
    dropZoneElement.addEventListener("drop", (e) => {
      e.preventDefault();
  
      if (e.dataTransfer.files.length) {
        inputElement.files = e.dataTransfer.files;
        updateThumbnail(dropZoneElement, e.dataTransfer.files[0]);
      }
  
      dropZoneElement.classList.remove("drop-zone--over");
    });
  });
  
  /**
   * Updates the thumbnail on a drop zone element.
   *
   * @param {HTMLElement} dropZoneElement
   * @param {File} file
   */
  function updateThumbnail(dropZoneElement, file) {
    let thumbnailElement = dropZoneElement.querySelector(".drop-zone__thumb");
  
    // First time - remove the prompt
    // if (dropZoneElement.querySelector(".drop-zone__prompt")) {
    //   dropZoneElement.querySelector(".drop-zone__prompt").remove();
    // }
    if (dropZoneElement.querySelector(".top")) {
        dropZoneElement.querySelector(".top").remove();
    }
    if (dropZoneElement.querySelector(".middle")) {
        dropZoneElement.querySelector(".middle").remove();
    }
      if (dropZoneElement.querySelector(".bottom")) {
        dropZoneElement.querySelector(".bottom").remove();
    }
  
    // First time - there is no thumbnail element, so lets create it
    if (!thumbnailElement) {
      thumbnailElement = document.createElement("div");
      thumbnailElement.classList.add("drop-zone__thumb");
      dropZoneElement.appendChild(thumbnailElement);
    }
  
    thumbnailElement.dataset.label = file.name;
  
    // Show thumbnail for image files
    if (file.type.startsWith("image/")) {
      const reader = new FileReader();
  
      reader.readAsDataURL(file);
      reader.onload = () => {
        thumbnailElement.style.backgroundImage = `url('${reader.result}')`;
      };
    } else {
      thumbnailElement.style.backgroundImage = null;
    }
  }




// display date and time 
// let text = new Date()
let text = document.lastModified
document.getElementById('datePicker').innerHTML = text;
// document.getElementById('datePicker').value = new Date().toDateInputValue();



// button share function

// function openForm() {
//   document.getElementById("myForm").style.display = "block";
// }

// function closeForm() {
//   document.getElementById("myForm").style.display = "none";
// }









// When the user clicks on div, open the popup
// function myFunction() {
  // var openButton = document.getElementById("myPopup").style.display = "block";
  // var popup = document.getElementById("myPopup");
  // openButton.classList.toggle("show");
// }
// click outside to close form 



// function pop() { window.open('http://www.example.com','pop',"height=590,width=450,toolbar=no,location=no,directories=no,status=no,menubar=no,scrollbars=auto,resizable=yes,copyhistory=no"); }






