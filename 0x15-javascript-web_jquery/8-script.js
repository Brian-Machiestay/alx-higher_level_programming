$.get('https://swapi-api.hbtn.io/api/films/?format=json', function(data, stat){
    data.results.forEach(function(item){
        $('UL#list_movies').append('<li>' + item.title + '</li>');
    });
});