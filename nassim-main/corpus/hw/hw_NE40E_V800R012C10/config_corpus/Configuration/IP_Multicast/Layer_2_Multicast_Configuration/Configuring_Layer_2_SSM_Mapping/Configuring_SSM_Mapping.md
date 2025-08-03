Configuring SSM Mapping
=======================

To provide SSM services for old-fashioned multicast terminals that support only IGMPv1 or IGMPv2, configure SSM mapping on the terminals. The SSM mapping mechanism is used to convert IGMPv1 and IGMPv2 Report messages into messages with (S, G) information. It allows hosts that do not support IGMPv3 to enjoy SSM services. SSM mapping allows the mapping to be established between a multicast group and a multicast source.

#### Context

If IGMPv3 snooping is running in a VLAN or VSI but user hosts run IGMPv1 or IGMPv2, SSM mapping must be configured in the VLAN or VSI so that these user hosts can enjoy SSM services.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) Run [**ssm-mapping policy**](cmdqueryname=ssm-mapping+policy) *policy-name*
   
   
   
   An IPv4 SSM mapping policy is configured, and the IPv4 SSM mapping policy view is displayed.
3. (Optional) Run [**group**](cmdqueryname=group) *group-address* { *mask-length* | *mask* } **source** *source-address*
   
   
   
   A static SSM mapping is created between a multicast group and a multicast source in the IPv4 SSM mapping policy. To map a multicast group to multiple sources, run this command multiple times.
4. Perform either of the following operations based on the VLAN or VPLS networking:
   
   
   * To enter the VLAN view, run the [**vlan**](cmdqueryname=vlan) *vlan-id* command.
   * To enter the VSI view, run the [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** ] command.
5. Run [**igmp-snooping enable**](cmdqueryname=igmp-snooping+enable)
   
   
   
   IGMP snooping is enabled for the VLAN or VSI.
6. Run [**igmp-snooping version 3**](cmdqueryname=igmp-snooping+version+3)
   
   
   
   The version number of IGMP snooping is set to 3.
7. Run [**igmp-snooping ssm-mapping enable**](cmdqueryname=igmp-snooping+ssm-mapping+enable) **policy** *policy-name*
   
   
   
   SSM mapping is enabled for the VLAN or VSI.
   
   The SSM mapping policy specified by **policy** must have been configured using the [**ssm-mapping policy**](cmdqueryname=ssm-mapping+policy) command.
8. Run [**igmp-snooping ssm-mapping**](cmdqueryname=igmp-snooping+ssm-mapping) *ip-group-address* { *ip-group-mask* | *mask-length* } *ip-source-address*
   
   
   
   The multicast address in the specified range is mapped to the source address.
   
   The configured multicast address must be within the SSM group address range.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.