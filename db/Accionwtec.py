from db.conec import DBconec


class AccionWtec(DBconec.DBcon):
	
	def __init__(self):
		pass

	def validarUsuario(self, usuario, clave):
		con = self.conexion().connect().cursor()
		con.execute(""" select * from usuarios where usuario='%s' and clave='%s'""" % (usuario, clave))

	def listarEquipos(self):
		con = self.conexion().connect().cursor()
		con.execute(" select um.id, um.nombre, um.serie, r.conexion, r.actualizacion from registro r, um where um.serie = r.serie order by um.nombre asc ")
		equipos = con.fetchall()
		return equipos 

	def listaJson(self, datobuscado):
		con=self.conexion().connect().cursor()
		con.execute("select um.id, um.nombre, um.serie, r.conexion, r.actualizacion from registro r, um where um.serie = r.serie order by um.nombre asc  ")
		reporte=con.fetchall()
		columna=('value', 'id')
		lista=[]
		for row in reporte:
			lista.append(dict(zip(columna, row)))
		return json.dumps(lista, indent=2)