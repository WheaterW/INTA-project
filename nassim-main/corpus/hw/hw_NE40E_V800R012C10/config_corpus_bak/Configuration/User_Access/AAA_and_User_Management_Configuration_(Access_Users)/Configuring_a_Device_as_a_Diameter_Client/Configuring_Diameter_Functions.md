Configuring Diameter Functions
==============================

Configuring_Diameter_Functions

#### Context

Enabling Diameter functions is a prerequisite for configuring a Diameter server. After Diameter is enabled, you can also configure some optional Diameter functions, such as the format of the subscription-id attribute to be sent to the Diameter server, number of retransmissions of detection packets, and number of retransmissions of CCR-I messages.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**diameter enable**](cmdqueryname=diameter+enable)
   
   
   
   The Router is configured to interwork with the Diameter server.
3. (Optional) Run [**diameter subscription-id include**](cmdqueryname=diameter+subscription-id+include) { **mac-address** { *macaddr\_separator* | **noseparator** } [ *subscription-separator* ] | **username** [ *subscription-separator* ] | **circuit-id** [ *subscription-separator* ] } \*
   
   
   
   The format of the subscription-id attribute to be sent to the Diameter server is configured.
4. (Optional) Run [**diameter-dwr**](cmdqueryname=diameter-dwr) { **retransmit** *retry-times* | **timeout** *second* } \*
   
   
   
   The number of retransmissions of device watchdog request (DWR) packets and a detection timeout period are configured.
5. (Optional) Run [**diameter gx event-trigger version**](cmdqueryname=diameter+gx+event-trigger+version) { **r940** | **r970** }
   
   
   
   The value of USAGE-REPORT in Event-Trigger is modified.
6. (Optional) Run [**diameter monitor-key parse-mode**](cmdqueryname=diameter+monitor-key+parse-mode) { **integer** | **string** }
   
   
   
   A parsing mode is configured for the Diameter monitoring key.
7. (Optional) Run [**diameter gx ccri retransmit**](cmdqueryname=diameter+gx+ccri+retransmit) *retry-times*
   
   
   
   The number of times that the device retransmits CCR-I messages to the Diameter server is configured when the Diameter server does not receive CCR-I messages or the device discards CCR-I messages returned by the Diameter server. This command can be used together with the [**diameter gx ccri retransmit round**](cmdqueryname=diameter+gx+ccri+retransmit+round) *round-num* **round-timeout** *timeout-num* command to configure the number of CCR-I message retransmission rounds and the retransmission interval of each round.
8. (Optional) Run [**diameter gx event-trigger ignore usage-report**](cmdqueryname=diameter+gx+event-trigger+ignore+usage-report)
   
   
   
   The device is enabled to identify the quotas delivered by the Diameter server through CCR-I, CCR-U, or RAR messages even if the Event-Trigger AVP of USAGE\_REPORT is not delivered.
9. (Optional) Run [**diameter daa volume-quota total**](cmdqueryname=diameter+daa+volume-quota+total) { **send** | [**receive**](cmdqueryname=receive) }
   
   
   
   The device is configured to process the traffic quota delivered by the Diameter server or the traffic usage sent to the Diameter server in total mode.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.