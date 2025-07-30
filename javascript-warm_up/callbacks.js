const posts = [
    {title: "Post one", body: "This is post one"}, 
    {title: "Post two", body: "This is post two"}
];

function getPosts() {
    setTimeout(() => {
        let output = ''
        posts.forEach((post, index) => { /* searches through the blog list*/
            output += `<li>${post.title}<li>`; /* creates lists of all the titles*/
        });
        document.body.innerHTML = output; /* inserts the items unto the body */
    }, 1000);
}

getPosts();

/* normally, this will not work when testing the html due to the
fact that the website's index page already appended the two previous
items post 1 and post 2 into the document. Take note of how they are seconds
apart and the logic fails in synchronous functions

Therefore, to allow this to be added into the html, we would need
asynchronous functions*/

function createPosts(post, callback) {
    setTimeout(() => {
        posts.push(post);
        callback();
    }, 2000);
};

/* to correct the function and implement async performance, we would
need to implement callback functions*/
createPosts({title: "Post three", body: "this is post three"}, getPosts);