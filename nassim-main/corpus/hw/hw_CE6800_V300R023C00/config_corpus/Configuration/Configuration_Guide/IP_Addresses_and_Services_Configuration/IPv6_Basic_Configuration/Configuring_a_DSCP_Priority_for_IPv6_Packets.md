Configuring a DSCP Priority for IPv6 Packets
============================================

Configuring a DSCP Priority for IPv6 Packets

#### Context

In an IPv6 packet header, the first six bits in the Traffic Class field are defined as the differentiated services code point (DSCP). Each protocol has a default DSCP value. After receiving packets, a device classifies them into different queues based on the DSCP priorities they carry, and preferentially processes those with higher DSCP priorities. During network deployment, you can change the DSCP priorities of packets as required.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure a DSCP priority for IPv6 packets on the device.
   
   
   ```
   [set priority ipv6 dscp](cmdqueryname=set+priority+ipv6+dscp) dscp-value
   ```