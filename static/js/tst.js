
    var view = "console";

    
    $(document).ready(function(){
        
        view = (window.location.hash).substring(1);
        
        
        namespace = '/test'; 
        //var socket = io.connect('http://192.168.227.133:8000' + namespace);
        var socket = io.connect('http://' + document.domain + ':' + location.port + namespace);
        socket.on('connect', function() {
            socket.emit('cliente mensaje', { data: 'conectado'});
           
        });
       
        socket.on('server respuesta', function(msg) {
            console.log(msg)
           
            $('.console-out').append("[COMANDO:"+msg.topic+"] [VALOR:"+msg.payload+"]\n");
            var h = parseInt($('#log')[0].scrollHeight);
            $('#log').scrollTop(h);
            
        });

       

         $("#enviarcomando").click(function(){
            $.ajax({ 
                type: "POST", 
                url: "/comando", 
                contentType: "text/plain", 
                data: $("#comando").val() 
            });
        });
        
        // socket.emit('my event', {data: $('#emit_data').val()});
        
       
        
    });
    
  
        

