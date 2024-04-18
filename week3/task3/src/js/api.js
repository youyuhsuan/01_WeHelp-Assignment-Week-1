async function getData() {
  try {
    const response = await fetch(
      "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
    );
    if (!response.ok) {
      throw new Error("Could not fetch resource");
    }
    const data = await response.json();
    dynamicHTML(data);
  } catch (error) {
    console.error(error);
  }
}
getData();
