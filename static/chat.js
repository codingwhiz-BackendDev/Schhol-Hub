$(document).ready(function () {
    $(document).on('submit', '#chat-message', function (e) {
        e.preventDefault()
        $.ajax({
            type: 'POST',
            url: '/send_chat_message',
            data: {
                sender: $('#sender').val(),
                receiver: $('#receiver').val(),
                profile_image: $('#profile_image').val(),
                message: $('#message').val(),
                receiverId: $('#receiverId').val(),
                senderId: $('#senderId').val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function (response) {
                // document.getElementById('display-comment').innerHTML = response
                //alert(response) 

            },
            error: function (response) {
                //alert('an error occured')
            }
        })
        document.getElementById('message').value = ''
    })
})

$(document).ready(function () {
    setInterval(function () {

        $.ajax({
            type: 'GET',
            url: '/get_chat_message/' + $('#pks').val(),
            success: function (response) {

                $('#display-comment').empty()
                for (var key in response.messages) {
                    if (response.messages[key].sender != $('#user').val()) {
                        var temp = "<div class='border-t pt-4' style='margin-right:auto;width:fit-content;'><div class='flex'><div class='w-10 h-10 rounded-full relative flex-shrink-0'><img class='absolute h-full rounded-full w-full' src = " + response.messages[key].profileimage + "/></div><div class='text-gray-700 py-2 px-3 rounded-md bg-gray-100 h-full relative lg:ml-5 ml-2 lg:mr-20'><h6><b><a href =" +
                            '/profile/' + response.messages[key].sender + " > " + response.messages[key].sender + "</a></b ></h6 > <p class='leading-6'><ul>" + response.messages[key].message + "</ul></div></div ></div > "
                        $('#display-comment').append(temp)

                    } else {
                        var temp = "<div class='border-t pt-4' style='margin-left:auto;width:fit-content;'><div class='flex'><div class='w-10 h-10 rounded-full relative'></div><div class='text-gray-700 py-2 px-3 rounded-md bg-gray-100 h-full relative lg:ml-5 ml-2 lg:mr-20' style='background-color:pink;'><h6><b><a href =" +
                            '/profile/' + response.messages[key].sender + " > " + 'You' + "</a></b ></h6 > <p class='leading-6'><ul>" + response.messages[key].message + "</ul></div></div ></div > "
                        $('#display-comment').append(temp)

                    }
                }

            },
            error: function (response) {
                //alert('an error occured')
            }
        });
    }, 100)
})

window.oninput = function ScrollTo() {
    window.scrollTo(0, document.body.scrollHeight)
}
window.onclick = function ScrollTo() {
    window.scrollTo(0, document.body.scrollHeight)
}
window.onchange = function ScrollTo() {
    window.scrollTo(0, document.body.scrollHeight)
}