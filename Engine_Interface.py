from os import stat
from flask import Flask, request, abort, Response
from flask_restful import Api, Resource
import time
import json

ITEM_ID_KEY = "item_ids"

app = Flask(__name__)
api = Api(app)
latency_log = []

def assemble_metrics():
    metrics = {'average_latency': sum(latency_log)/len(latency_log) if len(latency_log) > 0 else -1,
               'latencies': latency_log}
    return json.dumps(metrics)


class recommendation_Engine(Resource):
    def get(self):
        return {"response": "Hello World!"}

    def put(self):
        time_now = time.time()
        json_data = request.get_json()
        if ITEM_ID_KEY not in json_data.keys():
            abort(Response(f"Invalid json data, include {ITEM_ID_KEY} field", status=400))
        latency_log.append(time.time() - time_now)
        return json_data["item_ids"]


class recommendation_Engine_Ping(Resource):
    def get(self):
        return {"response": "Pong!"}


class recommendation_Engine_Metrics(Resource):
    def get(self):
        return assemble_metrics()


api.add_resource(recommendation_Engine, "/recsys/")
api.add_resource(recommendation_Engine_Ping, "/recsys/ping")
api.add_resource(recommendation_Engine_Metrics, "/recsys/metrics")


if __name__ == "__main__":
    app.run(debug=True)