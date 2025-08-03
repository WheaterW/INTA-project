(Optional) Configuring the Function of Discarding IP Packets with Identical Source and Destination IP Addresses
===============================================================================================================

(Optional) Configuring the Function of Discarding IP Packets with Identical Source and Destination IP Addresses

#### Context

IP packets typically have identical source and destination IP addresses only in special scenarios, for example, a network administrator may construct such packets for internal tests. By default, the device forwards these packets. However, if you suspect that such packets are caused by a local area network denial (LAND) attack, configure this function to discard the packets.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure the function of discarding IP packets with identical source and destination IP addresses.
   
   
   ```
   [ip anti-attack source-ip equals destination-ip drop](cmdqueryname=ip+anti-attack+source-ip+equals+destination-ip+drop) { all | slot slot-id } 
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The CE6885-LL in low latency mode does not support [**ip anti-attack source-ip equals destination-ip drop**](cmdqueryname=ip+anti-attack+source-ip+equals+destination-ip+drop).
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```