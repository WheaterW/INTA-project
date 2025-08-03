Verifying the Configuration
===========================

Verifying the Configuration

#### Procedure

* Run the [**display igmp snooping**](cmdqueryname=display+igmp+snooping) **bridge-domain** [ *bd-id* ] **configuration** command to check IGMP snooping configurations in a BD.
* Run the [**display igmp snooping port-info**](cmdqueryname=display+igmp+snooping+port-info) **bridge-domain** *bd-id* [ **group-address** *group-address* ] [ **verbose** ] command to check multicast group member ports.
* Run the [**display l2-multicast forwarding-table**](cmdqueryname=display+l2-multicast+forwarding-table) [ **bridge-domain** *bridge-domain-id* [ **group** *group-address* ] ] [ **slot** *slot-id* [ **cpu** *cpu-id* ] ] command to check Layer 2 multicast forwarding entries in a BD.