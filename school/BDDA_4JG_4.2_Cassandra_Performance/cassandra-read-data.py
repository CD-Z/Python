import time
import random
from cassandra.cluster import Cluster

cluster = Cluster(['10.115.2.20'], port=8042)
session = cluster.connect('store', wait_for_all_pools=True)
session.execute('Use store')


def test():     # Funktioniert nicht ohne ersichtlichen Grund
    row_key_total = 10
    row_columns_total = 10
    read_operations = 10
    debug = True
    start = time.time()

    print("Start reading data...")
    for i in range(1, read_operations + 1):
        random_row_key = random.randint(1, row_key_total)
        random_row_key_string = f"row-key-"+str(random_row_key)
        random_column_key = random.randint(1, row_columns_total)
        random_column_key_string = f"column-key-"+str(random_column_key)
        print(f"row-key-{random_row_key}")
        column_value = session.execute("SELECT row_columns as column_value from store.Perf_data"+
                                       " where row_key_id = '"+random_row_key_string+"' "+
                                       "and row_columns contains key '"+random_column_key_string+"' allow filtering")
        if not column_value.current_rows:
            print(f"Error: no value found for row-key "
                  f"{random_row_key} column-key {random_column_key} column value {column_value}")

        for row in column_value:
            print("Row: "+str(row.column_value[random_column_key]))
            if row.column_value != f'column-value-{random_column_key}':
                print(f"Error: value from database does not match "
                      f"for row-key {random_row_key} column-key {random_column_key}")
            if debug:
                print(f"row-key: {random_row_key} / "
                      f"column-key: {random_column_key} / "
                      f"column-value: column-value-{random_column_key}")
            if i % 1000 == 0:
                print(f"Read operations executed: {i}, elapsed time: {round(time.time() - start, 2)}")

    end = time.time()
    print(f"Read operations: {read_operations}, "
          f"duration: {round(end - start, 2)}")


if __name__ == '__main__':
    test()
