Monitoring the Running Status of IGMP Snooping
==============================================

The commands for monitoring IGMP snooping display Layer 2 multicast information, including the information about the Layer 2 multicast enabling status, the forwarding table and port table, and the protection group.

#### Context

You can run the following commands in any view to check the running status of IGMP snooping.


#### Procedure

* Run the [**display igmp-snooping**](cmdqueryname=display+igmp-snooping) [ **vlan** [ *vlan-id* ] | **vsi** [ *vsi-name* ] ] [ **configuration** ] command in any view to check all the configurations of IGMP snooping.
* Run the [**display igmp-snooping port-info**](cmdqueryname=display+igmp-snooping+port-info) [ **vlan** *vlan-id* [ **group-address** *group-address* ] ] [ **verbose** ] command in any view to check information about Router ports.
* Run the [**display igmp-snooping router-port**](cmdqueryname=display+igmp-snooping+router-port) { **vlan** *vlan-id* | **vsi** *vsi-name* } command in any view to check information about router interfaces.
* Run the [**display igmp-snooping statistics**](cmdqueryname=display+igmp-snooping+statistics) { **vlan** [ *vlan-id* ] | **vsi** [ *vsi-name* ] } command in any view to check IGMP snooping statistics.
* Run the [**display igmp-snooping querier**](cmdqueryname=display+igmp-snooping+querier) { **vlan** [ *vlan-id* ] | **vsi** [ *vsi-name* ] } command in any view to check information about the IGMP snooping querier.
* Run the [**display igmp-snooping group-info**](cmdqueryname=display+igmp-snooping+group-info) command in any view to check dynamically learned multicast group information on local interfaces.
* Run the [**display igmp-snooping group-info remote-peer**](cmdqueryname=display+igmp-snooping+group-info+remote-peer) command in any view to check dynamically learned multicast group information on remote peers.