from flask import Flask, jsonify, request, send_from_directory
import pyodbc

app = Flask(__name__)

# Database connection
server = 'LAPTOP-44KMOPHS\SQLEXPRESS2'
database = 'database'
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

#Starting endpoint
@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

# FetchData Endpoint to query the DB 
@app.route('/fetchData', methods=['GET'])
def fetch_data():
    query = request.args.get('query')  # Get the 'query' parameter from the URL

    if not query:
        return jsonify({"status": "error", "message": "No query provided"}), 400

    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # Execute the query
        cursor.execute(query)
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        data = [dict(zip(columns, row)) for row in rows]

        return jsonify({"status": "success", "data": data})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    finally:
        conn.close()


@app.route('/virtual-reality')
def virtual_reality():
    return send_from_directory('static', 'virtual-reality.html')


if __name__ == '__main__':
    app.run(debug=True)
