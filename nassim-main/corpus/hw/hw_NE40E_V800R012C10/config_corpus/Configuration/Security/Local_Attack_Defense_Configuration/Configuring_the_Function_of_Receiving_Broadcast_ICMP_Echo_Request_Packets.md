Configuring the Function of Receiving Broadcast ICMP Echo Request Packets
=========================================================================

Configuring the Function of Receiving Broadcast ICMP Echo Request Packets

#### Usage Scenario

A device drops ICMP echo request packets that carry broadcast addresses (including subnet broadcast and network broadcast addresses) as destination IP addresses by default. When the device is required to normally process broadcast ICMP echo request packets, run the [**icmp-broadcast-address-echo enable**](cmdqueryname=icmp-broadcast-address-echo+enable) command to enable the device to receive broadcast ICMP echo request packets.

In VS mode, this feature is supported only by the admin VS.


#### Prerequisites

None


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**cpu-defend policy**](cmdqueryname=cpu-defend+policy) *policy-number*
   
   
   
   The attack defense policy view is displayed.
3. Run [**icmp-broadcast-address-echo enable**](cmdqueryname=icmp-broadcast-address-echo+enable)
   
   
   
   The system is enabled to receive broadcast ICMP echo request packets.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.