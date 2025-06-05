function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function putRequest(url, requestBody) {
    return fetch(url, {
        method: "PUT",
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify(requestBody)
    });
}

async function likeButtonFunctionality(element) {
    const isLikeButton = element.dataset.like === "true" ? 1 : 0;
    try {
        const response = await putRequest('/like', { "like": isLikeButton, "postID": element.dataset.postid });

        if (!response.ok) {
            throw new Error(`Response Status: ${response.status}`);
        }

        // now change the like button content and update like counter
        if (isLikeButton) {
            element.dataset.like = "false";
            element.innerHTML = "remove like";
            document.querySelector(`.like-count-${element.dataset.postid}`).innerHTML++;
        } else {
            element.dataset.like = "true";
            element.innerHTML = "add like";
            document.querySelector(`.like-count-${element.dataset.postid}`).innerHTML--;
        }
    } catch (error) {
        console.error(error.message);
    }
}

function displayEditPostForm(element) {
    const postid = element.dataset.postid;
    const previousPostContent = document.querySelector(`.post-content-${postid}`).innerHTML;
    document.querySelector(`.post-content-${postid}`).innerHTML = `
        <div class="edit-post">
            <textarea class="edit-post-content-${postid}">${previousPostContent}</textarea>
            <button class="edit-post-submit-button" data-postid="${postid}">save</button>
        </div>
    `;
    document.querySelector(`.edit-post-content-${postid}`).focus();
    element.disabled = true;
}

async function editPostSubmitButtonFunctionality(element) {
    const postid = element.dataset.postid;
    const newPostContent = document.querySelector(`.edit-post-content-${postid}`).value;

    try {
        const response = await putRequest('/editPost', { "postContent": newPostContent, "postID": postid });

        if (!response.ok) {
            alert("You cannot edit other user's post!!");
            throw new Error(`Response Status: ${response.status}`);
        }

        document.querySelector(`.post-content-${postid}`).innerHTML = newPostContent;
        document.querySelector(`#edit-post-button-${postid}`).disabled = false;
    } catch (error) {
        console.error(error.message);
    }
}

async function addComment(postID, commentContent) {
    const response = await fetch('/addComment', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({ "postID":postID, "content":commentContent })
    });

    if (!response.ok) {
        throw new Error(`Response Status: ${response.status}`);
    }

    console.log("Comment added successfully");
}

async function loadComments(postID) {
    const response = await fetch(`/getComments?postID=${postID}`);
    if (!response.ok) {
        throw new Error(`Response Status: ${response.status}`);
    }

    const comments = await response.json();
    const commentsContainer = document.querySelector(`#all-the-comments-${postID}`);
    commentsContainer.innerHTML = '';

    if (comments.length === 0) {
        commentsContainer.innerHTML = `
            <div class="card mb-4" id="empty-comment-section-${postID}">
                <div class="card-body">
                    <p>No Comments on this post so far.</p>
                </div>
            </div>
        `;
    } else {
        comments.forEach(comment => {
            commentsContainer.innerHTML += `
                <div class="card mb-4">
                    <div class="card-body">
                        <p>${comment.content}</p>
                        <div class="d-flex justify-content-between">
                            <div class="d-flex flex-row align-items-center">
                                <p class="small mb-0 ms-2">
                                    <a class="hover-effect text-decoration-none" href="/user/${comment.writer.username}">${comment.writer.username}</a>
                                </p>
                            </div>
                            <div class="d-flex flex-row align-items-center">
                                <p class="small text-muted mb-0">${comment.created_at}</p>
                            </div>
                        </div>
                    </div>
                </div>
            `;
        });
    }

    console.log("comments loaded successfully");
}

document.addEventListener('DOMContentLoaded', function () {
    document.addEventListener('click', async function (event) {
        const element = event.target;
        console.log(element.className);
        if (element.className === "like-button") {
            await likeButtonFunctionality(element);
        } else if (element.className === "edit-post-button") {
            displayEditPostForm(element);
        } else if (element.className === "edit-post-submit-button") {
            await editPostSubmitButtonFunctionality(element);
        } else if (element.className === "save-comment-button") {
            console.log("i have clicked the save comment button");
            const postID = element.dataset.postid;
            const commentContent = document.querySelector(`#addANote-${postID}`).value;
            try {
                await addComment(postID, commentContent);
                await loadComments(postID);
                document.querySelector(`#addANote-${postID}`).value = "";

            } catch (error) {
                console.error(error.message);
            }
        }
    });

    document.querySelectorAll('.modal').forEach(modal => {
        modal.addEventListener('shown.bs.modal', async function () {
            const postID = modal.dataset.postid;
            try {
                await loadComments(postID);
            } catch (error) {
                console.error(error.message);
            }
        });
    });
});