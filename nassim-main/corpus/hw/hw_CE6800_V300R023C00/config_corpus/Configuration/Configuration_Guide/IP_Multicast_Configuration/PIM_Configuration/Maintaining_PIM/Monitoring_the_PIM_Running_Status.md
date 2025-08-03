Monitoring the PIM Running Status
=================================

Monitoring the PIM Running Status

#### Context

During routine maintenance, you can run the following commands as required in any view to check the PIM running status.

**Table 1** Monitoring the PIM running status
| Operation | Command |
| --- | --- |
| Check information about unicast routes used by PIM. | [**display pim**](cmdqueryname=display+pim) **claimed-route** [ *source-address* ] |
| Check information about BFD sessions. | [**display pim**](cmdqueryname=display+pim)  [**bfd** **session** [ **interface** *interface-type* *interface-number* | **neighbor** *neighbor-address* ]] |
| Check information about the BSR in a PIM-SM domain. | [**display pim**](cmdqueryname=display+pim) **bsr-info** |
| Check the number of sent and received PIM control messages. | [**display pim**](cmdqueryname=display+pim)  **control-message counters** **message-type** { **probe** | **register** | **register-stop** | **crp** }  [**display pim**](cmdqueryname=display+pim)  [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **control-message counters** [ **message-type** { **assert** | **graft** | **graft-ack** | **hello** | **join-prune** | **state-refresh** | **bsr** } | **interface** *interface-type* *interface-number* ] \* |
| Check PIM information on interfaces. | [**display pim**](cmdqueryname=display+pim)  **interface** [ *interface-type* *interface-number* | **up** | **down** ] [ **verbose** ] |
| Check PIM neighbor information. | [**display pim**](cmdqueryname=display+pim)  [ **neighbor** [ *neighbor-address* | **interface** *interface-type* *interface-number* | **verbose** ]] \* |
| Check PIM routing table information. | [**display pim**](cmdqueryname=display+pim) **routing-table** [ *group-address* [ **mask** { *group-mask-length* | *group-mask* } ] | *source-address* [ **mask** { *source-mask-length* | *source-mask* } ] | **incoming-interface** { *interface-type* *interface-number* | **register** } | **outgoing-interface** { **include** | **exclude** | **match** } { *interface-type* *interface-number* | **register** | **none** } | **mode** { **sm** | **ssm** } | **flags** *flag-value* | **fsm** ] \* [ **outgoing-interface-number** [ *number* ] ]  **display pim routing-table** **brief** [ *group-address* [ **mask** { *group-mask-length* | *group-mask* } ] | *source-address* [ **mask** { *source-mask-length* | *source-mask* } ] | **incoming-interface** { *interface-type interface-number* | **register** } ] \* |
| Check RP information of a multicast group. | [**display pim**](cmdqueryname=display+pim)   **rp-info** [ *group-address* ] |
| Check statistics about invalid PIM messages received on a device. | [**display pim**](cmdqueryname=display+pim)   **invalid-packet** [ **interface** *interface-type interface-number* | **message-type** { **assert** | **bsr** | **hello** | **join-prune** | **graft** | **graft-ack** | **state-refresh** } ] \* |
| Check the limit on the number of PIM entries, as well as PIM statistics, on a device. | **display multicast global** { **pim sm** | **pim dm** | **all**} **statistics** |