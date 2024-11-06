import json
import pika
import psycopg2

def create_connection():
    return pika.BlockingConnection(pika.ConnectionParameters("localhost"))


try:
    connection = create_connection()
    channel = connection.channel()

    channel.basic_qos(prefetch_count=1)


    def callback(ch, method, properties, body):
        order = json.loads(body)
        print(f"Получен заказ {order}")
        confirm_order(order)
        test_order(order)
        update_status(order['user_id'])
        delivery(order)

        delivery_notification = f"Ваш заказ {order['item']} доставлен"
        channel.basic_publish(
            exchange='',
            routing_key='send_notification',
            body=delivery_notification,
            properties=pika.BasicProperties(
                delivery_mode=1
        ))
        ch.basic_ack(delivery_tag = method.delivery_tag)


    def confirm_order(order):
        print(f"Заказ {order['item']} подтверждён")


    def test_order(order):
        try:
            conn = psycopg2.connect(dbname="orders", user="postgres", password="1234", host="localhost", port="5432")
            cursor = conn.cursor()

            cursor.execute(f"INSERT INTO orders (item, price, user_id) VALUES ('{order['item']}', {order['price']}, {order['user_id']})")
            conn.commit()
        except Exception as r:
            print(f"Где-то произошла ошибка {r}")
        finally:
            cursor.close()
            conn.close()


    def update_status(user_id):
        print(f"Заказ клиента {user_id} подтверждён")

    def delivery(order):
        print(f"Заказ {order['item']} отправлен")


    channel.basic_consume(
        queue='new_order',
        on_message_callback=callback
    )
    print('Ожидание сообщений. Нажмите CTRL+C для выхода.')
    channel.start_consuming()
except Exception as e:
    print(f"Ошибка в consumer {e}")