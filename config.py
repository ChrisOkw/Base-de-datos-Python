import sys

DATABASE_PATH = "usuarios.csv"

if "pytest" in sys.argv[0]: #esto se hace para no machacar y sobreescribir el archivo de usuarios.csv
    DATABASE_PATH = "test/usuarios_test.csv"
