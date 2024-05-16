let deleteBtns = document.querySelectorAll(".delete_btn");
deleteBtns.forEach((deleteBtn) => {
  deleteBtn.addEventListener("click", async () => {
    let messageId = deleteBtn.getAttribute("data-message-id");
    let confirmed = window.confirm("Do you really want to delete message?");
    if (confirmed) {
      try {
        const response = await fetch(`/deleteMessage/${messageId}`, {
          method: "DELETE",
        });
        if (response.ok) {
          const data = await response.json();
          console.log(data.message);
          location.reload();
        } else {
          console.error("Failed to delete message:", response.status);
          alert("Failed to delete message:", response.status);
        }
      } catch (error) {
        console.error("Failed to fetch:", error);
      }
    }
  });
});
