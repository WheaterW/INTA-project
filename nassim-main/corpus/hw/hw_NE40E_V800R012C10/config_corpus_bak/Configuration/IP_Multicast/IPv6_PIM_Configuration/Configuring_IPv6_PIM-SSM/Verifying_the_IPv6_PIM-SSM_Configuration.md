Verifying the IPv6 PIM-SSM Configuration
========================================

After configuring IPv6 Protocol Independent Multicast-Source-Specific Multicast (PIM-SSM), verify PIM interfaces, PIM neighbors, and PIM routing tables by using related commands.

#### Prerequisites

The IPv6 PIM-SSM configurations are complete.


#### Procedure

* Run the [**display pim ipv6 interface**](cmdqueryname=display+pim+ipv6+interface) [ *interface-type* *interface-number* ] [ **verbose** ] command to check IPv6 PIM interfaces.
* Run the [**display pim ipv6 neighbor**](cmdqueryname=display+pim+ipv6+neighbor) [ *ipv6-link-local-address* | **interface** *interface-type* *interface-number* | **verbose** ] \* command to check IPv6 PIM neighbors.
* Run the [**display pim ipv6 routing-table**](cmdqueryname=display+pim+ipv6+routing-table) [ *ipv6-source-address* [ **mask** *mask-length* ] | *ipv6-group-address* [ **mask** *mask-length* ] | **incoming-interface** { *interface-type* *interface-number* | **register** } | **outgoing-interface** { **include** | **exclude** | **match** } { *interface-type* *interface-number* | **register** | **none** } | **mode** { **sm** | **ssm** } | **flags** *flag-value* | **fsm** ] \* [ **outgoing-interface-number** [ *number* ] ] command to check the IPv6 PIM routing table of a device.