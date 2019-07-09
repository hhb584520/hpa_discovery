#https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask

curl -i -H "Content-Type: application/json" -X GET http://localhost:5000/hpa
curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read a book"}' http://localhost:5000/hpa
curl -i -H "Content-Type: application/json" -X DELETE http://localhost:5000/hpa/2
