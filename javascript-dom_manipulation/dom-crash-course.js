const title = document.getElementById('title');
const outputE1 = document.querySelector('.output');
const button = document.getElementById('change-text');


button.addEventListener('click', () => {
    title.textContent = 'Logged in';
    outputE1.element.innerHTML = `<p>Hello, user</p>`;
    title.style.color = 'blue';
});

/*this is a second exercise for adding events and manipulating DOM
the mockup HTML tags for which we will perform the manipulation are the following: 

<div class="action">Standard text</div>
<button id="change-color">Click me</button>
<script>script.js</script>


*/

const button2 = document.getElementById("change-color")
const output2 = document.querySelector('.action')

button2.addEventListener('click', () => {
  output2.textContent = 'You clicked me!';
  output2.style.backgroundcolor = 'lightblue';
}
)