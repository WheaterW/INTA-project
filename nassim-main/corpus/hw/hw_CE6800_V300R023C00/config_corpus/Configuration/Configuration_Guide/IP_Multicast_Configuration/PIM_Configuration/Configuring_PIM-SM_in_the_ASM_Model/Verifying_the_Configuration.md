Verifying the Configuration
===========================

Verifying the Configuration

#### Procedure

* Run the [**display pim**](cmdqueryname=display+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **bsr-info** command to check information about the BSR in a PIM-SM domain.
* Run the [**display pim**](cmdqueryname=display+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **interface** [ *interface-type* *interface-number* ] [ **verbose** ] command to check PIM interface information.
* Run the [**display pim**](cmdqueryname=display+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **neighbor** [ **interface** *interface-type* *interface-number* | *neighbor-address* | **verbose** ] \* command to check PIM neighbor information.
* Run the [**display pim**](cmdqueryname=display+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **routing-table** [ *group-address* [ **mask** { *group-mask-length* | *group-mask* } ] | *source-address* [ **mask** { *source-mask-length* | *source-mask* } ] | **outgoing-interface** **include** { *interface-type* *interface-number* | **register** | **none** } | **fsm** ] command to check the PIM routing table.
* Run the [**display pim**](cmdqueryname=display+pim) **rp-info** [ *group-address* ] command to check information about the RPs in a PIM-SM domain.