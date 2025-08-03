Monitoring the Running Status of IPv6 PIM
=========================================

You can monitor the IPv6 PIM running status by checking unicast routes, BootStrap routers (BSRs), and Rendezvous Points (RPs) used by IPv6 PIM, statistics about PIM control messages, and information about PIM neighbors and PIM routing tables.

#### Context

You can run the following commands in any view to check the IPv6 PIM running status.


#### Procedure

* Run the [**display pim ipv6 claimed-route**](cmdqueryname=display+pim+ipv6+claimed-route) [ *source-address* ] command to check unicast routes used by IPv6 PIM.
* Run the [**display pim ipv6 bsr-info**](cmdqueryname=display+pim+ipv6+bsr-info) command to check information about a BSR in an IPv6 PIM-SM domain.
* Run the [**display pim ipv6 control-message counters**](cmdqueryname=display+pim+ipv6+control-message+counters) **message-type** { **probe** | **register** | **register-stop** | **crp** } or [**display pim ipv6 control-message counters**](cmdqueryname=display+pim+ipv6+control-message+counters) [ **message-type** { **assert** | **hello** | **join-prune** | **bsr** } | **interface** *interface-type* *interface-number* ] \* command to check statistics about IPv6 PIM control messages.
* Run the [**display pim ipv6 interface**](cmdqueryname=display+pim+ipv6+interface) [ *interface-type* *interface-number* ] [ **verbose** ] command to check IPv6 PIM interfaces.
* Run the [**display pim ipv6 neighbor**](cmdqueryname=display+pim+ipv6+neighbor) [ *ipv6-link-local-address* | **interface** *interface-type* *interface-number* | **verbose** ] \* command to check IPv6 PIM neighbors.
* Run the [**display pim ipv6 routing-table**](cmdqueryname=display+pim+ipv6+routing-table) [ *ipv6-source-address* [ **mask** *mask-length* ] | *ipv6-group-address* [ **mask** *mask-length* ] | **incoming-interface** { *interface-type* *interface-number* | **register** } | **outgoing-interface** { **include** | **exclude** | **match** } { *interface-type* *interface-number* | **register** | **none** } | **mode** { **sm** | **ssm** } | **flags** *flag-value* | **fsm** ] \* [ **outgoing-interface-number** [ *number* ] ] command to check the IPv6 PIM routing table.
* Run the [**display pim ipv6 rp-info**](cmdqueryname=display+pim+ipv6+rp-info) [ *ipv6-group-address* ] command to check information about an RP in an IPv6 PIM-SM domain.