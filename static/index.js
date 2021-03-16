document.addEventListener('DOMContentLoaded', nav)

function nav(){

    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.main-nav');
	const search_id = document.getElementById('search_id');
	const btn_search = document.querySelector('button');

    burger.addEventListener('click', ()=>{
        nav.classList.toggle('show')
    })

	btn_search.addEventListener("click",e=>{
		video = search_id.value.trim()
		if(video=="") document.location.href = `/`
		else document.location.href = `/?video=${video}`
	})

}

function $_GET(param) {
	var vars = {};
	window.location.href.replace( location.hash, '' ).replace( 
		/[?&]+([^=&]+)=?([^&]*)?/gi, // regexp
		function( m, key, value ) { // callback
			vars[key] = value !== undefined ? value : '';
		}
	);

	if ( param ) {
		return vars[param] ? vars[param] : null;	
	}
	return vars;
}