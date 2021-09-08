from flask import jsonify,send_file
from flask_restful import Resource
# import config

# ----- Command to run the class methods from command line --------
# (venv) ubuntu@laptop:~/FILE_PATH$ python Square.py 
# ===GET Request Method=== Square === 8
# (venv) ubuntu@laptop:~/FILE_PATH$ 
# -------------------------------------------------------------------


class Square(Resource): 

    def __init__(self):
        pass

    def get(self): 
        # print("\n===GET Request Method=== Square ===", str(num))
        # filename_server1 = "/var/www/html/gpxfile.gpx"
        return {'msg': 'Hello World'}

        # return {'square': num*num}
        # return send_file('/var/www/html/gpxfile.gpx',
        #              mimetype='text',
        #              attachment_filename='gpxfile.gpx',
        #              as_attachment=True)
        

    # Corresponds to POST request 
    def post(self):   
        # data = request.get_json()     # status code 
        # return jsonify({'data': data}), 201
        pass


#if __name__ == '__main__':
#    square = Square()
#    square.get(8)
