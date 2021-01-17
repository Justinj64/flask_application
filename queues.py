from config import Config
from kombu import Exchange, Queue

## configure queue and exchanges
exchange_name = Config.ENCHANGE_NAME
item_queue_name = Config.ITEM_QUEUE_NAME
item_routing_key = Config.ITEM_ROUTING_KEY

exchange = Exchange(exchange_name, type=Config.EXCHANGE_TYPE)

task_queues = [Queue(
    item_queue_name,
    exchange=exchange,
    routing_key=item_routing_key)]