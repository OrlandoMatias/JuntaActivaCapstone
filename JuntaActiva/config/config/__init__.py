import pymysql

# Permite que Django use PyMySQL como si fuera mysqlclient
pymysql.install_as_MySQLdb()
