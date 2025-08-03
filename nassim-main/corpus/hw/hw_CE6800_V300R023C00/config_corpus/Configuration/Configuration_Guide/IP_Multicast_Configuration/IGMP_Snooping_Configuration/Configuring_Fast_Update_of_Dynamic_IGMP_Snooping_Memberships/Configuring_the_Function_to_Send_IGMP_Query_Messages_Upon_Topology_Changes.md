Configuring the Function to Send IGMP Query Messages Upon Topology Changes
==========================================================================

Configuring the Function to Send IGMP Query Messages Upon Topology Changes

#### Context

When a Layer 2 network topology changes, multicast forwarding paths may also change. You can configure a device to proactively send IGMP Query messages if a fault occurs on a link. After receiving IGMP Report messages from multicast group members, the device can update the member port information based on the Report messages and quickly switch multicast data traffic to new forwarding paths.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure the device to send IGMP General Query messages upon topology changes.
   
   
   ```
   [igmp snooping send-query enable](cmdqueryname=igmp+snooping+send-query+enable)
   ```
   
   
   
   By default, the device does not send IGMP General Query messages upon topology changes.
   
   After this command is run, the device proactively sends IGMP General Query messages (the default source IP address is 192.168.0.1) upon topology changes. This ensures that the port information can be updated quickly, thereby minimizing the period of interruption for forwarding multicast data to downstream members.
3. Configure a source IP address for IGMP General Query messages.
   
   
   ```
   [igmp snooping send-query source-address](cmdqueryname=igmp+snooping+send-query+source-address) ip-source-address
   ```
   
   By default, the source IP address is 192.168.0.1 in the General Query messages sent upon topology changes. Run this command if you want to specify a different IP address. If the [**igmp-snooping send-query source-address**](cmdqueryname=igmp-snooping+send-query+source-address) command is executed in both the system view and VLAN view, the configuration in the VLAN view is used.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```