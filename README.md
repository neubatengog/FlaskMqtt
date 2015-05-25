# Creating a browser based using python, flask, socketio, MQTT

Written in Python using the flask web framework this example subscribes to a MQTT topic to which logs are posted from broker mosquitto and pushes messages up to the browser using socket.io. The results are displayed in a html box that looks like a ubuntu linux terminal window. The example includes basic session based authentication with a hardcoded username and password see app.py.


# Install

    sudo pip install Flask
    sudo pip install Flask-SocketIO
    sudo pip install paho-mqtt
    
Installation of Flask-SocketIO can be slow on a raspberrypi.

see: https://flask-socketio.readthedocs.org/en/latest/

Code is based on the flask-socketio example
