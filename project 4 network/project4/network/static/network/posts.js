

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

        //now change the like button content and update like counter
        if (isLikeButton) {
            element.dataset.like = "false";
            element.innerHTML = "remove like";
            document.querySelector(`.like-count-${element.dataset.postid}`).innerHTML++;
        } else {
            element.dataset.like = "true";
            element.innerHTML = "add like";
            document.querySelector(`.like-count-${element.dataset.postid}`).innerHTML--;
        }
    }
    catch (error) {
        console.error(error.message);
    }
}

function displayEditPostForm(element) {
    const postid = element.dataset.postid;
    const previousPostContent = document.querySelector(`.post-content-${postid}`).innerHTML;
    document.querySelector(`.post-content-${postid}`).innerHTML = `
            <div class="edit-post">
                <textarea class="edit-post-content-${postid}" >${previousPostContent}</textarea>
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
            alert("You cannot edit other user's post!!")
            throw new Error(`Response Status: ${response.status}`);
        }


        document.querySelector(`.post-content-${postid}`).innerHTML = newPostContent;
        document.querySelector(`#edit-post-button-${postid}`).disabled = false;

    }
    catch (error) {
        console.error(error.message);
    }

}

document.addEventListener('DOMContentLoaded', function () {
    document.addEventListener('click', async function (event) {
        const element = event.target;

        if (element.className === "like-button") {
            await likeButtonFunctionality(element);
        } else if (element.className === "edit-post-button") {
            displayEditPostForm(element);
        } else if (element.className === "edit-post-submit-button") {
            await editPostSubmitButtonFunctionality(element);
        }
    })
})