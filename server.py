from flask import Flask, render_template, session, request, redirect, Response
from flask.ext.socketio import SocketIO, emit
from flask import jsonify

import paho.mqtt.client as mqtt
from db import Accionwtec




app = Flask(__name__)
app.debug = True
socketio = SocketIO(app)




#----------------RUTAS---------------#

@app.route('/')
def  index():
	listado_equipos = Accionwtec.AccionWtec().listarEquipos()
	#equipos=listado_equipos
	return render_template ('tables.html')

@app.route('/equipos')
def  equipos():
	listado_equipos = Accionwtec.AccionWtec().listarEquipos()
	equipos=listado_equipos
	return render_template ('tables2.html', datos = equipos )

@app.route('/consola')
def consola():
	return render_template ('forms.html')

@app.route('/data/datos.json')
def  jsonEquipos():
	listado_equipos = Accionwtec.AccionWtec().listarEquipos()
	return jsonify(data=listado_equipos)


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
		print "Conexion exitosa al servidor COD:[{0}]".format(str(rc))
		client.subscribe("DATA/#")

	if rc == 1:
		print "Conexion rechazada COD:[{0}]".format(str(rc))
	if rc == 2:
		print "Conexion rechazada COD:[{0}]".format(str(rc))
	if rc == 3:
		print "Conexion rechazada COD:[{0}]".format(str(rc))	
	if rc == 4:
		print "Conexion rechazada COD:[{0}]".format(str(rc))
	if rc == 5:
		print "Conexion rechazada COD:[{0}]".format(str(rc))

def on_message(client, userdata, message):
	print("Valor recibido: '" + str(message.payload) + "' en topic: '"
		+ message.topic + "' con QOS " + str(message.qos))
	parsear(str(message.topic), str(message.payload))
	socketio.emit('my response', { 'topic' :message.topic, 'payload':message.payload} , namespace='/test')
	

def on_disconnect(client, userdata, rc):
	if rc != 0:
		print("Desconexion inesperada.")
	print "Desconexion"

@socketio.on('my event', namespace='/test')
def test_message(message):
    pass


@socketio.on('connect', namespace='/test')
def test_connect():
    pass

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    pass 

#-------------FIN MQTT---------------#

def main():
	app.run(host='0.0.0.0', port=9080)
	try:
		client = mqtt.Client()
		client.on_connect = on_connect
		client.on_message = on_message
		client.connect("dev.wtec.cl", 1883, 6)
		
		client.loop_forever()
	except Exception, e:
		client.disconnect
		client.reconnect()
		print "Error:{0} ".format(str(e))

if __name__ == '__main__':main()
	