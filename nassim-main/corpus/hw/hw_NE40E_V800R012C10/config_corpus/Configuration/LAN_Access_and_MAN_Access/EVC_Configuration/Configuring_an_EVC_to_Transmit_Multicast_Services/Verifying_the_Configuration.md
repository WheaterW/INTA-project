Verifying the Configuration
===========================

After configuring an EVC to transmit multicast services, you can check the status of multicast services.

#### Prerequisites

An EVC has been configured to transmit multicast services.


#### Procedure

* Run the [**display igmp-snooping**](cmdqueryname=display+igmp-snooping) **bridge-domain** [ *bd-id* ] [ **configuration** ] command to check whether IGMP snooping is enabled.
* Run the [**display igmp-snooping router-port**](cmdqueryname=display+igmp-snooping+router-port) **bridge-domain** *bd-id* command to check information about router interfaces.
* Run the [**display pim interface**](cmdqueryname=display+pim+interface) [ *interface-type interface-number* ] [ **verbose** ] command to check whether PIM-SM is enabled.
* Run the [**display pim routing-table**](cmdqueryname=display+pim+routing-table) command to check the IPv4 routing table.