Verifying the Configuration
===========================

After adjusting PIM neighbor parameters, Designated router (DR) parameters, forwarding parameters, or Assert parameters, verify information about PIM interfaces, PIM neighbors, PIM routing tables, and statistics about PIM control messages.

#### Prerequisites

PIM neighbor parameters, DR parameters, forwarding parameters, or Assert parameters have been adjusted.


#### Procedure

* Run the [**display pim**](cmdqueryname=display+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ]  **interface** [ *interface-type* *interface-number* | **up** | **down** ] [ **verbose** ] command to check information about PIM interfaces.
* Run the [**display pim**](cmdqueryname=display+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ]  **neighbor** [ **interface** *interface-type* *interface-number* | *neighbor-address* | **verbose** ] \* command to check information about PIM neighbors.
* Run the [**display pim**](cmdqueryname=display+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ]  **routing-table** [ *group-address* [ **mask** { *group-mask-length* | *group-mask* } ] | *source-address* [ **mask** { *source-mask-length* | *source-mask* } ] | **outgoing-interface** **include** { *interface-type* *interface-number* | **register** | **none** } | **fsm** ] command to check information about the PIM routing table.
* Run the [**display pim**](cmdqueryname=display+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **control-message** **counters** [ **interface** *interface-type interface-number* | **message-type** { **assert** | **hello** | **join-prune** | **bsr** } ] \* or [**display pim**](cmdqueryname=display+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **control-message** **counters** **message-type** { **crp** | **probe** | **register** | **register-stop** } command to check statistics about PIM control messages.