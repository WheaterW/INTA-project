(Optional) Configuring a Device to Send a Trap Message to an NMS When an Interface Physical Status Changes
==========================================================================================================

You can enable a device to send a trap message to an NMS when the interface physical status changes. After this function is enabled, the NMS monitors the interface status in real time.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**enable snmp trap physical-updown**](cmdqueryname=enable+snmp+trap+physical-updown)
   
   
   
   The device is enabled to send a trap message to the NMS when the interface physical status changes.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.