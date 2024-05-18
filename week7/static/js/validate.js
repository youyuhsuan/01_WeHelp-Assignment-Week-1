// checkbox
const agreeTerms = document.getElementById("agree_terms");
const SigninBtn = document.getElementById("signin_btn");

SigninBtn.addEventListener("click", validateCheckbox);

function validateCheckbox(event) {
  if (!agreeTerms.checked) {
    event.preventDefault();
    alert("Please check the checkbox first");
  }
}

// signinForm
const signinForm = document.getElementById("signin_form");
signinForm.addEventListener("submit", function (event) {
  let username = document.getElementById("signin_username").value.trim();
  let password = document.getElementById("signin_password").value.trim();
  if (username === "" || password === "") {
    event.preventDefault();
    alert("Username or password cannot be empty");
  }
});

// signupForm
const signupForm = document.getElementById("signup_form");
signupForm.addEventListener("submit", function (event) {
  let name = document.getElementById("name").value.trim();
  let username = document.getElementById("username").value.trim();
  let password = document.getElementById("password").value.trim();

  if (name === "" || username === "" || password === "") {
    event.preventDefault();
    alert("Name, Username or password cannot be empty");
  }
});

// squareForm
const squareForm = document.getElementById("square_form");
squareForm.addEventListener("submit", function (event) {
  let number = document.getElementById("number").value.trim();
  if (number === "") {
    alert("Number cannot be empty");
    event.preventDefault(); // Prevent the form's default behavior
  } else if (number < 0) {
    alert("Please enter a positive integer");
    event.preventDefault(); // Prevent the form's default behavior
  } else {
    let url = `/square/${number}`;
    window.location.href = url;
    event.preventDefault(); // Prevent the form's default behavior
  }
});

const createMessageForm = document.getElementById("create_message_form");
createMessageForm.addEventListener("submit", function (event) {
  let content = document.getElementById("content").value.trim();
  if (content === "") {
    event.preventDefault();
    alert("content cannot be empty");
    // Prevent the form's default behavior
  }
});
