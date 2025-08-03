(Optional) Configuring the IPv6 Router-Alert Option
===================================================

(Optional) Configuring the IPv6 Router-Alert Option

#### Context

Generally, an MLD message is sent to the routing protocol layer for processing only if the message is destined for the IP address of a local interface. IPv6 Router-Alert is a special mechanism for identifying protocol messages. If a message contains the IPv6 Router-Alert option, it needs to be sent to the routing protocol layer for processing.

To ensure compatibility, the device does not check the IPv6 Router-Alert option by default. That is, when receiving MLD messages, the device sends them to the upper-layer protocol for processing, regardless of whether the IP headers of the messages contain the IPv6 Router-Alert option. To improve system performance, reduce costs, and improve protocol security, you can configure the device to check the IPv6 Router-Alert option in received MLD messages. This ensures that the device discards the MLD messages that do not carry the option.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VLAN view.
   
   
   ```
   [vlan](cmdqueryname=vlan) vlan-id
   ```
3. Configure the device to check the Router-Alert option in received MLD messages.
   
   
   ```
   [mld snooping require-router-alert](cmdqueryname=mld+snooping+require-router-alert)
   ```
   
   By default, the MLD messages accepted by a device from a VLAN do not need to contain the Router-Alert option in the IP header.
4. Configure the device to add the Router-Alert option to the MLD messages to be sent.
   
   
   ```
   [undo mld snooping send-router-alert disable](cmdqueryname=undo+mld+snooping+send-router-alert+disable)
   ```
   
   By default, the device adds the Router-Alert option to MLD messages before sending them.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```