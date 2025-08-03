Configuring a BOD Service Policy
================================

This section describes how to configure a BOD service policy.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) Run [**value-added-service bod portal-reserved**](cmdqueryname=value-added-service+bod+portal-reserved)
   
   
   
   The device is enabled to reserve portal services when BOD is deployed.
3. Run [**value-added-service policy**](cmdqueryname=value-added-service+policy) *service-policy-name* **bod**
   
   
   
   A BOD service policy is created, and its view is displayed.
4. Run [**accounting-scheme**](cmdqueryname=accounting-scheme) *scheme-name*
   
   
   
   An existing accounting scheme is configured for the BOD service policy.
5. Run [**qos-profile**](cmdqueryname=qos-profile) *qos-profile-name*
   
   
   
   A QoS profile is referenced in the BOD service policy.
   
   
   
   If both CAR and user-queue are configured in a QoS profile, you are advised to set the two CIRs to the same value.
6. (Optional) Run [**user-group**](cmdqueryname=user-group) *user-group-name*
   
   
   
   A user group is bound to the BOD service policy.
7. (Optional) Configure a Diameter monitor key for the BOD service policy based on the format of the monitor key delivered by the Diameter server.
   
   
   * Run the [**diameter monitor-key string**](cmdqueryname=diameter+monitor-key+string) *monitor-key-string* command to configure a Diameter monitor key in string format for the BOD service policy.
     
     Before running this command, run the [**diameter monitor-key parse-mode**](cmdqueryname=diameter+monitor-key+parse-mode) **string** command in the system view to set the parsing mode of the Diameter monitor key to string.
   * Run the [**diameter monitor-key**](cmdqueryname=diameter+monitor-key) *monitor-key* command to configure a Diameter monitor key in integer format for the BOD service policy.
     
     Before running this command, run the [**diameter monitor-key parse-mode**](cmdqueryname=diameter+monitor-key+parse-mode) **integer** command in the system view to set the parsing mode of the Diameter monitor key to integer.
8. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
9. (Optional) Run [**diameter gx attribute used-service-unit include cc-output-octets**](cmdqueryname=diameter+gx+attribute+used-service-unit+include+cc-output-octets)
   
   
   
   The device is enabled to report the downstream traffic of value-added services to the Diameter server.
10. (Optional) Run [**diameter monitor-key change support-type bod**](cmdqueryname=diameter+monitor-key+change+support-type+bod)
    
    
    
    The Gx interface is enabled to support changes of the Diameter monitor key in the BOD service policy. If the BOD service policy is subsequently replaced, the quota can be matched based on the monitor key in the new BOD service policy.
11. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.