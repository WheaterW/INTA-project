Verifying the PIM-SSM Configuration
===================================

After the Protocol Independent Multicast-Source-Specific Multicast (PIM-SSM) is configured, verify information about PIM interfaces, PIM neighbors, and PIM routing tables.

#### Prerequisites

PIM-SSM has been configured.


#### Procedure

* Run the [**display pim**](cmdqueryname=display+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **interface** [ *interface-type* *interface-number* ] [ **verbose** ] command to check PIM interface information.
* Run the [**display pim**](cmdqueryname=display+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **neighbor** [ **interface** *interface-type* *interface-number* | *neighbor-address* | **verbose** ] \* command to check PIM neighbor information.
* Run the [**display pim**](cmdqueryname=display+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **routing-table** [ *group-address* [ **mask** { *group-mask-length* | *group-mask* } ] | *source-address* [ **mask** { *source-mask-length* | *source-mask* } ] | **outgoing-interface** **include** { *interface-type* *interface-number* | **register** | **none** } | **fsm** ] command to check the PIM routing table.