Configuring a Neighbor Filtering Policy
=======================================

Configuring a Neighbor Filtering Policy

#### Context

A neighbor filtering policy defines the range of permitted neighbor addresses. A device with such a policy discards Hello messages from neighbors that are not in this address range.


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
7. Configure a neighbor filtering policy.
   
   
   ```
   [pim ipv6 neighbor-policy](cmdqueryname=pim+ipv6+neighbor-policy) { basic-acl6-number | acl6-name acl6-name }
   ```
   
   A neighbor filtering policy defines the range of permitted neighbor addresses. A device with such a policy discards Hello messages from neighbors that are not in this address range.
   
   * If an ACL6 rule is matched and the action is **permit**, the device establishes neighbor relationships with the addresses in this range.
   * If an ACL6 rule is matched and the action is **deny**, the device does not set up any neighbor relationships with the addresses in this range.
   * If an ACL6 rule is not matched, the device does not set up any neighbor relationships with the addresses in this range.
   * If a specified ACL6 does not exist or does not contain rules, the device does not establish a neighbor relationship with any other devices using any address.
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```