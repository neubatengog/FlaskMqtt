from gevent import monkey
monkey.patch_all()

from flask import Flask, render_template, session, request, redirect, Response
from flask.ext.socketio import SocketIO, emit
from flask import jsonify
import paho.mqtt.client as mqtt
from db import Accionwtec

from threading import Thread

app = Flask(__name__)
app.debug = True
mqtt_thread = None
socketio = SocketIO(app)


class MQTT_Thread(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.stop = False

	def run(self):
		while not self.stop and client.loop_forever() == 0:
			pass
		print "MQTT Thread terminado"

#----------------RUTAS---------------#
@app.route('/')
@app.route('/monitor/')
def  equipos():
	listado_equipos = Accionwtec.AccionWtec().listarEquipos()
	equipos = listado_equipos
	return render_template ('tables2.html', datos = equipos )


@app.route('/comando',methods = ['GET','POST'])
def conf():
	if request.method == 'POST':
			comando = request.data.split(",")
			peticion = comando[0]
			idCliente = comando[1]
			print peticion, idCliente
			client.publish("CONF/"+idCliente, peticion)
			return "ok"
	else:
		return Response(content, mimetype='text/plain')

@app.route('/consola/')
def consola():
	return render_template ('forms.html')

@app.route('/data/datos.json')
def  jsonEquipos():
	listado_equipos = Accionwtec.AccionWtec().listarEquipos()
	return jsonify(data = listado_equipos)

#--------------FIN RUTAS------------#


#----------------MQTT---------------#

def parsear(topic,datos):
	try:
		valores_tele = { }
		val = {}

		valores_topic = topic.split("/")
		valores_telemetria = datos.split(",")
		if valores_topic[0] == "DATA":
			#print "DATA Telemetria TST[%s]" % valores_topic[1]	
			for x in valores_telemetria[1:]:
				k, v = x.split(":")
				val[k] = v
			#DICCIONARIO {fecha : {tag : valor , tag:valor }}
			#valores_tele[valores_telemetria[0]] = val
			
			#clase datos (id, telemetria)
			#bd = Datos(valores_topic[1], valores_tele)
			#bd.procesar()
		
	except Exception, e:
		print "Error: {0}".format(str(e))


def on_connect(client, userdata, rc):
	if rc == 0:
		print "Conectado al servidor MQTT COD:[{0}]".format(str(rc))
		client.subscribe("RESP/#")
	elif rc != 0:
		print "Conexion rechazada al servidor MQTT COD:[{0}]".format(str(rc))
	
def on_message(client, userdata, message):
	socketio.emit('server respuesta', { 'topic' :message.topic, 'payload':message.payload } , namespace='/test')
	
def on_disconnect(client, userdata, rc):
	if rc != 0:
		print "Desconexion inesperada al servidor MQTT COD:[{0}]".format(str(rc))
	

@socketio.on('cliente mensaje', namespace='/test')
def test_message(message):
    pass

@socketio.on('connect', namespace='/test')
def test_connect():
	pass

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    pass 

#-------------FIN MQTT---------------#

client = mqtt.Client(client_id="agente")
client.on_connect = on_connect
client.on_message = on_message
client.connect("dev.wtec.cl", 1883, 10)


def main():
	try:
		mqtt_thread = MQTT_Thread()
		mqtt_thread.start()
		socketio.run(app, host='0.0.0.0',port=8000)
	except Exception, e:
		client.disconnect
		client.reconnect()
		print "Error:{0} ".format(str(e))

if __name__ == '__main__':main()
	