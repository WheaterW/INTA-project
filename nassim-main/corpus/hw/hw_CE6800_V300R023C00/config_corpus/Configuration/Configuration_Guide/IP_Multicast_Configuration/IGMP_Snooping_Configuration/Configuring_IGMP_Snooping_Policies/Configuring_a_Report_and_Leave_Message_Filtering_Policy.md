Configuring a Report/Leave Message Filtering Policy
===================================================

Configuring a Report/Leave Message Filtering Policy

#### Context

To improve multicast service security, you can configure a policy to filter out the IGMP Report/Leave messages sent from hosts that initiate attacks.

This function must be used together with an ACL. A basic ACL enables you to filter IGMP Report/Leave messages based on specified source addresses, whereas an advanced ACL enables you to filter such messages based on specified source and destination IP addresses.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VLAN view.
   
   
   ```
   [vlan](cmdqueryname=vlan) vlan-id
   ```
3. Configure a Report/Leave message filtering policy to allow hosts in the VLAN to dynamically join only the multicast groups that match specified ACL rules.
   
   
   ```
   [igmp snooping ip-source-policy](cmdqueryname=igmp+snooping+ip-source-policy) { acl-number | acl-name acl-name }
   ```
   
   By default, no Report/Leave message filtering policy is configured in a VLAN.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```