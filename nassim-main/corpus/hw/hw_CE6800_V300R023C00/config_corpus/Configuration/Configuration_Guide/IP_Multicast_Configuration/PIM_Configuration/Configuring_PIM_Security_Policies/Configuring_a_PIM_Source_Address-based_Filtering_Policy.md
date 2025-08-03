Configuring a PIM Source Address-based Filtering Policy
=======================================================

Configuring a PIM Source Address-based Filtering Policy

#### Context

You can configure a multicast source address-based filtering policy through an ACL so that a PIM device forwards only the multicast packets whose source addresses or source/group addresses match the ACL.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure a type of ACL as required.
   
   
   * Configure a basic ACL.
     ```
     [acl](cmdqueryname=acl) [ number ] basic-acl-number 
     ```
     
     Configure an ACL rule.
     
     ```
     [rule](cmdqueryname=rule) [ rule-id ] [ name rule-name ] { deny | permit } source { source-ip-address { source-wildcard | 0 } | any }
     ```
     
     If a basic ACL is used, set the **source** parameter in the **rule** command to the source address of multicast data packets.
   * Configure an advanced ACL.
     ```
     [acl](cmdqueryname=acl) { name advance-acl-name [ advance | [ advance ] number advance-acl-number ] | [ number ] advance-acl-number } [ match-order { config | auto } ]
     ```
     
     Configure an ACL rule.
     
     ```
     [rule](cmdqueryname=rule) [ rule-id ] [ name rule-name ] { deny | permit } ip [ destination { destination-ip-address { destination-wildcard | 0 } | any } | source { source-ip-address { source-wildcard | 0 } | any } ]
     ```
     
     If an advanced ACL is used, in the **rule** command, set the **source** parameter to the source address of multicast data packets, and set the **destination** parameter to a multicast group address.
3. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
4. Enter the PIM view.
   
   
   ```
   [pim](cmdqueryname=pim) [vpn-instance vpn-instance-name ]
   ```
5. Limit the range of source addresses.
   
   
   ```
   [source-policy](cmdqueryname=source-policy) { acl-number | acl-name acl-name }
   ```
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```