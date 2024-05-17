async function queryMember(username) {
  try {
    const response = await fetch(`/api/member?username=${username}`, {
      method: "GET",
    });
    if (response.ok) {
      const content = await response.json();
      return content;
    } else {
      throw new Error(
        `Server Error: ${response.status} ${response.statusText}`
      );
    }
  } catch (error) {
    console.error("Fetch Error:", error);
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
    if (response.ok) {
      const content = await response.json();
      return content;
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
