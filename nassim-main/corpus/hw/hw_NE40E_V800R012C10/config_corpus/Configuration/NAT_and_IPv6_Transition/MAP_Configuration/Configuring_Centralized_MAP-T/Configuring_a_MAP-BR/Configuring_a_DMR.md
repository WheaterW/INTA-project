Configuring a DMR
=================

A default mapping rule (DMR) can be created. A MAP-CE encapsulates an IPv6 prefix defined in the DMR into packets and directs the packets to a service board. Address translation is performed in the bound MAP-T instance.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dmr-prefix**](cmdqueryname=dmr-prefix) *dmr-name* **ipv6-prefix** *ipv6-prefix* **prefix-length** *prefix-length*
   
   
   
   The IPv6 prefix address and length are set in a DMR.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.