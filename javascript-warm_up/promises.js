#!/bin/node
const posts = [
    {title: "Post one", body: "This is post one"}, 
    {title: "Post two", body: "This is post two"}
];

function getPosts() {
    setTimeout(() => {
        let output = ''
        posts.forEach((post, index) => { /* searches through the blog list*/
            output += `<li>${post.title}</li>`; /* creates lists of all the titles*/
        });
        document.body.innerHTML = output; /* inserts the items unto the HTML body */
    }, 1000);
}

getPosts();

/* normally, this will not work when testing the html due to the
fact that the website's index page already appended the two previous
items post 1 and post 2 into the document. Take note of how they are seconds
apart and the logic fails in synchronous functions

Therefore, to allow this to be added into the html, we would need
asynchronous functions*/

function createPosts(post) {
    return new Promise((resolve, reject) => {
    setTimeout(() => {
        posts.push(post);

        const error = false; /* checking for true now, remember to switch back */

        if(!error) {
            resolve(); /* simple error checking */
        } else {
            reject("Error: something went wrong");
        }
    }, 2000);
    });
};

/* to correct the function and implement async performance, we would
need to implement callback functions*/
/* or, for simplicity, we create a promise, which is then followed by
the get posts function */ 

/*createPosts({title: "Post three", body: "this is post three"})
.then(getPosts)
.catch(err => console.log(err)); <--- add this back and review later

/* async and await*/
/* utilizing these permits us to perform async of two functions */
async function init() {
    await createPosts({title: "post three", body: "This is post three"});

    getPosts()
}

init()

/* Promise.all */
const promise1 = Promise.resolve('Hello, mum');
const promise2 = 10;
const promise3 = new Promise((resolve, reject) =>
setTimeout(resolve, 2000, 'Bye'));

Promise.all([promise1, promise2, promise3]).then(values => console.log(values))

/* fetching objects with http and AJAX */
promise4 = fetch('https://jsonplaceholder.typicode.com/users')
