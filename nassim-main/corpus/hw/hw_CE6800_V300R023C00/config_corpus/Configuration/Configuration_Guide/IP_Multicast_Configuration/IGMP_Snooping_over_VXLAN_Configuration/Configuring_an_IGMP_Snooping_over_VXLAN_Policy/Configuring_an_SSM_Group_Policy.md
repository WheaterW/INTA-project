Configuring an SSM Group Policy
===============================

Configuring an SSM Group Policy

#### Prerequisites

Before configuring an SSM group policy, create ACL rules for the policy. For details about ACL configuration, see [ACL Configuration](vrp_acl_cfg_0001.html). By default, the **deny** action in an ACL rule configured for an SSM group policy applies to all multicast groups. To exclude a multicast group address from the SSM group address range, you need to run the **[**rule**](cmdqueryname=rule) **permit** **source** **any**** command.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BD view.
   
   
   ```
   [bridge-domain](cmdqueryname=bridge-domain) bd-id
   ```
3. Configure an SSM group policy.
   
   
   ```
   [igmp snooping ssm-policy](cmdqueryname=igmp+snooping+ssm-policy) { basic-acl-number | acl-name acl-name }
   ```
   
   
   
   After an SSM group policy is configured, the multicast groups permitted by the policy are processed as SSM groups.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```