Setting an SSM Group Address Range
==================================

Setting an SSM Group Address Range

#### Context

The group address range in the PIM-SSM model is different from that in the PIM-SM model. If the address of the group that a user joins is within the SSM group address range, the PIM-SSM mode is used. Otherwise, the PIM-SM mode is used. The default SSM group address range is FF3x::/32. You can change the SSM group address range. When changing the SSM group address range, ensure that the SSM group address ranges configured on all devices on the network are the same. Otherwise, network faults may occur.


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
5. Enter the IPv6 PIM view.
   
   
   ```
   [pim ipv6](cmdqueryname=pim+ipv6) [ vpn-instance vpn-instance-name ]
   ```
6. Set an SSM group address range.
   
   
   ```
   [ssm-policy](cmdqueryname=ssm-policy) { basic-acl6-number | acl6-name acl6-name }
   ```
   
   
   
   The ACL6 takes effect as follows:
   
   * If a multicast group address matches the ACL6 rule and the action is **permit**, the device forwards the packets corresponding to the multicast group address in SSM mode.
   * If a multicast group address matches the ACL6 rule and the action is **deny**, the device refuses to forward the packets corresponding to the multicast group address in SSM mode.
   * If a multicast group address does not match the ACL6 rule, the device refuses to forward the packets corresponding to the multicast group address in SSM mode.
   * If a specified ACL6 does not exist or does not contain rules, no SSM group address range is configured.
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```