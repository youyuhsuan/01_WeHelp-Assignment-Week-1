const agreeTerms = document.getElementById("agree_terms");
const SigninBtn = document.getElementById("signin_btn");

SigninBtn.addEventListener("click", validateCheckbox);

function validateCheckbox(event) {
  if (!agreeTerms.checked) {
    event.preventDefault();
    alert("Please check the checkbox first");
  }
}
