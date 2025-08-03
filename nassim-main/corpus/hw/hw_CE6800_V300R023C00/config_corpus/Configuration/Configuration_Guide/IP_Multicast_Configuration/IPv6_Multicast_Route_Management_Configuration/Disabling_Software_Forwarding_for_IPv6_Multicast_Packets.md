Disabling Software Forwarding for IPv6 Multicast Packets
========================================================

Disabling Software Forwarding for IPv6 Multicast Packets

#### Context

In most cases, a device uses software forwarding for assistance before hardware forwarding is complete. After software forwarding is complete, the forwarding mode is switched to hardware forwarding. In software forwarding, due to the first-packet cache mechanism and slow forwarding speed, the first packet may arrive out of order when multicast traffic arrives quickly. To avoid this issue, disable software forwarding for multicast packets on the device.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the IPv6 multicast function.
   
   
   ```
   [multicast ipv6 routing-enable](cmdqueryname=multicast+ipv6+routing-enable)
   ```
3. Disable software forwarding for IPv6 multicast packets.
   
   
   ```
   [multicast ipv6 cpu-forward disable](cmdqueryname=multicast+ipv6+cpu-forward+disable)
   ```
   
   In fast channel change (FCC) scenarios, you are advised to run this command to disable software forwarding for IPv6 multicast packets.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```