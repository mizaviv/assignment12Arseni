import mysql.connector

DEFAULT_PORT = 3307


def interact_db(query, query_type: str, query_params=None):
    return_value = False
    column_names = None
    connection = mysql.connector.connect(host='localhost',
                                         port=DEFAULT_PORT,
                                         user='root',
                                         passwd='root',
                                         database='users')

    if query_params == None:
        cursor = connection.cursor(named_tuple=True)
        cursor.execute(query)
    else:
        cursor = connection.cursor(prepared=True)
        cursor.execute(query, query_params)
    #
    if query_type == 'commit':
        connection.commit()
        return_value = True

    if query_type == 'fetchone':
        column_names = cursor.column_names
        query_result = cursor.fetchone()
        return_value = query_result

    cursor.close()
    connection.close()
    if column_names != None: # used for fetch
        return [column_names, return_value]
    else:
        return return_value

def json_query(query, query_params=None):
    result = {}
    query_result = interact_db(query, "fetchone", query_params)
    # build the object from user columns names + data
    if len(query_result) == 2 and query_result[1] != None: # cursor with columns-names & data
        result_names = list(map(lambda row: row, query_result[0]))
        result_values = list(map(lambda row: row, query_result[1]))

        j = 0
        for i in result_names:
            result[result_names[j]] = result_values[j]
            j = j + 1

    return  result