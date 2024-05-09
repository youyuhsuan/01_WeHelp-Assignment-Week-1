const squareForm = document.getElementById("square_form");
squareForm.addEventListener("submit", function (event) {
  let number = document.getElementById("number").value;
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
