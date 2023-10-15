##Postmortem

#Issue Summary:

Duration of the Outage: October 9, 2023, 14:00 - 14:30 UTC
Impact: The Nginx web server was not listening on port 80, causing service unavailability. Approximately 100% of users were affected, as all requests to the web server were failing.
Root Cause:
The root cause of the issue was a misconfiguration in the Nginx server settings that prevented it from properly binding to port 80.

#Timeline:

Issue Detected: October 9, 2023, 14:00 UTC
The issue was detected when users started reporting that they were unable to access the website hosted on the server.
Actions Taken:
Initial investigation revealed that the Nginx server was not listening on port 80.
Checked the Nginx configuration files in /etc/nginx/ to ensure that port 80 was correctly specified.
Ran the command netstat -tuln to verify that Nginx was not listening on port 80.

#Misleading Investigation Paths:
Initially, we suspected that the issue might be related to a recent server update, but this was not the case.
There was also a brief consideration of a firewall issue, but this was ruled out as port 80 was not being blocked.
#Escalation:
The incident was escalated to the server administrator and the web development team.
Incident Resolution:
The issue was resolved by correcting the Nginx configuration settings.

#Root Cause and Resolution:
The root cause was identified as a misconfiguration in the Nginx server settings. Specifically, the configuration file /etc/nginx/sites-available/default had an incorrect configuration for the listen directive. It was configured to listen on port 8080 instead of port 80. This misconfiguration prevented Nginx from binding to port 80, causing the service outage.

To resolve the issue, the following steps were taken:

Edited the Nginx configuration file using the command  vi /etc/nginx/sites-available/default.
Corrected the listen directive to specify port 80 instead of 8080.
Saved the configuration file and exited the text editor.
Reloaded Nginx configuration using the command sudo systemctl reload nginx.
After these steps, Nginx started listening on port 80, and the website became accessible to users again.

Corrective and Preventative Measures:
To prevent similar issues in the future, the following measures will be implemented:

Regular configuration reviews: Scheduled reviews of server configurations to catch potential misconfigurations before they impact services.
Version control for configuration files: Storing Nginx configuration files in a version control system to track changes and facilitate easy rollback in case of issues.
Automated testing: Implementing automated tests that validate server configuration after updates or changes.
Monitoring and alerting: Setting up monitoring and alerting systems to promptly detect and notify administrators of service disruptions.
Documentation: Maintaining up-to-date documentation of server configurations and procedures for troubleshooting common issues.

#Conclusion:
The Nginx port 80 issue was resolved by correcting a misconfiguration in the Nginx server settings. This incident highlighted the importance of regular configuration reviews and the need for monitoring and automation to detect and prevent similar issues in the future.

