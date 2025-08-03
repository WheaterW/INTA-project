Configuring a Query Message Filtering Policy
============================================

Configuring a Query Message Filtering Policy

#### Prerequisites

Before configuring a policy for filtering IGMP Query messages, configure an ACL to permit IGMP Query messages with the source IP address in a specified range. For details about ACL configuration, see [ACL Configuration](vrp_acl_cfg_0001.html).


#### Context

A source address-based IGMP Query message filtering policy filters IGMP Query messages based on specified ACL rules, improving Layer 2 multicast network security.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BD view.
   
   
   ```
   [bridge-domain](cmdqueryname=bridge-domain) bd-id
   ```
3. Configure a Query message filtering policy.
   
   
   ```
   [igmp snooping query ip-source-policy](cmdqueryname=igmp+snooping+query+ip-source-policy) { acl-number | acl-name acl-name }
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```