(Optional) Configuring Alarm Generation and Clearance Thresholds for SSH Server Login Failures
==============================================================================================

This section describes how to configure alarm generation and clearance thresholds for SSH server login failures within a specified period. This configuration facilitates user login management.

#### Context

When the number of SSH server login failures within a specified period exceeds the threshold, an alarm is generated and displayed for an administrator to promptly handle the associated event.

Perform the following steps on a device that functions as an SSH server:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ssh server login-failed threshold-alarm**](cmdqueryname=ssh+server+login-failed+threshold-alarm) **upper-limit** *report-times* **lower-limit** *resume-times* **period** *period-time*
   
   
   
   Alarm generation and clearance thresholds for SSH server login failures within a specified period are configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The alarm generation threshold specified using *report-times* must be greater than or equal to the alarm clearance threshold specified using *resume-times*.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.