// DRAG AND DROP ZONE
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
    if (dropZoneElement.querySelector(".top")) {
        dropZoneElement.querySelector(".top").remove();
    }
    if (dropZoneElement.querySelector(".middle")) {
        dropZoneElement.querySelector(".middle").remove();
    }
      if (dropZoneElement.querySelector(".bottom")) {
        dropZoneElement.querySelector(".bottom").remove();
    }
  
    // First time - create thumbnail element
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
        document.getElementById("save").style.display = "block";
      };
    } else {
      thumbnailElement.style.backgroundImage = null;
      document.getElementById("save").style.display = "block";
    }
  }


// LIGHT/DARK MODE 
function toggle_light_mode() {
    var app = document.getElementsByTagName("BODY")[0];
    // var app = document.getElementsById("overlay")[0];
    if (localStorage.lightMode == "dark") {
        localStorage.lightMode = "light";
        app.setAttribute("light-mode", "light");
    } else {
        localStorage.lightMode = "dark";
        app.setAttribute("light-mode", "dark");
    }

    var app = document.getElementsByTagName("BODY")[0];
    // var app = document.getElementsById("overlay")[0];
    if (localStorage.lightMode == "dark") {
        app.setAttribute("light-mode", "dark");
    }
}

window.addEventListener(
    "storage",
    function () {
        if (localStorage.lightMode == "dark") {
            app.setAttribute("light-mode", "dark");
        } else {
            app.setAttribute("light-mode", "light");
        }
    },
    false
);


// SLIDING/COLLAPSIBLE SIDEBAR 

{
  let sideBar = document.querySelector('.side-bar');
  let arrowCollapse = document.querySelector('#logo-name__icon');
  sideBar.onclick = () => {
    sideBar.classList.toggle('collapse');
    arrowCollapse.classList.toggle('collapse');
    if (arrowCollapse.classList.contains('collapse')) {
      arrowCollapse.classList =
        'fa-solid fa-angle-left logo-name__icon collapse';
        // 'bx bx-arrow-from-left logo-name__icon collapse';
    } else {
      arrowCollapse.classList = 'fa-solid fa-angle-right logo-name__icon';
      // arrowCollapse.classList = 'bx bx-arrow-from-right logo-name__icon';
    }
  };
}

