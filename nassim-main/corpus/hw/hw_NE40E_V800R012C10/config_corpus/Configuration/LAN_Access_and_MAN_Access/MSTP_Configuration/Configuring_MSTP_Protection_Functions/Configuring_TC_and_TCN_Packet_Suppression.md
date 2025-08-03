Configuring TC/TCN Packet Suppression
=====================================

If TC/TCN packets do not need to be flooded, you can enable TC/TCN packet suppression.

#### Context

If TC/TCN packet suppression is enabled, after a device interface receives TC/TCN packets, it neither updates local ARP or MAC entries nor floods the packets to other interfaces on the device.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The interface view is displayed.
3. Run [**stp tc-restriction enable**](cmdqueryname=stp+tc-restriction+enable)
   
   
   
   TC/TCN packet suppression is enabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.