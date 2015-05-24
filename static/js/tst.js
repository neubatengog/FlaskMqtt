
    var view = "console";

    
    $(document).ready(function(){
        view = (window.location.hash).substring(1);
        
        
        namespace = '/test'; // change to an empty string to use the global namespace
        // the socket.io documentation recommends sending an explicit package upon connection
        // this is specially important when using the global namespace
        //var socket = io.connect('http://192.168.227.133:8000' + namespace);
        var socket = io.connect('http://' + document.domain + ':' + location.port + namespace);
        socket.on('connect', function() {
            socket.emit('my event', { data: 'conectado'});
           
        });
        // event handler for server sent data
        // the data is displayed in the "Received" section of the page
        socket.on('my response', function(msg) {
            console.log(msg)
            $('.console-out').append(msg.topic+" "+msg.payload+"\n");
            var h = parseInt($('#log')[0].scrollHeight);
            $('#log').scrollTop(h);
            
        });

        socket.on('mi conexion', function(msg) {
            console.log(msg.data)
            $('.console-out').append(msg.data+"\n");
            var h = parseInt($('#log')[0].scrollHeight);
            $('#log').scrollTop(h);
            
        });
        
        // socket.emit('my event', {data: $('#emit_data').val()});
        
       
        
    });
    
  
        

