// this is for the map in home
window.addEventListener('load', function () {


    const clickable = document.getElementsByClassName('clickable')


    const clickable_array = Array.from(clickable)


    for (let i = 0; i < clickable_array.length; i++) {

        clickable_array[i].onmouseover = function(){
            basic_opacity = clickable_array[i].style.fillOpacity
            clickable_array[i].style.fillOpacity = 0.2;
            console.log(clickable_array[i]);
            
        }
        clickable_array[i].onmouseout = function(){

            clickable_array[i].style.fillOpacity = basic_opacity;
        }
                
    }
});


// this is for ajax stoisko.html comment liking

async function make_request(url, method, body){
    headers = {
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/json'
    }

    if (method == "post"){
        const csrf = document.querySelector('[name=csrfmiddlewaretoken]').value
        headers['X-CSRFToken'] = csrf
    }
    let response = await fetch(url, {
        method: method,
        headers: headers,
        body: body
    })
    return await response.json()
}

async function get_likes(komentarz_id){

    const data = await make_request(url = 'polubienie/', method = 'post', body = JSON.stringify({'komentarz_id':komentarz_id}))

    id = `polubienie ${komentarz_id}`

    let ilosc_polubien = document.getElementById(id)
    ilosc_polubien.innerHTML = data['ilosc_polubien']

}

const rate = (rating, stoisko_id) => {
    fetch(`/stoisko/${stoisko_id}/${rating}/`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(rest => {
        window.location.reload();
        //moze kiedys ajax wjedzie prawdziwy, ilosc/wielkosc requestow do bazy danych nie ma az takiego znaczenia dla strony targow xdddd
    })
}
