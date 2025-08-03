Configuring Static SSM Mapping
==============================

To allow MLDv1 hosts to use the Source-Specific Multicast (SSM) service, configure static SSM mapping by establishing mappings between multicast groups and sources.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mld**](cmdqueryname=mld)
   
   
   
   The MLD view is displayed.
3. Run [**ssm-mapping**](cmdqueryname=ssm-mapping) *ipv6-group-address* *ipv6-group-mask-length* *ipv6-source-address*
   
   
   
   A mapping is created between a multicast group and a multicast source.
   
   
   
   * *ipv6-group-address* *ipv6-group-mask-length*: specifies an MLD group address and mask, which must be in the SSM group address range.
   * *ipv6-source-address*: specifies an IPv6 multicast source address to be mapped to the MLD group address.
   
   To map a multicast group to N (an integer) sources, run the [**ssm-mapping**](cmdqueryname=ssm-mapping) command N times.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.