Setting the Alarm Severity
==========================

You can change the default alarm severity.

#### Context

Alarm information is classified to enable users to roughly determine the alarm severity and take measures for prompt fault recovery. In this way, alarms of high severity are handled at a high priority, preventing service interruption.

According to X.733, alarms are classified into four severities, as shown in [Table 1](#EN-US_TASK_0172361216__tab_dc_vrp_logs_feature_210501). A smaller value indicates a higher severity.

**Table 1** Definition of alarm severities
| Value | Alarm Severity | Corresponding Trap Level | Description |
| --- | --- | --- | --- |
| 1 | Critical | Alert | Services have been affected, and an immediate rectification measure is required. |
| 2 | Major | Critical | Services are being affected, and an urgent rectification measure is required. |
| 3 | Minor | Error | A fault that does not yet affect services has occurred, and a rectification measure is required to prevent the fault from affecting services. |
| 4 | Warning | Warning | A potential fault that will affect services is detected. Actions should be taken to further diagnose the fault (if necessary) and rectify the fault before the fault grows in severity and affects services. |



#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**alarm**](cmdqueryname=alarm) command to enter the alarm management view.
3. Run the [**alarm-name**](cmdqueryname=alarm-name) *alarm-name* **severity** { **critical** | **major** | **minor** | **warning** } command to set the alarm severity.
   
   
   
   If you are concerned about certain types of alarms, you can set the highest severity for these types of alarms and configure filtering conditions. In this manner, the system reports only these types of alarms to the NMS.
4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.