import json
import pika


def create_connection():
    """Создаёт и возвращает соединение с RabbitMQ на localhost
    """
    return pika.BlockingConnection(pika.ConnectionParameters("localhost"))


try:
    #Установка соединения и создание канала с RabbitMQ
    connection = create_connection()
    channel = connection.channel()

    #Объявление очередей
    channel.queue_declare(queue='new_order', durable=True)
    channel.queue_declare(queue='process_order', durable=True)
    channel.queue_declare(queue='send_notification', durable=True)

    #Ограничение количества сообщений (=1)
    channel.basic_qos(prefetch_count=1)


    def callback(ch, method, properties, body):
        """" Функция обратного вызова для обработки заказов
         ch (pika.channel.Channel): Канал RabbitMQ.

            method (pika.spec.Basic.Deliver): Метаданные доставки сообщения.
            properties (pika.spec.BasicProperties): Свойства сообщения.
            body (bytes): Тело сообщения, содержащее данные о заказе.

        После обработки заказа отправляет подтверждение о его получении
        """
        order = json.loads(body) # Преобразование в словарь
        print(f"Получен заказ {order}")
        process_order(order) # Обработка полученного заказа
        ch.basic_ack(delivery_tag = method.delivery_tag) # Отправляем подтверждение о получении сообщения


    def process_order(order):
        """ Обрабатывает заказ и отправляет уведомление о статусе.

                order (dict): Словарь с данными о заказе, содержащий ключ 'item'.

            Отправляет уведомление о статусе обработки заказа в очередь `send_notification`.
        """
        print(f"Заказ {order['item']} обработан")

        status_notification = f"Ваш заказ {order['item']} обработан"

        # Формируем уведомление о статусе заказа
        channel.basic_publish(
            exchange='', # Используем стандартный обменник
            routing_key='send_notification', # Указываем очередь
            body=status_notification, # Сообщение
            properties=pika.BasicProperties(
                delivery_mode=pika.DeliveryMode.Persistent # Убедимся, что сообщение будет сохранено
        ))

    # Подписываемся на очередь с новыми заказами
    channel.basic_consume(
        queue='new_order',
        on_message_callback=callback # Указываем функцию, которая будет вызываться при получении сообщения
    )
    print('Ожидание сообщений. Нажмите CTRL+C для выхода.')
    channel.start_consuming() # Начинаем получать сообщения из очереди
except Exception as e:
    print("Ошибка в обработчике")