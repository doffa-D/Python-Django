function displayFormContent() {
  // Get form values
  var firstName = document.getElementById("first_name").value;
  var lastName = document.getElementById("last_name").value;
  var age = document.getElementById("age").value;
  var email = document.getElementById("email").value;
  var phone = document.getElementById("Phone").value;
  var student = document.getElementById("Student").checked ? "Yes" : "No";
  var gender = document.querySelector('input[name="gender"]:checked').value;

  // Update popup content
  var popupText =
    "First Name: " +
    firstName +
    "<br>" +
    "Last Name: " +
    lastName +
    "<br>" +
    "Age: " +
    age +
    "<br>" +
    "Email: " +
    email +
    "<br>" +
    "Phone: " +
    phone +
    "<br>" +
    "Student at 42?: " +
    student +
    "<br>" +
    "Gender: " +
    gender;

  // Update the popup content
  document.getElementById("popup-text").innerHTML = popupText;

  // Display the popup
  document.getElementById("popup").style.display = "block";
}

function closePopup() {
  // Close the popup
  document.getElementById("popup").style.display = "none";
}
