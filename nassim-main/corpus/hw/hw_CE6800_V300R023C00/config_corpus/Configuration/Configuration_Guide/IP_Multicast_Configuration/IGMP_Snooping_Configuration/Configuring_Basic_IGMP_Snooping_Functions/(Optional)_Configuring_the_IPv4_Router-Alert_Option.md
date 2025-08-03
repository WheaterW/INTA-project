(Optional) Configuring the IPv4 Router-Alert Option
===================================================

(Optional) Configuring the IPv4 Router-Alert Option

#### Context

Generally, an IGMP message is sent to and processed by the routing protocol layer only if the message is destined for the IP address of a local interface. Router-Alert is a special mechanism for identifying protocol messages. If a message contains the Router-Alert option, it needs to be sent to the routing protocol layer for processing.

For compatibility purposes, a device does not check the Router-Alert option by default. When receiving an IGMP message, it sends the message to the upper-layer protocol for processing, regardless of whether the message carries the Router-Alert option in the IP header. To improve system performance, reduce costs, and improve protocol security, you can configure the device to check the Router-Alert option in IGMP messages. This ensures that the device discards the IGMP messages that do not carry the option.

By default, the device adds the Router-Alert option to IGMP messages before sending them.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VLAN view.
   
   
   ```
   [vlan](cmdqueryname=vlan) vlan-id
   ```
3. Configure the device to check the Router-Alert option in received IGMP messages.
   
   
   ```
   [igmp snooping require-router-alert](cmdqueryname=igmp+snooping+require-router-alert)
   ```
4. Configure the device to add the Router-Alert option to sent IGMP messages.
   
   
   ```
   [undo igmp snooping send-router-alert disable](cmdqueryname=undo+igmp+snooping+send-router-alert+disable)
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```