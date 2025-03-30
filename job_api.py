import json
from flask import Flask, jsonify

app = Flask(__name__)

jobs_data = []
try:
    with open('jobs.json', 'r') as f:
        jobs_data = json.load(f)
    print(f"Successfully loaded {len(jobs_data)} jobs from jobs.json")
except FileNotFoundError:
    print("Error: jobs.json not found!")
except json.JSONDecodeError:
    print("Error: jobs.json is not valid JSON!")

@app.route('/api/jobs', methods=['GET'])
def get_all_jobs():
    return jsonify(jobs_data)

@app.route('/api/jobs/titles', methods=['GET'])
def get_job_titles():
    titles = [job['title'] for job in jobs_data]
    return jsonify(titles)

@app.route('/api/jobs/companies', methods=['GET'])
def get_job_companies():
    if not jobs_data:
        return jsonify({"error": "No job data available"}), 500
    companies = list(set(job.get('company', 'N/A') for job in jobs_data))
    return jsonify(companies)

@app.route('/api/jobs/location', methods=['GET'])
def get_job_locations():
    if not jobs_data:
        return jsonify({"error": "No job data available"}), 500
    locations = list(set(job.get('location') for job in jobs_data))
    return jsonify(locations)

@app.route('/api/jobs/content', methods=['GET'])
def get_job_content():
    if not jobs_data:
        return jsonify({"error": "No job data available"}), 500
    urls = list(set(job.get('content', 'N/A') for job in jobs_data))
    return jsonify(urls)

if __name__ == '__main__':
    app.run(debug=True, port=8080)

