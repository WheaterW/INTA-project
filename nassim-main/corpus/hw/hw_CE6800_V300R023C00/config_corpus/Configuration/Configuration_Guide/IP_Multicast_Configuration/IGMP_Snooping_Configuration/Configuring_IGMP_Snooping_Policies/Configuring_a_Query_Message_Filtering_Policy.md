Configuring a Query Message Filtering Policy
============================================

Configuring a Query Message Filtering Policy

#### Context

If an attacker sends Query messages with a smaller querier IP address than the real IGMP querier on the network, devices running IGMP snooping consider the attacker to be a legitimate querier and forward IGMP Membership Report messages to the attacker. As a result, multicast traffic fails to be forwarded correctly. To address this issue, you can permit only IGMP Query messages with specified source IP addresses and reject other IGMP Query messages by configuring an IGMP Query message filtering policy. This improves the security of a Layer 2 multicast network.

This function must be used together with an ACL. An IGMP Query message is permitted only when its source IP address is within the permit range specified in the ACL rule.


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
   [igmp snooping query ip-source-policy](cmdqueryname=igmp+snooping+query+ip-source-policy) { acl-number | acl-name acl-name }  
   ```
   
   By default, no IGMP Query message filtering policy is configured in a VLAN.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```