fetch("https://swapi-api.hbtn.io/api/films/?format=json")
  .then(response => response.json())  // Convert the response to JSON
  .then(data => {
    const films = data.results;

    const listMovies = document.querySelector("#list_movies");

    films.forEach(film => {
      const li = document.createElement("li");
      li.textContent = film.title;
      listMovies.appendChild(li);
    });
  })
  .catch(error => {
    console.log("Error:", error);
  });
