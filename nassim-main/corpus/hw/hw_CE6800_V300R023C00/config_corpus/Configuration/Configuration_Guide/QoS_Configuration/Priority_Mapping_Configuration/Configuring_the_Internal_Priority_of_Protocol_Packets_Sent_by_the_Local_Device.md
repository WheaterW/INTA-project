Configuring the Internal Priority of Protocol Packets Sent by the Local Device
==============================================================================

Configuring the Internal Priority of Protocol Packets Sent by the Local Device

#### Context

A device processes packets based on their internal priorities. You can change the internal priority of protocol packets sent by the local device to preferentially process packets with a high internal priority on the local device.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure the internal priority of protocol packets sent by the local device.
   
   
   ```
   [set priority traffic-class](cmdqueryname=set+priority+traffic-class) traffic-class-value
   ```
   
   
   
   By default, the internal priority is not configured for protocol packets sent by the local device, and the local device sends all protocol packets based on their original internal priorities.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```