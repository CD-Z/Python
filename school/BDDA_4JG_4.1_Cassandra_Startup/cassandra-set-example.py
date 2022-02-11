from cassandra.cluster import Cluster

cluster = Cluster(['10.115.2.20'], port=8042)
session = cluster.connect('store', wait_for_all_pools=True)
session.execute('USE store')

rows = session.execute('SELECT * FROM student')


def start():
    for row in rows:
        print(f"userid: {row.userid}; Item-count: {row.name}; contact: {row.emails[0]}")
        print(f"                                        {row.emails[1]}")


if __name__ == '__main__':
    start()
