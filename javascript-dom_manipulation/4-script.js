document.querySelector('#add_item').addEventListener('click', () => {
  const list = document.createElement('li');
  list.textContent = 'Item'
  document.querySelector('.my_list').appendChild(list)
})