# Web infrastructure design

## Task 0

A simple web infrastructure that hosts the website reachable via www.foobar.com using a single server.

- What is a server?
A server is a specialized computer system or software program that provides services, resources, or functionality to other devices or programs (clients) in a networked environment.

- What is the role of the domain name?
A domain name serves as a human-readable identifier that allows users to access websites and services on the internet without the need to remember complex IP addresses.

-  What type of DNS record is www in www.foobar.com?
The DNS record type for "www" in the domain "www.foobar.com" a "CNAME" record.

- What is the role of the web server?
The web server plays a central role in delivering web content and services to users by handling HTTP requests and serving web pages and resources.

- What is the role of the application server?
The application server handles dynamic aspects of web applications.

- What is the role of the database?
The database provides structured storage for managing and persisting data used by web applications.

- What is the server using to communicate with the user's computer?
The server uses the Hypertext Transfer Protocol (HTTP) to communicate with the user's computer.

- Issues with the single server infrastructure:
    - Single Point of Failure (SPOF) can cause downtime if the server fails.
    - Downtime during maintenance or updates when the web server needs to be restarted.
    -  Limited scalability, unable to handle high traffic demands.

