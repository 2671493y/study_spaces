function showInput(fieldName) {
    var input = document.getElementById(fieldName);
    
    if (!input) {
      var label = document.querySelector('label[for="' + fieldName + '"]');
      input = document.createElement('input');
      input.type = fieldName === 'password' ? 'password' : 'text';
      input.name = fieldName;
      input.id = fieldName;
      input.className = 'form-control mt-2';
      input.autocomplete = 'off';
      input.oninput = enableSubmitButton;
      
      if (fieldName === 'user_profile') {
        input.type = 'file';
        input.accept = 'image/*';
      }
      
      label.parentNode.insertBefore(input, label.nextSibling);
    } else {
      if (input.style.display === "none") {
        input.style.display = "block";
      } else {
        input.style.display = "none";
      }
    }
  }

  function enableSubmitButton() {
    document.getElementById("submit-button").disabled = false;
  }