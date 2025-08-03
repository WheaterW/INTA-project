(Optional) Setting the Time During Which the EFM OAM Status of an Interface Remains Down
========================================================================================

After EFM OAM is associated with an interface, you can adjust the delay in changing the EFM OAM status of an interface from Down to Up by setting the time during which the EFM OAM status of the interface remains Down, if a link connectivity fault is rectified.

#### Pre-configuration Tasks

Before setting the time during which the EFM OAM status of an interface remains Down, [associate EFM OAM with the interface](dc_vrp_efm_cfg_2030.html).


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the interface at one end of a link is displayed.
3. Run [**efm holdup-timer**](cmdqueryname=efm+holdup-timer) *time*
   
   
   
   The time during which the EFM OAM status of the interface remains Down is set.
   
   
   
   If the parameter *time* is not specified, the EFM OAM status of an interface immediately changes from down to up when a link connectivity fault is rectified. If the parameter is specified, the EFM OAM status of an interface changes from down to up only when a link connectivity fault is rectified and after the time specified by the parameter *time* elapses. Setting the parameter can reduce link flapping. You can run the [**recover efm-down**](cmdqueryname=recover+efm-down) command to change the EFM OAM status of an interface from down to up.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.