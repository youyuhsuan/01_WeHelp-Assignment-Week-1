// signinForm
const signinForm = document.getElementById("signin_form");
signinForm.addEventListener("submit", function (event) {
  let username = document.getElementById("signin_username").value;
  let password = document.getElementById("signin_password").value;
  if (username === "" || password === "") {
    event.preventDefault();
    alert("Username or password cannot be empty");
  }
});

// signupForm
const signupForm = document.getElementById("signup_form");
signupForm.addEventListener("submit", function (event) {
  let name = document.getElementById("name").value;
  let username = document.getElementById("username").value;
  let password = document.getElementById("password").value;

  if (name === "" || username === "" || password === "") {
    event.preventDefault();
    alert("Name, Username or password cannot be empty");
  }
});
