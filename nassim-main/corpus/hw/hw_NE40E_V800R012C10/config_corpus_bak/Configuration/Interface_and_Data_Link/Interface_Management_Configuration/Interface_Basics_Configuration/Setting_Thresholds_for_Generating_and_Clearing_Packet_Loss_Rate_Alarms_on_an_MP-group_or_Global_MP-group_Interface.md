Setting Thresholds for Generating and Clearing Packet Loss Rate Alarms on an MP-group or Global MP-group Interface
==================================================================================================================

To allow the device to generate and clear packet loss rate alarms on an MP-group or global MP-group interface, set packet loss alarm thresholds.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This configuration is not supported only on the NE40E-M2K-B.

When an interface discards packets frequently, the link is in the poor condition, affecting service transmission. If you want to monitor the link quality, set thresholds for generating and clearing packet loss rate alarms on the MP-group interface or global MP-group interface.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The interface view is displayed.
   
   
   
   MP-group and global MP-group interfaces are supported.
3. Run [**trap-threshold mp-lospkt-exc**](cmdqueryname=trap-threshold+mp-lospkt-exc) **trigger-threshold** *coefficient-value* *power-value* [ **resume-threshold** *resume-coefficient-value* *resume-power-value* ]
   
   
   
   The thresholds for generating and clearing packet loss rate alarms are set.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.