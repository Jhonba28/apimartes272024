#Datos para la conexion a BD

dataBaseName="gestordb"
userName= "root"
userPassword = ""
conncetionPort=3306
server="localhost"

#creando la conexion
dataBaseConnection=f"mysql+mysqlconnector://{userName}:{userPassword}@{server}:{conncetionPort}/{dataBaseName}"

print(dataBaseConnection)