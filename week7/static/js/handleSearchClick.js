async function handleSearchClick(event) {
  event.preventDefault();
  const username = document.getElementById("username").value.trim();
  if (username === "") {
    alert("username cannot be empty");
  } else {
    try {
      const content = await queryMember(username);
      displayMemberInfo(content);
    } catch (error) {
      console.error("Error handling search click:", error);
      alert("Error retrieving member info");
    }
  }
}

document
  .getElementById("search_form")
  .addEventListener("submit", handleSearchClick);

async function handleUpdateClick(event) {
  event.preventDefault();
  const name = document.getElementById("name").value.trim();
  if (name === "") {
    alert("name cannot be empty");
  } else {
    try {
      const content = await updatingName(name);
      if (content.ok === True) {
        displayUpdateStatus("Updated successfully", true);
        displayUpdateName(name);
      } else {
        displayUpdateStatus("Failed to update", false);
      }
    } catch (error) {
      console.error("Error handling update click:", error);
      alert("Error retrieving update info");
    }
  }
}

document
  .getElementById("update_form")
  .addEventListener("submit", handleUpdateClick);
