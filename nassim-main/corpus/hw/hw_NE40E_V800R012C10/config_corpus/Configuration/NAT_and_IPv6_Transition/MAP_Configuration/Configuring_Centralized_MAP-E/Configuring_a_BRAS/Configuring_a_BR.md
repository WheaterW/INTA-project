Configuring a BR
================

A border relay (BR) is created. The MAP-CE encapsulates
an IPv6 prefix defined based on the BR into traffic and directs the
traffic to an interface board. The MAP-CE then selects a MAP-E instance
to convert the traffic.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**br-ipv6-address**](cmdqueryname=br-ipv6-address) *br-name* **ipv6-address** *ipv6-address* **prefix-length** *prefix-length*
   
   
   
   The IPv6 prefix address and length are set in on the BR.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.