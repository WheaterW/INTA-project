Configuring a Limit on the C-RP Address Range
=============================================

Configuring a Limit on the C-RP Address Range

#### Context

On a PIM-SM network that uses the BSR mechanism, any multicast device can be configured as a candidate-rendezvous point (C-RP) to serve the multicast group within a specified address range. C-RPs unicast C-RP information to the BSR. The BSR summarizes all collected C-RP information as an RP-set, and floods the RP-set through BSR messages on the entire network. Then, each multicast device locally calculates the RP corresponding to the specific group address range according to the RP-Set.

To prevent C-RP spoofing, you need to configure the range of valid C-RP addresses on the BSR to limit the range of multicast groups that can be served. You need to configure the same filtering policy on each C-BSR because each C-BSR may become the BSR.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create an advanced ACL and enter the ACL view.
   
   
   ```
   [acl](cmdqueryname=acl) { name advance-acl-name [ advance | [ advance ] number advance-acl-number ] | [ number ] advance-acl-number } [ match-order { config | auto } ]
   ```
3. Configure a rule for the advanced ACL.
   
   
   ```
   [rule](cmdqueryname=rule) [ rule-id ] [ name rule-name ] { deny | permit } ip [ destination { destination-ip-address { destination-wildcard | 0 } | any } | source { source-ip-address { source-wildcard | 0 } | any } ]
   ```
   
   
   
   In the [**rule**](cmdqueryname=rule) command, the **source** parameter is used to specify a multicast source address, and the **destination** parameter is used to specify a multicast group address.
4. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
5. Enter the PIM view.
   
   
   ```
   [pim](cmdqueryname=pim) [ vpn-instance vpn-instance-name ]
   ```
6. Set the range of valid C-RP addresses.
   
   
   ```
   [c-rp policy](cmdqueryname=c-rp+policy) { policyNum | acl-name acl-name }
   ```
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```