fetch ('https://swapi-api.hbtn.io/api/films/?format=json')
  .then (response => response.json()) //gives back the JSON object
  .then (data => { //accessess the data
    data.results.forEach(movie => { //iteates through every element in the key
        const li = document.createElement('li') //creates the list item
        li.textContent = movie.title //fills the element with the title list
        document.querySelector('#list_movies').appendChild(li) //appends every title
    });
  })