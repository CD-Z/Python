from cassandra.cluster import Cluster

cluster = Cluster(['10.115.2.20'], port=8042)
session = cluster.connect('school', wait_for_all_pools=True)
session.execute('USE school')

rows = session.execute('SELECT * FROM student')


def start():
    for row in rows:
        print(f"userid: {row.userid}; User-Name: {row.name}; contact: {row.e_mails[0]}")
        print(f"                                       {row.e_mails[1]}")


if __name__ == '__main__':
    start()
