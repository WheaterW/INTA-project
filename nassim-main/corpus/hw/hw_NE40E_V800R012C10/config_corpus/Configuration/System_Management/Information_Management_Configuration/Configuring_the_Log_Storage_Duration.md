Configuring the Log Storage Duration
====================================

Configuring the Log Storage Duration

#### Usage Scenario

After the log storage duration is configured, expired logs are not deleted immediately. They are deleted only after the configured storage duration expires.


#### Pre-configuration Tasks

Before configuring the log storage duration, ensure that the device is powered on correctly and the self-test is successful.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**info-center log-storage-time**](cmdqueryname=info-center+log-storage-time) *day-value*
   
   
   
   The log storage duration is configured.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.