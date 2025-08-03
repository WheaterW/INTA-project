Configuring a Limit on the C-RP Address Range
=============================================

Configuring a Limit on the C-RP Address Range

#### Context

On an IPv6 PIM-SM network that uses the BSR mechanism, any multicast device can be configured as a C-RP to serve the multicast group within a specified address range. C-RPs unicast C-RP information to the BSR. The BSR summarizes all collected C-RP information into an RP-Set, and floods the RP-Set through BSR messages on the entire network. Then, each multicast device locally calculates the RP corresponding to the specific group address range according to the RP-Set.

To prevent C-RP spoofing, you need to configure the range of valid C-RP addresses on the BSR to limit the range of multicast groups that can be served. You need to configure the same filtering policy on each C-BSR because each C-BSR may become the BSR.


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
   
   In the [**rule**](cmdqueryname=rule) command, the **source** parameter is used to specify a multicast source address, and the **destination** parameter is used to specify a multicast group address.
4. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
5. Enter the PIM view.
   
   
   ```
   [pim ipv6](cmdqueryname=pim+ipv6) [vpn-instance vpn-instance-name ]
   ```
6. Set the range of valid C-RP addresses.
   
   
   ```
   [c-rp policy](cmdqueryname=c-rp+policy) { advanced-acl-number| acl6-name acl6-name }
   ```
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```