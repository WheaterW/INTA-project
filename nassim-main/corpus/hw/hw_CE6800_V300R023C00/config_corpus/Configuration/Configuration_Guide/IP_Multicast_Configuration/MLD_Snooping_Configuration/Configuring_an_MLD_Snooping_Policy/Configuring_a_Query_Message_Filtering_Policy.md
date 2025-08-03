Configuring a Query Message Filtering Policy
============================================

Configuring a Query Message Filtering Policy

#### Context

If an attacker sends Query messages with a smaller querier IP address than the real MLD querier on the network, devices running MLD snooping consider the attacker as a legitimate querier and forward MLD Report messages to the network interface of the attacker. As a result, multicast traffic fails to be forwarded correctly. To address this issue, you can permit only MLD Query messages with specified source IP addresses and reject other MLD Query messages by configuring an MLD Query message filtering policy. This improves the security of a Layer 2 multicast network.

This function must be used together with an ACL6. An MLD Query message is permitted only when its source IP address is within the permit range specified in the ACL6 rule.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VLAN view.
   
   
   ```
   [vlan](cmdqueryname=vlan) vlan-id
   ```
3. Configure a Query message filtering policy.
   
   
   ```
   [mld snooping query ip-source-policy](cmdqueryname=mld+snooping+query+ip-source-policy) { acl6-number | acl6-name acl6-name }  
   ```
   
   By default, no MLD Query message filtering policy is configured in a VLAN.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```