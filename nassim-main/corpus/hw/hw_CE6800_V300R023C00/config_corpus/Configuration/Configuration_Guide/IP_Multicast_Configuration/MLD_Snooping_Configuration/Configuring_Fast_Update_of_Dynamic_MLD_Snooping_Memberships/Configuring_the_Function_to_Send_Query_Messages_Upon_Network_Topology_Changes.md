Configuring the Function to Send Query Messages Upon Network Topology Changes
=============================================================================

Configuring the Function to Send Query Messages Upon Network Topology Changes

#### Context

When a Layer 2 network topology changes, multicast forwarding paths may also change. You can configure a device to proactively send MLD Query messages if a fault occurs on a link. After receiving MLD Report messages from multicast group members, the device can update the member port information based on the Report messages and quickly switch multicast data traffic to new forwarding paths.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure the device to send MLD General Query messages upon network topology changes.
   
   
   ```
   [mld snooping send-query enable](cmdqueryname=mld+snooping+send-query+enable)
   ```
   
   
   
   By default, the device does not send MLD General Query messages upon network topology changes. After this command is run, the device proactively sends MLD General Query messages upon topology changes. This ensures that the port information can be updated quickly, thereby minimizing the period of interruption for forwarding multicast data to downstream members.
3. Configure a source IP address for MLD General Query messages.
   
   
   ```
   [mld snooping send-query source-address](cmdqueryname=mld+snooping+send-query+source-address) ip-address
   ```
   
   By default, the source address of General Query messages sent by the device upon topology changes is a link-local address, that is, an IPv6 address starting with FE80::. If this address is already in use on the network, use this command to set a different address.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```