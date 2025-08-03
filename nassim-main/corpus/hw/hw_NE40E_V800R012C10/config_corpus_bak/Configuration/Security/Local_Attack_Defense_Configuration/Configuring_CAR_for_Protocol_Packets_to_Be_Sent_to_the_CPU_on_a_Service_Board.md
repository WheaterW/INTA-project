Configuring CAR for Protocol Packets to Be Sent to the CPU on a Service Board
=============================================================================

You can configure CAR for protocol packets to be sent to the CPU on a service board to implement traffic policing for these packets, preventing CPU usage from increasing and services from being affected.

#### Usage Scenario

When a large number of users access a device and the CPU of the service board is vulnerable to packet attacks or needs to process a large number of packets, you can configure the CAR function on the service board.

In VS mode, this feature is supported only by the admin VS.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only the NE40E-M2K, NE40E-M2K-B support this configuration.



#### Prerequisites

None


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**slot**](cmdqueryname=slot) *slot-id*
   
   
   
   The slot view is displayed.
3. Run [**cpu-defend spu-car**](cmdqueryname=cpu-defend+spu-car+icmp+tcp+udp+gre+bgp+default+ike-total-car) { **icmp** | **tcp** | **udp** | **gre** | **bgp** | **default** | **ike-total-car** | **ike-tunnel-car** | **plain-sa-miss** | **cipher-sa-miss** | **ipsec-rekey** | **ike-dpd** | **fast-channel** | **pst** | **bfd-down** | **dslite-private-ipv4** | **ip-option** | **mtu-exceed** | **tsu-detect-keeplive**} { **cir** *cir-value* | **cbs** *cbs-value* } \* or [**cpu-defend spu-car**](cmdqueryname=cpu-defend+spu-car+cgn-icmp+cgn-icmpv6+cgn-ipv4-other) { **cgn-icmp** | **cgn-icmpv6** | **cgn-ipv4-other** | **cgn-ipv6-other** | **cgn-ipv6-raw** | **cgn-total** } { **cir** *cir-value* | **cbs** *cbs-value* } \*
   
   
   
   CAR is configured for packets on the service board.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.