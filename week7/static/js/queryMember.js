async function queryMember(username) {
  try {
    const response = await fetch(`/api/member?username=${username}`, {
      method: "GET",
    });
    const status_code = response.status;
    if (response.ok) {
      if (content && status_code === 200) {
        const content = await response.json();
        console.log("content:", content);
        return content;
      } else {
        return null;
      }
    } else {
      console.error("Server Error:", data.error.message);
      throw new Error(
        `Server Error: ${response.status} ${response.statusText}`
      );
    }
  } catch (error) {
    console.error("Fetch Error:", error.message);
    throw error;
  }
}

async function updatingName(name) {
  try {
    const response = await fetch("/api/member", {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ name: name }),
    });
    const status_code = response.status;
    if (response.ok) {
      const content = await response.json();
      if (content && status_code === 200) {
        displayUpdateStatus("Updated successfully", true);
        displayUpdateName(name);
        return content;
      } else {
        displayUpdateStatus("Failed to update", false);
        return null;
      }
    } else {
      console.error("Server Error:", content.error);
      throw new Error(
        `Server Error: ${response.status} ${response.statusText}`
      );
    }
  } catch (error) {
    console.error("Fetch Error:", error);
    throw error;
  }
}
