Verifying the Configuration of Other IPv6 PIM Parameters
========================================================

After adjusting PIM neighbor parameters, Designated router (DR) parameters, forwarding parameters, or Assert parameters, verify information about PIM interfaces, PIM neighbors, PIM routing tables, and statistics about PIM control messages.

#### Prerequisites

PIM neighbor parameters, DR parameters, forwarding parameters, or Assert parameters have been adjusted.


#### Procedure

* Run the [**display pim ipv6 interface**](cmdqueryname=display+pim+ipv6+interface) [ *interface-type* *interface-number* ] [ **verbose** ] command to check information about IPv6 PIM interfaces.
* Run the [**display pim ipv6 neighbor**](cmdqueryname=display+pim+ipv6+neighbor) [ *ipv6-link-local-address* | **interface** *interface-type* *interface-number* | **verbose** ] \* command to check information about IPv6 PIM neighbors.
* Run the [**display pim ipv6 routing-table**](cmdqueryname=display+pim+ipv6+routing-table) [ *ipv6-source-address* [ **mask** *mask-length* ] | *ipv6-group-address* [ **mask** *mask-length* ] | **incoming-interface** { *interface-type* *interface-number* | **register** } | **outgoing-interface** { **include** | **exclude** | **match** } { *interface-type* *interface-number* | **register** | **none** } | **mode** { **sm** | **ssm** } | **flags** *flag-value* | **fsm** ] \* [ **outgoing-interface-number** [ *number* ] ] command to check information about the IPv6 PIM routing table.
* Run the [**display pim ipv6 control-message counters**](cmdqueryname=display+pim+ipv6+control-message+counters) **message-type** { **probe** | **register** | **register-stop** | **crp** } or [**display pim ipv6 control-message counters**](cmdqueryname=display+pim+ipv6+control-message+counters) [ **message-type** { **assert** | **hello** | **join-prune** | **bsr** } | **interface** *interface-type* *interface-number* ] \* command to check the statistics about IPv6 PIM control messages.