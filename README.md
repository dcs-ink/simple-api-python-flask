https://dev.to/dcs_ink/create-a-simple-api-with-python-and-flask-2b80

This was a simple api I built using python and flask. I used it for learning with my data requested from indeed. There is sample data in the json.

Steps to make it work.
After setup and activating a virtual environment...
1. `pip install flask`
2. `pip install jsonify`
3. Create python file and paste above python code
4. Create json file and paste above json code
5. Run python script

```
sudo python3 job_api.py
```

6. Use curl to test

```
curl http://127.0.0.1:8080/api/jobs
```
```
[
    {
        "company": "CoolCompany",
        "date": "date timestamp",
        "location": "Cool City, COOL",
        "title": "Job Title"
    }
]
```
