# 0x19. Postmortem
Date: October 15, 2022 Duration: 7 hours 30 minutes.
## Summary:
On October 15, 2022, Our web based Open specimen system suddenly went down. The postmortem report provides detailed summary of series of events that followed resulting to cause of action and subsequent rectification.
## Timeline:
	9:00 AM - Incident identified and reported.
	9:35 AM - Investigation initiated.
	10:15 AM - Root cause identified.
	12:30 AM - Mitigation efforts initiated.
	04:30 PM - System restored and services resumed.
## Root Cause:
The root cause of outage was discovered to be expired SSL certificate that rendered SSL termination in our load balancer impossible and therefore the destination server unreachable.
## Impact:
This disruption lead to a number of impacts:
1. Inability to reach the database hosting server for monitoring of perfomance and logs.
2. Disrupted data entry of collected data into the system and a subsequent halt in data and sample collection activities due to uncertainity in recovery timeline.
3. Delayed data cleaning and reports.
## Mitigation and Recovery:
Upon identification of the root cause of the outage, the following steps were undertaken:
1. Instant requisition was placed to facilitate purchase of new SSL certificate license.
2. Installation of the newly purchased license into our Load balancer  to restore SSL termination services.
3. Incompartibility issues rose resulting in purchasing of another license and subsequent installaction that this time was successful after a series of tests that lasted some times to validate stability.
4. SSL certificate expiration date monitor was installed to alert the server administrators in the event the certificates were due to expire. This alerts would be synchronized to the admins' emails.
