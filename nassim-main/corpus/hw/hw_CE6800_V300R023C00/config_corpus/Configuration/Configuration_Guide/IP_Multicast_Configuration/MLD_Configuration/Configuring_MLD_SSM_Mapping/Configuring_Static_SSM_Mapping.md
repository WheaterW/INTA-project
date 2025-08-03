Configuring Static SSM Mapping
==============================

Configuring Static SSM Mapping

#### Context

After a static SSM mapping policy is configured on an interface, the interface maps multicast groups to sources based on the configured mapping policy. In this way, a multicast device running a later version is compatible with hosts running an earlier version and can provide the SSM service for these hosts.

A mapping from a multicast group to a multicast source can be configured in the MLD view or SSM mapping policy view.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the MLD view.
   
   
   ```
   [mld](cmdqueryname=mld)
   ```
3. Configure a mapping from a multicast group to a multicast source.
   
   
   ```
   [ssm-mapping](cmdqueryname=ssm-mapping) ipv6-group-address ipv6-group-mask-length ipv6-source-address
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```