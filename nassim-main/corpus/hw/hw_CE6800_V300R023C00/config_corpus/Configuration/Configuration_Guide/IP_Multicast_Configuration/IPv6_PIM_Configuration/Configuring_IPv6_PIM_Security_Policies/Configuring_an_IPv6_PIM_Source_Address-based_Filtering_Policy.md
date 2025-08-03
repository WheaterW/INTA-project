Configuring an IPv6 PIM Source Address-based Filtering Policy
=============================================================

Configuring an IPv6 PIM Source Address-based Filtering Policy

#### Context

You can configure a multicast source address-based filtering policy through an ACL6 so that an IPv6 PIM device forwards only the multicast packets whose source addresses or source and group addresses match the ACL6.


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
   [pim ipv6](cmdqueryname=pim+ipv6) [vpn-instance vpn-instance-name ]
   ```
6. Limit the range of source addresses.
   
   
   ```
   [source-policy](cmdqueryname=source-policy) { acl6-number | acl6-name acl6-name }
   ```
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```