Monitoring the Running Status of PIM
====================================

You can monitor the PIM running status by checking unicast routes, BSRs, and RPs used by PIM, statistics about PIM control messages, and information about PIM neighbors and the PIM routing table.

#### Context

You can run the following commands in any view to check the PIM running status.


#### Procedure

* Run the [**display pim**](cmdqueryname=display+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **claimed-route** [ *source-address* ] command in any view to check information about unicast routes used by PIM.
* Run the [**display pim**](cmdqueryname=display+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **bsr-info** command in any view to check information about a BSR in a PIM-SM domain.
* Run the [**display pim**](cmdqueryname=display+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **control-message counters** command in any view to check statistics about PIM control messages.
* Run the [**display pim**](cmdqueryname=display+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **interface** [ *interface-type* *interface-number* ] [ **verbose** ] command in any view to check PIM interfaces.
* Run the [**display pim**](cmdqueryname=display+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **neighbor** [ **interface** *interface-type* *interface-number* | *neighbor-address* | **verbose** ] \* command in any view to check information about PIM neighbors.
* Run the [**display pim routing-table**](cmdqueryname=display+pim+routing-table) command in any view to check information about PIM routing tables.
  
  
  + [**display pim**](cmdqueryname=display+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **routing-table** [ *group-address* [ **mask** { *group-mask-length* | *group-mask* } ] | *source-address* [ **mask** { *source-mask-length* | *source-mask* } ] | **incoming-interface** { *interface-type* *interface-number* | **register** | **through-bgp** } | **outgoing-interface** { **include** | **exclude** | **match** } { *interface-type* *interface-number* | **register** | **none** | **pseudo** } | **mode** { **ssm** | **sm** } | **flags** *flag-value* | **fsm** ] \* [ **outgoing-interface-number** [ *number* ] ]
  + [**display pim routing-table**](cmdqueryname=display+pim+routing-table) [ *group-address* [ **mask** { *group-mask-length* | *group-mask* } ] | *source-address* [ **mask** { *source-mask-length* | *source-mask* } ] | **incoming-interface** { *interface-type* *interface-number* | **register** } | **outgoing-interface** { **include** | **exclude** | **match** } { *interface-type* *interface-number* | **vpn-instance** *vpn-instance-name* | **register** | **none** } | **mode** { **ssm** | **sm** } | **flags** *flag-value* | **fsm** ] \* [ **outgoing-interface-number** [ *number* ] ]
* Run the [**display pim**](cmdqueryname=display+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ]  **rp-info** [ *group-address* ] command in any view to check information about the RP serving the multicast group.