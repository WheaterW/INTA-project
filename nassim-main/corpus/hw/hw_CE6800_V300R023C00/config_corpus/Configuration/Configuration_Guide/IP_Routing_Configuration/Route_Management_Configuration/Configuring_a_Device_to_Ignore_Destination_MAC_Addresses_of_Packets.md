Configuring a Device to Ignore Destination MAC Addresses of Packets
===================================================================

Configuring a Device to Ignore Destination MAC Addresses of Packets

#### Context

During network maintenance, traffic is often diverted to specific devices for analysis. Generally, the device forwards only the packets with destination MAC addresses being the MAC addresses of local Layer 3 interfaces at Layer 3 according to the routing table. Other packets are forwarded at Layer 2 or discarded. If the device needs to forward the latter packets at Layer 3, you need to configure the device to ignore the destination MAC addresses of packets.

![](public_sys-resources/note_3.0-en-us.png) 

This configuration is supported only by the following: CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, CE6863E-48S8CQ, CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure the device to ignore the destination MAC addresses of packets.
   
   
   ```
   [ip routing ignore-mac](cmdqueryname=ip+routing+ignore-mac)
   ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display this**](cmdqueryname=display+this) command to check the configuration of ignoring the destination MAC addresses of packets.