from opcua import ua, uamethod, Server
from time import sleep
import logging
import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="classicmodels")

mycursor = mydb.cursor(buffered=True , dictionary=True)

sql = "SELECT * FROM classicmodels.customers"
mycursor.execute(sql)
myresult = mycursor.fetchone()

sql1 = "SELECT * FROM classicmodels.employees"
mycursor.execute(sql1)
myresult1 = mycursor.fetchone()


if __name__ == "__main__":
    """
    OPC-UA-Server Setup
    """
    server = Server()

    endpoint = "opc.tcp://127.0.0.1:4848"
    server.set_endpoint(endpoint)

    servername = "Python-OPC-UA-Server"
    server.set_server_name(servername)
    """
    OPC-UA-Modeling
    """
    root_node = server.get_root_node()
    object_node = server.get_objects_node()
    idx = server.register_namespace("OPCUA_SERVER")
    myobj = object_node.add_object(idx, "DA_UA")
    myobj1 = object_node.add_object(idx, "D_U")
    """
    OPC-UA-Server Add Variable
    """

    for key, value in myresult.items():
        myobj.add_variable(idx, key, str(value))
    for key, value in myresult1.items():
        myobj1.add_variable(idx, key, str(value))
    """
    OPC-UA-Server Start
    """
    server.start()
'''
