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

## Task 1:

- Why additional element? Having multiple servers ensure that the website remains accessible even if one server fails. The load balancer optimizes resource utilization by distributing incoming requests among the servers.

- Load Balancer Distribution Algorithm? The Round Robin algorithm distributes incoming requests sequentially among the available servers in a cyclic manner.

- An Active-Active load balancer setup? all load balancers are actively distributing traffic at the same time for increased capacity and resilience, while in an Active-Passive setup, only one load balancer is actively handling traffic, and others become active only when the primary load balancer fails.

- Primary-Replica cluster? The Primary Database (Master) handles all write operations as the main authoritative source of data, while the Replica Databases (Slaves) are read-only copies that replicate data from the Primary and serve read operations to enhance performance and provide redundancy.

- The Primary node? in regard to the application handles all write operations and serves as the main authoritative source of data, while the Replica node is a read-only copy that replicates data from the Primary.

- Issues:
    - Single Point of Failure (SPOF): The lack of multiple load balancers.
    - Security issues (no firewall, no HTTPS): Our servers are at risk of unauthorized access without a firewall, and our servers is not secure or encrypted when HTTPS is not used.
    - No monitoring: Without monitoring, there is no way to proactively identify performance issues prolonging downtime in case of issues.

