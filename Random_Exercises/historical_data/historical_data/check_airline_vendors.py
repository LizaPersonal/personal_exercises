import mysql.connector


def validate_airline_vendor(airline_in_file):
    connection = mysql.connector.connect(host='customerhistorical-vpc-enc.cvhe9o57xgm1.us-east-1.rds.amazonaws.com',
                                         user='readwrite',
                                         password='analyzerforwriter1234',
                                         database='historical')
    cursor = connection.cursor()

    query = "SELECT airline_code FROM airlines WHERE airline_fullname = %(Vendor *)s"
    update_query = "INSERT INTO airlines (airline_fullname, airline_code) VALUES (%(name)s, %(code)s)"

    cursor.execute(query, airline_in_file)
    results = cursor.fetchone()

    if results is None:
        missing_airline = airline_in_file['Vendor *']
        update_vendor_code = input(missing_airline + """ vendor does not exist yet, what should it be mapped to?
You can look it up here: http://www.iata.org/publications/Pages/code-search.aspx\n""")
        data = {'name': missing_airline, 'code': update_vendor_code}
        cursor.execute(update_query, data)
        print(update_vendor_code)
        return update_vendor_code
    else:
        # print(airline_in_file['Vendor *'] + ' ---> ' + str(results))
        return results

    cursor.close()
    connection.close()

validate_airline_vendor({'Vendor *': 'SwissAir'})


