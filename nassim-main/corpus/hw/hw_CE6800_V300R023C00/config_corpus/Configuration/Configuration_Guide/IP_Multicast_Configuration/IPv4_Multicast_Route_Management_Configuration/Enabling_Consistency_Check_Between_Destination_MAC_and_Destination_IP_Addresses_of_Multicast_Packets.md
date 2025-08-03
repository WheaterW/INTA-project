Enabling Consistency Check Between Destination MAC and Destination IP Addresses of Multicast Packets
====================================================================================================

Enabling Consistency Check Between Destination MAC and Destination IP Addresses of Multicast Packets

#### Context

For each multicast packet, there is a mapping between the destination MAC and destination IP addresses. The last 23 bits of these addresses must be consistent. After the function of checking the consistency between these addresses is enabled, the device discards the packet if the last 23 bits are inconsistent.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable consistency check between destination MAC and destination IP addresses of multicast packets.
   
   
   ```
   [multicast mac-ip-check enable](cmdqueryname=multicast+mac-ip-check+enable) 
   ```
   
   By default, the device does not check the mapping correctness between destination MAC addresses and destination IP addresses of multicast packets.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```