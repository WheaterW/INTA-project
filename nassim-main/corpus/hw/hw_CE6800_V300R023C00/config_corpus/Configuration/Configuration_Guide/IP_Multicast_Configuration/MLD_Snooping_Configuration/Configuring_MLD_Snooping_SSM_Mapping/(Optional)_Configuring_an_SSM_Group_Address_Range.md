(Optional) Configuring an SSM Group Address Range
=================================================

(Optional) Configuring an SSM Group Address Range

#### Context

By default, the SSM IPv6 group address range is FF3x::/32 (x cannot be 1 or 2). If the address of the multicast group that a user joins is not in the SSM group address range, configure an SSM group policy in the VLAN to add the group address to the range.

![](../public_sys-resources/note_3.0-en-us.png) 

By default, the **deny** action in an ACL6 rule configured for an SSM policy applies to all multicast groups. To exclude a multicast group address from the SSM group address range, you also need to run the **rule permit source any** command.



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
   [ssm-mapping ipv6 policy](cmdqueryname=ssm-mapping+ipv6+policy) policy-name
   ```
   
   After an SSM group policy is configured, the multicast groups permitted by the policy are processed as SSM groups.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```