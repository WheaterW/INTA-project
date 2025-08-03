Configuring a Join Information Filtering Policy
===============================================

Configuring a Join Information Filtering Policy

#### Context

To prevent unauthorized users from joining a multicast group, configure a join information filtering policy to specify a permitted source address range for join information in Join/Prune messages.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create an ACL6 and enter the ACL6 view.
   
   
   ```
   [acl ipv6](cmdqueryname=acl+ipv6) { name basic-acl6-name basic | [ number ] basic-acl6-number }
   ```
3. Configure a rule for the ACL6.
   
   
   ```
   [rule](cmdqueryname=rule) [ rule-id ] [ name rule-name ] { permit | deny } [ fragment | source { source-ipv6-address { prefix-length | source-wildcard } | source-ipv6-address/prefix-length | any } | time-range time-name | vpn-instance vpn-instance-name | logging ] *
   ```
4. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
5. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
6. Switch the interface working mode from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
7. Configure a join information filtering policy to specify the permitted source address range of join information.
   
   
   ```
   [pim ipv6 join-policy](cmdqueryname=pim+ipv6+join-policy) { basic-acl6-number | {acl6-name acl6-name } | { asm { asm-basic-acl6-number | acl6-name asm-acl6-name } | ssm { ssm-basic-acl6-number | acl6-name ssm-acl6-name }}}
   ```
   
   When defining an ACL6 rule, you can use the **permit** parameter to enable the device to accept only the Join messages with addresses in the specified address range. If no ACL6 [**rule**](cmdqueryname=rule) is defined, the interface filters out join information of any address range in Join/Prune messages by default.
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```