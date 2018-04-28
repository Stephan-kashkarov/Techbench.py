$( document ).ready( function() {
	var height = $( document ).height();
	$( window ).scroll( function() {

		console.log( parseInt( ( $( this ).scrollTop() / height ) * 100 ) );
		if ( $( this ).scroll() ) {
			let initial = $( this ).scroll();
		}
	} );
} );
