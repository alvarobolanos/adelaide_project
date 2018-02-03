# adelaide_project

OpenWeathermap connected forecast SMTP/TLS mailer

This is my first project and simply exemplifies the use of JSON formatted data pulled from the internet via the openweathermap api to create an emailed weather forecast to a list of clients in the (name, email) format read from a CSV file.

As it stands, the program has the following issues:

- UTC to X needs to be finished. It's not offering the appropriate conversion from UTC to the running system's Unix time (epoch).
