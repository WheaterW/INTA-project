Configuring Static SSM Mapping
==============================

To allow IGMPv1 or IGMPv2 hosts to use the Source-Specific Multicast (SSM) service, configure static SSM mapping by establishing mappings between multicast groups and sources.

#### Context

If an IGMPv1 or IGMPv2 host requests multicast data from a specific multicast source, but the host's IGMP version cannot be upgraded to IGMPv3, configure a static SSM mapping policy to map the multicast group to the multicast source.

A static SSM mapping policy can be configured in the following situations: Interfaces in the same VPN share one SSM mapping.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**igmp**](cmdqueryname=igmp) [ **vpn-instance** *vpn-instance-name* ]
   
   
   
   The IGMP view is displayed.
3. Run [**ssm-mapping**](cmdqueryname=ssm-mapping) *group-address* { *mask* | *mask-length* } *source-address*
   
   
   
   A mapping is created between a multicast group and a multicast source. To map a multicast group to N (an integer) sources, run the command N times.
   
   
   
   * *group-address* { *mask* | *mask-length* }: specifies an IGMP group address and mask, which must be in the SSM group address range.
   * *SrcAddr*: specifies the address of a source to be mapped to the multicast group.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.