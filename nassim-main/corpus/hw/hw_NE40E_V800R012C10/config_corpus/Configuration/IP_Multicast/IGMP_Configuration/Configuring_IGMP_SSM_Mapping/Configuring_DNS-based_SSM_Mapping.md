Configuring DNS-based SSM Mapping
=================================

This section describes how to configure DNS-based SSM mapping on the multicast device connecting to the user network segment, so that the multicast device can obtain the multicast source corresponding to the multicast group through the DNS server and provide the SSM service for users.

#### Context

The DNS-based SSM mapping function allows the multicast device enabled with SSM mapping to dynamically obtain the source-group mapping from the DNS server, so that the multicast device provides the SSM service for users in the group.

This function can be configured when each VPN corresponds to an SSM mapping relationship.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**igmp**](cmdqueryname=igmp) [ **vpn-instance** *vpn-instance-name* ]
   
   
   
   The IGMP view is displayed.
3. Run [**ssm-mapping query dns**](cmdqueryname=ssm-mapping+query+dns) [ **policy** { *basic-acl-number* | **acl-name** *basic-acl-name* ]
   
   
   
   The DNS-based SSM mapping function is enabled.
4. Run [**ssm-mapping domain**](cmdqueryname=ssm-mapping+domain) *domain-name*
   
   
   
   The domain name suffix added to a multicast group address for SSM mapping is specified.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
6. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
7. Run [**igmp static-group**](cmdqueryname=igmp+static-group) *group-address* **source** **dns-ssm-map**
   
   
   
   The function of obtaining the multicast source address from a DNS server is configured.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.