// ************************ Drag and drop ***************** //

// import React, { useState, useEffect } from 'react';

let dropArea = document.getElementById("drop-area")
var numPosters = 0, data_loaded = 0;

// Prevent default drag behaviors
['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
  dropArea.addEventListener(eventName, preventDefaults, false)   
  document.body.addEventListener(eventName, preventDefaults, false)
})

// Highlight drop area when item is dragged over it
;['dragenter', 'dragover'].forEach(eventName => {
  dropArea.addEventListener(eventName, highlight, false)
})

;['dragleave', 'drop'].forEach(eventName => {
  dropArea.addEventListener(eventName, unhighlight, false)
})



// const movieFavourite = JSON.parse(
//   localStorage.getItem('movie-posters')
// );

// //Save to local storage
// const saveToLocalStorage= (items) =>{
//   localStorage.setItem('movie-posters',
//   JSON.stringify(items));
// }

// Handle dropped files
dropArea.addEventListener('drop', handleDrop, false)

function preventDefaults (e) {
  e.preventDefault()
  e.stopPropagation()
}

function highlight(e) {
  dropArea.classList.add('highlight')
}

function unhighlight(e) {
  dropArea.classList.remove('active')
}

function handleDrop(e) {
  var dt = e.dataTransfer
  var files = dt.files

  handleFiles(files)
}

let uploadProgress = []
let progressBar = document.getElementById('progress-bar')

function initializeProgress(numFiles) {
  progressBar.value = 0
  uploadProgress = []

  for(let i = numFiles; i > 0; i--) {
    uploadProgress.push(0)
  }
}

function updateProgress(fileNumber, percent) {
  uploadProgress[fileNumber] = percent
  let total = uploadProgress.reduce((tot, curr) => tot + curr, 0) / uploadProgress.length
  progressBar.value = total
}

function handleFiles(files) {
  files = [...files]

  initializeProgress(files.length)
  files.forEach(uploadFile)
  files.forEach(previewFile)
}

function previewFile(file) {
  let reader = new FileReader()
  reader.readAsDataURL(file)
  numPosters += 1
  console.log("There are " + numPosters)
  reader.onloadend = function() {
    let container = document.createElement('container')
    console.log("ID is " + container.id)
    let img = document.createElement('img')
    img.src = reader.result

    img.style = "width:182px;height:268px"
    let textbox = document.createElement('text')
    textbox.id = numPosters.toString()
    //var text = document.createTextNode("This just got added");
    container.appendChild(img)
    container.appendChild(textbox)
    
    document.getElementById('gallery').prepend(container)
    
    //document.getElementById('gallery').appendChild(text)
  }
}

function uploadFile(file, i) {
  var url = 'https://nickwood5.pythonanywhere.com/upload2'
  var xhr = new XMLHttpRequest()
  var formData = new FormData()
  xhr.open('POST', url, true)
  xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest')

  // Update progress (can be used to show progress indicator)
  xhr.upload.addEventListener("progress", function(e) {
    updateProgress(i, (e.loaded * 100.0 / e.total) || 100)
  })

  xhr.addEventListener('readystatechange', function(e) {
    if (xhr.readyState == 4 && xhr.status == 200) {
      updateProgress(i, 100) // <- Add this
    }
    else if (xhr.readyState == 4 && xhr.status != 200) {
      // Error. Inform the user
    }
  })

  formData.append('file', file)
  xhr.send(formData)
  xhr.onload = () => {
      let result = JSON.parse(xhr.responseText)
      data_loaded += 1
      console.log(result)
      
      let keys = Object.keys(result)
      if (keys[0] == 'error') {
        var text = document.createTextNode("Unsupported file extension");
      } else {
        predictions = result['predictions']
        var string = ""
      
        for (let i = 0; i < predictions.length; i++) {
            console.log(predictions[i])
            //var text = document.createTextNode(predictions[i] + "\n");
            string += predictions[i] + ", "
            console.log(string)
            //container.appendChild(text)
            string = string.replace("_", "/")
            var text = document.createTextNode(string.slice(0, -2));
        }
      }

      
      var container = document.getElementById(data_loaded.toString())

      container.appendChild(text)
  }
}