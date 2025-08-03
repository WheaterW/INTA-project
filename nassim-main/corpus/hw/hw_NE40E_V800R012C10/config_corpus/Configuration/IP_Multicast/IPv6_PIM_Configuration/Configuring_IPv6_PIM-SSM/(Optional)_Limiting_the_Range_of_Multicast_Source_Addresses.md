(Optional) Limiting the Range of Multicast Source Addresses
===========================================================

You can configure multicast source addresses-based filtering policies by creating IPv6 ACLs. Then, an IPv6 PIM Router forwards only the multicast packets whose source address or source/group addresses match the IPv6 ACLs.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure a basic or an advanced ACL6 as needed.
   
   
   * Configure a basic ACL6.
     
     1. Run [**acl ipv6**](cmdqueryname=acl+ipv6) [ **number** ] *basic-acl6-number* [ **match-order** { **auto** | **config** } ]
        
        A basic ACL6 is created, and the basic ACL6 view is displayed.
     2. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment** | **source** { *source-ipv6-address* *prefix-length* | *source-ipv6-address*/*prefix-length* | **any** } ] \*
        
        Rules are configured for the basic ACL6.
   * Configure an advanced ACL6.
     1. Run [**acl ipv6**](cmdqueryname=acl+ipv6) { **name** *advance-acl6-name* [ **advance** | [ **advance** ] **number** *advance-acl6-number* ] | [ **number** ] *advance-acl6-number* } [ **match-order** { **config** | **auto** } ]
        
        An advanced ACL6 is created, and the advanced ACL6 view is displayed.
     2. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **ipv6** [ **destination** { *destination-ipv6-address* *prefix-length* | *destination-ipv6-address*/*prefix-length* | **any** } | **source** { *source-ipv6-address* *prefix-length* | *source-ipv6-address*/*prefix-length* | **any** } ] \*
        
        Rules are configured for the advanced ACL6.
   
   If a basic ACL6 is used, run the [**rule**](cmdqueryname=rule) command and set the **source** parameter to a multicast source address.
   
   If an advanced ACL6 is used, run the [**rule**](cmdqueryname=rule) command, set the **source** parameter to a multicast source address, and set the **destination** parameter to a multicast group address.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**pim-ipv6**](cmdqueryname=pim-ipv6)
   
   
   
   The IPv6 PIM view is displayed.
5. Run [**source-policy**](cmdqueryname=source-policy) { *acl6-number* | **acl6-name** *acl6-name* }
   
   
   
   A multicast source address range is configured.
   
   The [**source-policy**](cmdqueryname=source-policy) command configuration cannot be used to filter static (S, G) entries.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * If a multicast data packet matches an ACL rule and the action is **permit**, the device permits this packet.
   * If a multicast data packet matches an ACL rule and the action is **deny**, the device denies this packet.
   * If a multicast data packet does not match any ACL rule, the device denies this packet.
   * If a specified ACL does not exist or does not contain rules, the device denies all multicast data packets.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.