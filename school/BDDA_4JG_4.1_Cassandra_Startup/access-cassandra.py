from cassandra.cluster import Cluster

cluster = Cluster(['10.115.2.20'], port=8042)
session = cluster.connect('store', wait_for_all_pools=True)
session.execute('USE store')

rows = session.execute('SELECT * FROM shopping_cart')


def start():
    for row in rows:
        timestamp = str('{:%Y-%b-%d--%H:%M:%S %Z}').format(row.last_update_timestamp)
        print(f"userid: {row.userid}; Item-count: {row.item_count}; changed at {timestamp}")


if __name__ == '__main__':
    start()
