Verifying the Configuration
===========================

Verifying the Configuration

#### Procedure

* Run the [**display pim ipv6**](cmdqueryname=display+pim+ipv6) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **bsr-info** command to check information about the BSR in an IPv6 PIM-SM domain.
* Run the [**display pim ipv6**](cmdqueryname=display+pim+ipv6) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **interface** [ *interface-type* *interface-number* ] [ **verbose** ] command to check IPv6 PIM interface information.
* Run the [**display pim ipv6**](cmdqueryname=display+pim+ipv6) [ **vpn-instance** *vpn-instance-name* | **all-instance** ]  **neighbor** [ **interface** *interface-type* *interface-number* | *ipv6-link-local-address* | **verbose** ] \* command to check IPv6 PIM neighbor information.
* Run the [**display pim ipv6**](cmdqueryname=display+pim+ipv6) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **routing-table** [ *ipv6-source-address* [ **mask** *mask-length* ] | *ipv6-group-address* [ **mask** *mask-length* ] | **incoming-interface** { *interface-type* *interface-number* | **register** } | **outgoing-interface** { **include** | **exclude** | **match** } { *interface-type* *interface-number* | **register** | **none** } | **mode** { **sm** | **ssm** } | **flags** *flag-value* | **fsm** ] \* [ **outgoing-interface-number** [ *number* ] ] command to check the IPv6 PIM routing table.