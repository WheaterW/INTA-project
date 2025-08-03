Setting the MTU Value for NAT64 Services
========================================

You can change the MTU value so that the packets for NAT64 are not fragmented, improving NAT64 translation efficiency.

#### Context

When the link MTU is small, NAT64 packet fragments may be generated. You can change the MTU value so that the packets for NAT64 are not fragmented, improving NAT64 translation efficiency.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nat64 instance**](cmdqueryname=nat64+instance) *instance-name* **id** *id*
   
   
   
   The NAT64 instance view is displayed.
3. Run [**nat64 mtu**](cmdqueryname=nat64+mtu) *value*
   
   
   
   The IPv6 MTU for packets of a NAT64 instance is set.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.