(Optional) Configuring a Delay for Sending LLDP Alarms
======================================================

This section describes how to configure a delay for sending LLDP alarms, so that flapping of network topology caused by frequent LLDP alarms can be prevented.

#### Background Information

The delay for sending LLDP alarms should be appropriate. You can adjust this parameter based on the load of a network.

* The longer the delay, the lower the frequency of network topology changes on a device. However, if the delay for sending LLDP alarms is too long, the NMS cannot trace changes of the neighbor status. As a result, the NMS cannot refresh network topology for a device in a timely manner.
* The shorter the delay, the higher the frequency of network topology changes on a device. This helps the NMS refresh network topology on the device in a timely manner. However, if the delay is too short, the NMS refreshes status information about neighbors frequently. This causes flapping of network topology on a device, increases the load on the system, and wastes resources.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**lldp enable**](cmdqueryname=lldp+enable)
   
   
   
   The LLDP function is enabled globally.
3. Run [**lldp trap-interval**](cmdqueryname=lldp+trap-interval) *interval*
   
   
   
   A delay for sending LLDP alarms is configured.
   
   
   
   It is recommended that you use the default delay for sending LLDP alarms unless otherwise noted.