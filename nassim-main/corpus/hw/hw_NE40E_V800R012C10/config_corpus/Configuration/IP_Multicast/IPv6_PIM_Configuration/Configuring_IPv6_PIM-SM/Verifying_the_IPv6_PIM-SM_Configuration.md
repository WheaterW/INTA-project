Verifying the IPv6 PIM-SM Configuration
=======================================

After configuring IPv6 PIM-SM, verify information about BootStrap routers (BSRs), Rendezvous Points (RPs), PIM interfaces, PIM neighbors, and PIM routing tables.

#### Prerequisites

IPv6 PIM-SM has been configured.


#### Procedure

* Run the [**display pim ipv6 bsr-info**](cmdqueryname=display+pim+ipv6+bsr-info) command to check BSR information in an IPv6 PIM-SM domain.
* Run the [**display pim ipv6 interface**](cmdqueryname=display+pim+ipv6+interface) [ *interface-type* *interface-number* ] [ **verbose** ] command to check information about IPv6 PIM interfaces.
* Run the [**display pim ipv6 neighbor**](cmdqueryname=display+pim+ipv6+neighbor) [ *ipv6-link-local-address* | **interface** *interface-type* *interface-number* | **verbose** ] \* command to check information about IPv6 PIM neighbors.
* Run the [**display pim ipv6 routing-table**](cmdqueryname=display+pim+ipv6+routing-table) [ *ipv6-source-address* [ **mask** *mask-length* ] | *ipv6-group-address* [ **mask** *mask-length* ] | **incoming-interface** { *interface-type* *interface-number* | **register** } | **outgoing-interface** { **include** | **exclude** | **match** } { *interface-type* *interface-number* | **register** | **none** } | **mode** { **sm** | **ssm** } | **flags** *flag-value* | **fsm** ] \* [ **outgoing-interface-number** [ *number* ] ] command to check information about IPv6 PIM routing tables.
* Run the [**display pim ipv6 rp-info**](cmdqueryname=display+pim+ipv6+rp-info) [ *ipv6-group-address* ] command to check RP information in an IPv6 PIM-SM domain.