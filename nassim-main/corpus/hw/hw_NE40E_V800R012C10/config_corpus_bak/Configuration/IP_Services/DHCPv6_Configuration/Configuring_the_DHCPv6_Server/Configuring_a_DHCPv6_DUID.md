Configuring a DHCPv6 DUID
=========================

Configuring_a_DHCPv6_DUID

#### Context

A DUID uniquely identifies a DHCPv6 device. Each DHCPv6 client or server must have only one DUID. A DHCPv6 server identifies clients based on client DUIDs, and a DHCPv6 client identifies servers based on server DUIDs.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dhcpv6 duid**](cmdqueryname=dhcpv6+duid) { *duid-value* | **llt** | **ll** }
   
   
   
   A DUID is configured for the DHCPv6 device.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.