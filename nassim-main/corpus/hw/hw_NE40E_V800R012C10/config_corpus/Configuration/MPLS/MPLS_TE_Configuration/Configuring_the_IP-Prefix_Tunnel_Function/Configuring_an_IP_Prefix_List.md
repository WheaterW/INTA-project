Configuring an IP Prefix List
=============================

An IP prefix list can be configured to define destination IP addresses used in the ip-prefix tunnel function.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip ip-prefix**](cmdqueryname=ip+ip-prefix) *ip-prefix-name* [ **index** *index-number* ] *matchMode* *ipv4-address* *masklen* [ **greater-equal** *greater-equal-value* ] [ **less-equal** *less-equal-value* ]
   
   
   
   An IPv4 prefix list is configured.
   
   
   
   *ip-prefix-name* specifies the destination IP address that can or cannot be used to establish a tunnel.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.