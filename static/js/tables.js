var table = $('#example').DataTable();
 
table.rows().every( function () {
    var d = this.data();
 
    d.counter++; // update data source for the row
 
    this.invalidate(); // invalidate the data DataTables has cached for this row
} );
 
// Draw once all updates are done
table.draw();

var table = $('#example').DataTable();
var data = table
    .cells( ".info" )
    .data();
 console.log( data );


 $('#tblUsuario tr').each(function () {

var pk = $(this).find("td").eq(0).html();
var nombre = $(this).find("td").eq(1).html();
var apellidos = $(this).find("td").eq(3).html();

});

     $('#equipos').DataTable( {
            "language" : {
              "search": "Busqueda:",
              "paginate": {
                  "first": "Primer",
                  "previous": "Previo",
                  "next":"Siguiente",
                  "last":"Ultimo"
              }
          },          
            "ajax": "../data/datos.json"
          });