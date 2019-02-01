This project is about a web/app server that need to execute a process into a cron job, but the request of elastic beanstalk is that the site was stateful
thats why we execute a lambda with a CloudWhats event.

The requirements:
- A lambda function that execute a curl command, in python.
- Filter the execution (security)

Lambda Function:

We send the execution to the server using a POST request, this is because the URL is encoded. We encoded the URL with a string of (name, value) pairs.

- The body of the HTTP message sent to the server is a query string:
> Content-Type: application/x-www-form-urlencoded
> URL Encoded Form: /urlencoded?firstname=sid

- We include the headers to filter the petitions in the application server:
> -H key:Value

.ebextensions:

We need to configure apache to filter the request process, and only accept the request from lambda
