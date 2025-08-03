Configuring the Function to Send IGMP Query Messages Upon Network Topology Changes
==================================================================================

Configuring the Function to Send IGMP Query Messages Upon Network Topology Changes

#### Context

When a Layer 2 network topology changes, multicast forwarding paths may also change. You can configure a device to proactively send IGMP Query messages if a fault occurs on a link. After receiving IGMP Report messages from multicast group members, the device can update the member port information based on the Report messages and quickly switch multicast data traffic to new forwarding paths.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure the function to send IGMP Query messages upon network topology changes.
   
   
   ```
   [igmp snooping send-query enable](cmdqueryname=igmp+snooping+send-query+enable)
   ```
   
   
   
   After this command is run, the device proactively sends IGMP General Query messages to update port information when detecting changes in a Layer 2 network topology. In this manner, multicast traffic can be rapidly switched to new forwarding paths, ensuring nonstop forwarding of multicast services.
3. (Optional) Set the source IP address of IGMP Query messages sent by the device.
   
   
   ```
   [igmp snooping send-query source-address](cmdqueryname=igmp+snooping+send-query+source-address) ip-source-address
   ```
   
   
   
   By default, the source address of IGMP Query messages is 192.168.0.1. If this address is already in use on the network, use this command to set a different address.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```