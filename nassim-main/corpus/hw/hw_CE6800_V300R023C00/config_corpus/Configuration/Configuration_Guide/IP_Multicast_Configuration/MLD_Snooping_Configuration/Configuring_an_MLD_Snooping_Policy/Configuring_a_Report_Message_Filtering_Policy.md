Configuring a Report Message Filtering Policy
=============================================

Configuring a Report Message Filtering Policy

#### Context

To improve multicast service security, you can configure a policy to filter out the MLD Report messages sent by hosts that initiate attacks. After a Report message filtering policy is configured, the hosts in the VLAN can dynamically join only the multicast groups matching ACL6 rules.

This function must be used together with an ACL6. A basic ACL6 can be used to filter MLD Report messages with specified source addresses. An advanced ACL6 can be used to filter MLD Report messages based on source and destination IP addresses.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VLAN view.
   
   
   ```
   [vlan](cmdqueryname=vlan) vlan-id
   ```
3. Configure a Report message filtering policy.
   
   
   ```
   [mld snooping ip-source-policy](cmdqueryname=mld+snooping+ip-source-policy) { acl6-number | acl6-name acl6-name }
   ```
   
   By default, no Report message filtering policy is configured in a VLAN.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```