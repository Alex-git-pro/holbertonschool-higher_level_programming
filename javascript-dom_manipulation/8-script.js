fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
  .then(response => response.json())
  .then(data => {
    const helloMessage = data.hello;

    document.querySelector("#hello").textContent = helloMessage;
  })
  .catch(error => {
    console.log("Error:", error);
  });
