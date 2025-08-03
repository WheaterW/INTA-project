(Optional) Configuring an Alarm Threshold for the Number of LSAs Learned by OSPF
================================================================================

You can configure an alarm threshold for the number of LSAs learned by OSPF so that an alarm is reported when this threshold is reached or exceeded.

#### Context

If the number of external routes that OSPF imports and advertises exceeds the routing table capacity of a device, the device may restart unexpectedly. To prevent this problem and ensure that the device runs properly, you can set an alarm threshold for the number of LSAs learned by OSPF and enable overload control.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
   
   
   
   The OSPF view is displayed.
3. Run [**maximum received-lsa threshold**](cmdqueryname=maximum+received-lsa+threshold) *value* [ **overload-limit** ]
   
   
   
   An alarm threshold is configured for the number of LSAs learned by OSPF. You can determine whether to enable overload control as required.
   
   
   
   * If an alarm threshold is configured but overload control is not, only an alarm is reported when this threshold is reached or exceeded.
   * If both an alarm threshold and overload control are configured, an alarm is reported when this threshold is reached or exceeded. In addition, OSPF no longer learns new LSAs when the following conditions are met:
     + The number of LSAs learned by OSPF reaches or exceeds the alarm threshold.
     + The memory is in the danger state, and the memory used by the OSPF LSDB component ranks in the top 3.
     + The [**ospf memory-overload control**](cmdqueryname=ospf+memory-overload+control) command configuration exists (the corresponding function is enabled by default).
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.