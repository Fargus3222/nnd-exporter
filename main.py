from flask import Flask, Response
from prometheus_client import Gauge, generate_latest
import docker
import os

app = Flask(__name__)

client = docker.from_env()

container_id = os.getenv('CONTAINER_ID')

if not container_id:
    raise ValueError("Environment variable CONTAINER_ID is not set.")

last_log_line_gauge = Gauge('nnd_log_line', 'Last log line from nnd container', ['container_id', 'log_line'])

@app.route('/metrics')
def metrics():
    try:
        container = client.containers.get(container_id)
        logs = container.logs(tail=1).decode('utf-8').strip()

        last_log_line_gauge.labels(container_id=container_id, log_line=logs).set(1)

    except docker.errors.NotFound:
        return "Container not found", 404
    except Exception as e:
        return f"Error: {str(e)}", 500

    return Response(generate_latest(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
