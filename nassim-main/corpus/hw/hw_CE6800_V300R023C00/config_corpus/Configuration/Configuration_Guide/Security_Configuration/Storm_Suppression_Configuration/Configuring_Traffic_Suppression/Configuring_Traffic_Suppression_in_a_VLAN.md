Configuring Traffic Suppression in a VLAN
=========================================

Configuring Traffic Suppression in a VLAN

#### Context

To rate-limit incoming broadcast packets, unknown multicast packets, or unknown unicast packets in a VLAN so as to prevent broadcast storms, you can configure traffic suppression for the corresponding type of packets in the VLAN. Once the rate reaches the configured threshold, the device will then discard excess packets.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VLAN view.
   
   
   ```
   [vlan](cmdqueryname=vlan) vlan-id
   ```
3. Configure traffic suppression in a VLAN.
   
   
   ```
   [storm suppression](cmdqueryname=storm+suppression) { broadcast | multicast | unknown-unicast } cir cir-value [ gbps | kbps | mbps ] [ cbs cbs-value [ bytes | kbytes | mbytes ] ]
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```