# 0x18. Webstack monitoring.
## General
Why is monitoring needed
What are the 2 main area of monitoring
What are access logs for a web server (such as Nginx)
What are error logs for a web server (such as Nginx)
## Tasks.
0. 0. Sign up for Datadog and install datadog-agent
mandatory
Score: 0.0% (Checks completed: 0.0%)
For this task head to https://www.datadoghq.com/ and sign up for a free Datadog account. When signing up, youll have the option of selecting statistics from your current stack that Datadog can monitor for you. Once you have an account set up, follow the instructions given on the website to install the Datadog agent.



Sign up for Datadog - Please make sure you are using the US website of Datagog (.com)
Install datadog-agent on web-01
Create an application key
Copy-paste in your Intranet user profile (here) your DataDog API key and your DataDog application key.
Your server web-01 should be visible in Datadog under the host name XX-web-01
You can validate it by using this API
If needed, you will need to update the hostname of your server
1. Among the litany of data your monitoring service can report to you are system metrics. You can use these metrics to determine statistics such as reads/writes per second, which can help your company determine if/how they should scale. Set up some monitors within the Datadog dashboard to monitor and alert you of a few. You can read about the various system metrics that you can monitor here: System Check.

2. Now create a dashboard with different metrics displayed in order to get a few different visualizations.

Create a new dashboard
Add at least 4 widgets to your dashboard. They can be of any type and monitor whatever youd like
Create the answer file 2-setup_datadog which has the dashboard_id on the first line. Note: in order to get the id of your dashboard, you may need to use Datadogs API
### End.
