(Optional) Configuring an SSM Group Address Range
=================================================

(Optional) Configuring an SSM Group Address Range

#### Context

By default, SSM group addresses range from 232.0.0.0 to 232.255.255.255. If a requested multicast group address is outside of the SSM group address range, configure an SSM group policy in the VLAN to add the group address to the range.

![](../public_sys-resources/note_3.0-en-us.png) 

By default, the **deny** action in an ACL rule configured for an SSM policy applies to all multicast groups. To exclude a multicast group address from the SSM group address range, you also need to run the **rule permit source any** command.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VLAN view.
   
   
   ```
   [vlan](cmdqueryname=vlan) vlan-id
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