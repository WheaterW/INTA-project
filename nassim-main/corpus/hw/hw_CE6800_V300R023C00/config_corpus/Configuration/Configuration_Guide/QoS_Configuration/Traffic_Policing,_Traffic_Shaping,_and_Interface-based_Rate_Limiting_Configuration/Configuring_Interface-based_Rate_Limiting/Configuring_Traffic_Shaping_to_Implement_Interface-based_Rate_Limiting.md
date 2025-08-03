Configuring Traffic Shaping to Implement Interface-based Rate Limiting
======================================================================

Configuring Traffic Shaping to Implement Interface-based Rate Limiting

#### Context

When a large amount of traffic is sent from the downstream device to its upstream device, to prevent congestion or packet loss, configure traffic shaping on the outbound interface of the device. Traffic shaping adjusts the rate of outgoing traffic on the interface to reduce traffic bursts so that outgoing packets can be transmitted at a stable rate. With traffic shaping, packets exceeding the rate limit enter the buffer queue, and are only sent out at an even rate when there are sufficient tokens in the token bucket. In addition, if the buffer queue is full, the system discards new packets.

If packets are encapsulated through VPN tunnels, the calculated packet length during rate limiting or traffic statistics collection on a WAN-side interface includes the lengths of link-layer and physical-layer packet headers and the lengths of tunnel protocol encapsulation headers. As a result, the actual user bandwidth calculated using this method is smaller than the expected value. To minimize the difference between the actual bandwidth and the expected bandwidth, you can disable the device from counting the inter-frame gaps and preambles when it calculates the packet length, and configure the function of excluding the tunnel encapsulation length of packets on the tunnel interface. In this way, the calculated packet length excludes the lengths of the physical-layer packet header and tunnel protocol encapsulation header.

![](public_sys-resources/note_3.0-en-us.png) 

Currently, traffic shaping can only be used to rate-limit outgoing traffic on an interface.

The system will generate an alarm when the rate of outgoing traffic on an interface exceeds the alarm threshold for rate-limiting outgoing traffic.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) { interface-type interface-number | interface-name }
   ```
3. Configure the rate limit for outgoing traffic on the interface.
   
   
   
   For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S:
   
   ```
   [qos lr](cmdqueryname=qos+lr) cir cir-value [ kbps | mbps | gbps ] [ cbs cbs-value [ bytes | kbytes | mbytes ] ] [ outbound ]
   ```
   
   For the CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, CE6863E-48S8CQ:
   
   ```
   [qos lr](cmdqueryname=qos+lr) cir cir-value [ kbps | mbps | gbps ] [ outbound ]
   ```
   
   By default, the rate limit on an interface is the maximum bandwidth of the interface.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```