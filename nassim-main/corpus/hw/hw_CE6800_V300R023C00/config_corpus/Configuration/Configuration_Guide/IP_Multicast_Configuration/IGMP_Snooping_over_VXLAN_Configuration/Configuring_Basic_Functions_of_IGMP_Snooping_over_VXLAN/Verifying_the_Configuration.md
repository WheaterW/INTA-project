Verifying the Configuration
===========================

Verifying the Configuration

#### Procedure

* Run the [**display igmp snooping**](cmdqueryname=display+igmp+snooping) **bridge-domain** [ *bd-id* ] **configuration** command to check IGMP snooping configurations in a BD.
* Run the [**display igmp snooping**](cmdqueryname=display+igmp+snooping) **bridge-domain** [ *bd-id* ] command to check IGMP snooping running parameters in a BD.
* Run the [**display igmp snooping port-info**](cmdqueryname=display+igmp+snooping+port-info) **bridge-domain** *bd-id* [ **group-address** *group-address* ] [ **verbose** ] command to check member ports of a multicast group.
* Run the [**display igmp snooping router-port**](cmdqueryname=display+igmp+snooping+router-port) [ **bridge-domain** *bd-id* ] command to check router ports in a BD.
* Run the [**display l2-multicast forwarding-table**](cmdqueryname=display+l2-multicast+forwarding-table) [ **bridge-domain** *bridge-domain-id* [ **group** *group-address* ] ] [ **slot** *slot-id* [ **cpu** *cpu-id* ] ] command to check Layer 2 multicast forwarding entries in a BD.
* Run the [**display igmp snooping querier**](cmdqueryname=display+igmp+snooping+querier) **bridge-domain** [ *bdid* ] command to check whether the IGMP snooping querier function is enabled.