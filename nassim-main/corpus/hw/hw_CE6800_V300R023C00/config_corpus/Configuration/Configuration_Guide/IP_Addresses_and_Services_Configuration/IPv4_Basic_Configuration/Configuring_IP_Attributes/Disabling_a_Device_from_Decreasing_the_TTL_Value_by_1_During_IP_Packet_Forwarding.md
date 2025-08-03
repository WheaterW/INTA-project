Disabling a Device from Decreasing the TTL Value by 1 During IP Packet Forwarding
=================================================================================

Disabling a Device from Decreasing the TTL Value by 1 During IP Packet Forwarding

#### Context

For accurate traffic analysis of distributed services, a traffic analysis server must receive the original network traffic without any change. To meet this requirement, a traffic distribution device must ensure the integrity of packets during forwarding, without changing any of their attributes.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Disable the device from decreasing the TTL value by 1 during IP packet forwarding.
   
   
   ```
   [ip ttl decrement disable](cmdqueryname=ip+ttl+decrement+disable)
   ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```