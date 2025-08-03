Configuring Static SSM Mapping
==============================

Configuring Static SSM Mapping

#### Context

After a static SSM mapping policy is configured on an interface, the interface maps multicast groups to sources based on the configured mapping policy. In this way, the multicast device running a later version is compatible with hosts running an earlier version and can provide the SSM service for these hosts.

A mapping from a multicast group to a multicast source can be configured in the IGMP view or SSM mapping policy view.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure a mapping from a multicast group to a multicast source.
   
   
   * Perform the configuration in the IGMP view.
     ```
     [igmp](cmdqueryname=igmp) [ vpn-instance vpn-instance-name ]
     [ssm-mapping](cmdqueryname=ssm-mapping) group-address { mask | mask-length } source-address
     ```
   * Perform the configuration in the SSM mapping policy view.
     ```
     [ssm-mapping policy](cmdqueryname=ssm-mapping+policy) policy-name
     [group](cmdqueryname=group) group-address { mask-length | mask } source source-address
     ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```