Enabling DHCPv6
===============

DHCPv6 provides client, relay, and server functions.

#### Context

DHCPv6 provides client, relay, and server functions. The NE40E can only have the DHCPv6 relay functionality.

A DHCP Unique Identifier (DUID) uniquely identifies a DHCPv6 device. Each DHCPv6 client or server must have one DUID. The DUID is optional for DHCPv6 relay agents.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dhcpv6 enable**](cmdqueryname=dhcpv6+enable)
   
   
   
   DHCPv6 is enabled globally.
3. (Optional) Run [**dhcpv6 duid**](cmdqueryname=dhcpv6+duid) { *duid-value* | **llt** }
   
   
   
   A DUID is configured for the DHCPv6 device.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.