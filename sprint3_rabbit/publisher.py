import json
import pika

def create_connection():
    return pika.BlockingConnection(pika.ConnectionParameters("localhost"))


try:
    connection = create_connection()
    channel = connection.channel()

    channel.queue_declare(queue='new_order', durable=True)
    channel.queue_declare(queue='process_order', durable=True)
    channel.queue_declare(queue='send_notification', durable=True)

    order = {
        "item" : "iphone",
        "price" : 150000,
        "user_id" : 1
    }
    if "item" in order and "user_id" in order:

        order_json = json.dumps(order)
        channel.basic_publish(
            exchange='',
            routing_key='new_order',
            body=order_json,
            properties=pika.BasicProperties(
                delivery_mode=1
        ))
        print(f"Заказ создан {order_json}")
        notification = f"Ваш заказ {order['item']} обрабатывается"
        channel.basic_publish(
            exchange='',
            routing_key='send_notification',
            body=notification,
            properties = pika.BasicProperties(
                delivery_mode=1
        ))
    else:
        raise ValueError("Ошибка заказа")
except Exception as e:
    print("Ошибка в publisher")
finally:
    connection.close()
