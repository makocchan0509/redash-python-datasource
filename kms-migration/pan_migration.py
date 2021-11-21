from dotenv import load_dotenv
from Crypto.Cipher import AES
import os, sys, postgresql


def get_env():
    key = os.getenv("AES_KEY")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    database = os.getenv("DB_DATABASE")
    return key, host, port, user, password, database


def get_conn(user: str, password: str, host: str, port: str, database: str):
    # pq://user:password@host:port/database
    conn_identify = "pq://{}:{}@{}:{}/{}"
    return postgresql.open(conn_identify.format(user, password, host, port, database))


def all_enc() -> None:
    key, host, port, user, password, database = get_env()
    db = get_conn(user, password, host, port, database)

    select_all_data_sql = "SELECT transaction_id,pan FROM transactions"
    update_encrypted_pan_sql = "UPDATE transactions SET pan_enc = $2, pan_enc_bin = $3 WHERE transaction_id = $1"

    select_transactions = db.prepare(select_all_data_sql)
    update_transaction = db.prepare(update_encrypted_pan_sql)

    with db.xact():
        for row in select_transactions():
            enc_hex, enc_byte = encryption(key, row["pan"])
            update_transaction(row["transaction_id"], enc_hex, enc_byte)


def all_dec() -> None:
    key, host, port, user, password, database = get_env()
    db = get_conn(user, password, host, port, database)

    select_all_data_sql = "SELECT transaction_id,pan_enc,pan_enc_bin FROM transactions"
    select_transactions = db.prepare(select_all_data_sql)

    for row in select_transactions():
        pan_dec_st = decryption(key, bytes.fromhex(row["pan_enc"]))
        pan_dec_by = decryption(key, row["pan_enc_bin"])
        print(row["transaction_id"])
        print(pan_dec_st.decode('utf-8'))
        print(pan_dec_by.decode('utf-8'))
        print("-----")


def encryption(key: str, text: str):
    cipher = AES.new(bytes.fromhex(key), AES.MODE_ECB)
    enc_result = cipher.encrypt(text.encode('utf-8'))
    print(enc_result)
    print(enc_result.hex())
    return enc_result.hex(), enc_result


def decryption(key:str, target: bytes):
    cipher = AES.new(bytes.fromhex(key), AES.MODE_ECB)
    dec_result = cipher.decrypt(target)
    return dec_result


if __name__ == "__main__":
    arg = sys.argv[1]
    load_dotenv()

    if arg == "enc":
        all_enc()
    elif arg == "dec":
        all_dec()
    else:
        print("[ERROR] invalid arg.")
