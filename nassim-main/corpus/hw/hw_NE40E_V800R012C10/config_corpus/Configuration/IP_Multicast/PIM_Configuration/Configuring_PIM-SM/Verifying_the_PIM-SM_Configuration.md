Verifying the PIM-SM Configuration
==================================

After PIM-SM is configured, verify information about BootStrap routers (BSRs), rendezvous points (RPs), PIM interfaces, PIM neighbors, and PIM routing tables.

#### Prerequisites

PIM-SM has been configured.


#### Procedure

* Run the [**display pim**](cmdqueryname=display+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **bsr-info** command to check BSR information in a PIM-SM domain.
* Run the [**display pim**](cmdqueryname=display+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **interface** [ *interface-type* *interface-number* ] [ **verbose** ] command to check PIM interface information.
* Run the [**display pim**](cmdqueryname=display+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **neighbor** [ **interface** *interface-type* *interface-number* | *neighbor-address* | **verbose** ] \* command to check PIM neighbor information.
* Run the [**display pim**](cmdqueryname=display+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **routing-table** [ *group-address* [ **mask** { *group-mask-length* | *group-mask* } ] | *source-address* [ **mask** { *source-mask-length* | *source-mask* } ] | **outgoing-interface** **include** { *interface-type* *interface-number* | **register** | **none** } | **fsm** ] command to check the PIM routing table.
* Run the [**display pim**](cmdqueryname=display+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **rp-info** [ *group-address* ] command to check RP information in a PIM-SM domain.
* Run the [**display multicast global**](cmdqueryname=display+multicast+global) **outgoing-interface pim sm statistics** command to check statistics about outbound interfaces in PIM-SM entries.