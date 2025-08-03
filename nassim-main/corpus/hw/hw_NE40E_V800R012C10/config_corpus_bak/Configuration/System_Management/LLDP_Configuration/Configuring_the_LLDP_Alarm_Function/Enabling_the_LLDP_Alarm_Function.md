Enabling the LLDP Alarm Function
================================

This section describes how to enable the LLDP alarm function, so that a device can send alarms to the NMS when information about neighbors changes.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**snmp-agent trap enable feature-name**](cmdqueryname=snmp-agent+trap+enable+feature-name) **lldp** [ **trap-name** **lldpremtableschange** ]
   
   
   
   The LLDP alarm function is enabled.
   
   
   
   After the LLDP alarm function is enabled for a device, the device sends alarms to the NMS when one of the following events occurs.
   
   The LLDP alarm function takes effect globally to control the capability to send LLDP alarms on all interfaces on a device.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The network topology changes frequently when the networking is first formed. After the LLDP alarm function is enabled for a device, the device will frequently send alarms to the NMS. This increases the load on the system and wastes resources. It is recommended that you disable the LLDP alarm function when the networking is first formed.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.