import time

from cassandra.cluster import Cluster

cluster = Cluster(['10.115.2.20'], port=8042)
session = cluster.connect('store', wait_for_all_pools=True)
session.execute('Use store')


def test():
    row_key_total = 10
    row_columns_total = 10

    cql = "insert into perf_data (row_key_id, row_columns) values (%s, %s)"
    row_columns = dict()
    for i in range(1, row_columns_total + 1):
        ck = f"column-key-{i}"
        cv = f"column-value{i}"
        row_columns.update({ck: cv})

    start = time.time()
    print("Start inserting data...")
    for i in range(1, row_key_total + 1):
        key = f"row-key-{i}"
        session.execute(cql, (key, row_columns))

    end = time.time()
    print(
        f'Values inserted: {row_key_total * row_columns_total};'
        f'Duration: {end - start} '
        f'throughput: {(row_key_total * row_columns_total) / (end - start)} Operations/s')


if __name__ == '__main__':
    test()
