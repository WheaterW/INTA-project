Configuring a Static PMTU
=========================

You can manually configure a static PMTU according to the minimum MTU of the path along which packets are sent, resulting in higher transmission efficiency.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipv6 pathmtu**](cmdqueryname=ipv6+pathmtu+vpn-instance) *ipv6-address* [ [ **vpn-instance** *vpn-instance-name* ] *path-mtu* ]
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.