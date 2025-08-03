Verifying the Configuration
===========================

After configuring IPv6 FRR, you can view information about the backup outbound interfaces and backup next hops in the routing table.

#### Prerequisites

IPv6 FRR has been configured.


#### Procedure

* Run the [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) **verbose** command to check backup outbound interface and backup next hop information in the routing table.
* Run the [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) *ip-address* [ *mask* | *mask-length* ] [ **longer-match** ] **verbose** command to check backup outbound interface and backup next hop information in the routing table.
* Run the [**display ipv6 routing-table**](cmdqueryname=display+ipv6+routing-table) *ip-address1* { *mask1* | *mask-length1* } *ip-address2* { *mask2* | *mask-length2* } **verbose** command to check backup outbound interface and backup next hop information in the routing table.