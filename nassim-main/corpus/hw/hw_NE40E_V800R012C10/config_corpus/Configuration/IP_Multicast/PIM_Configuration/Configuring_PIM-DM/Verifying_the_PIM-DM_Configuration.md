Verifying the PIM-DM Configuration
==================================

After configuring PIM-DM, verify PIM interfaces, PIM neighbors, and the PIM routing table.

#### Prerequisites

PIM-DM has been configured.


#### Procedure

* Run the [**display pim**](cmdqueryname=display+pim) **interface** [ *interface-type* *interface-number* ] [ **verbose** ] command to check information about PIM interfaces.
* Run the [**display pim**](cmdqueryname=display+pim) **neighbor** [ **interface** *interface-type* *interface-number* | *neighbor-address* | **verbose** ] \* command to check PIM neighbors.
* Run the [**display pim grafts**](cmdqueryname=display+pim+grafts) command to check an unacknowledged PIM-DM graft.
* Run the [**display pim**](cmdqueryname=display+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **control-message** **counters** [ **interface** *interface-type interface-number* | **message-type** { **assert** | **hello** | **join-prune** | **graft** | **graft-ack** | **state-refresh** | **bsr** | **announcement** | **discovery** } ] \* command to check the number of the sent or received PIM control messages.
* Run the [**display pim routing-table**](cmdqueryname=display+pim+routing-table) [ *group-address* [ **mask** { *group-mask-length* | *group-mask* } ] | *source-address* [ **mask** { *source-mask-length* | *source-mask* } ] | **incoming-interface** *interface-type* *interface-number* | **outgoing-interface** { **include** | **exclude** | **match** } *interface-type* *interface-number* | **flags** *flag-value* | **fsm** ] \* [ **outgoing-interface-number** [ *number* ] ] ââââcommand to check the PIM routing table.