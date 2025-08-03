Configuring an Alarm Threshold for Sudden Traffic Rate Decrease on an Interface
===============================================================================

To allow a device to detect real-time traffic rate changes on an interface, you can configure the device to generate an alarm when the traffic rate change (%) on the interface exceeds a specified threshold (*ratio-threshold*) while the bandwidth usage (%) is not below the set lower threshold (*bandwidth-usage-threshold*). Traffic rate change on an interface (%) = (Interface rate in the current traffic statistics collection interval â Interface rate in the previous traffic statistics collection interval)/Interface rate in the previous traffic statistics collection interval

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number* 
   
   
   
   The view of the Ethernet interface on which the alarm threshold for sudden traffic rate decrease needs to be set is displayed.
3. Run [**flow-change fall start-check bandwidth-ratio**](cmdqueryname=flow-change+fall+start-check+bandwidth-ratio) *bandwidth-ratio-threshold*
   
   
   
   The lower bandwidth usage threshold (%) for triggering sudden traffic rate decrease alarms is set.
4. Run [**flow-change fall**](cmdqueryname=flow-change+fall) { **input-threshold-ratio** | **output-threshold-ratio** } **ratio-threshold**
   
   
   
   An alarm threshold for sudden traffic rate decrease is set on the interface.
5. (Optional) Run [**flow-change fall interval**](cmdqueryname=flow-change+interval) *interval-value*
   
   
   
   The interval for collecting sudden traffic rate decrease statistics is set on the interface.
6. (Optional) Run [**flow-change fall disable**](cmdqueryname=flow-change+fall+disable)
   
   
   
   Detection of sudden traffic rate decrease is disabled on the interface.
7. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
8. (Optional) Run [**flow-change fall remain-time**](cmdqueryname=flow-change+fall+remain-time) *interval*
   
   
   
   An alarm clearance period is set.
9. (Optional) Run [**reset flow-change fall**](cmdqueryname=reset+flow-change+fall) **interface** *interface-type interface-number*
   
   
   
   Traffic rate detection is reset on the interface.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.