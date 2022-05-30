# DRF-CarRegister

Story: User can register/store Lithuanian car number plates, their owner names and car model to web application through API and application should asynchronously retrieve Car model image using Celery Framework, store it locally and display later on

## API endpoints
 
* `http://localhost:8000/api` - retrieve all cars 
* `http://localhost:8000/api/id` - GET car by id number
* `http://localhost:8000/api/create` - POST new car 
* `http://localhost:8000/api/id/delete` - DELETE car entry by id