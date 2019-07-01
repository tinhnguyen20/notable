# requirements

To run the code

```
	pip install -r requirements.txt

	python manage.py makemigrations
	python manage.py migrate
	python manage.py runserver

	python manage.py createsuperuser

```

After the server runs you can navigate to `http://localhost:8000/appointments/` for a list view of appointments.

at GET /appointments
	there is an option to pass physician_id, selected_date as cookies in order to filter by doctors/date

To access the django admin, login with
```
	username: tinhnguyen
	email: tinh@test.com
	password: password
```

The backend consists of 3 main models

```
	appointments
		-patient
		-physician
		-time (limited by 15 minute rule)
		-kind
	patients
	physicians
```

The main backend urls are 

```
 /appointments 
 /appointments/[appointment_id] 
 /patients
 /patients/[patient_id]
 /doctors
 /doctors/[doctor_id]
```

I've chosen to use the django rest framework for quick building of model related RESTful routes. This backend  supports all the functionalities described in the problem at the cost of needing to prepare correct json payloads according to the model definitions.

