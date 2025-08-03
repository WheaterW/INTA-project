(Optional) Setting a Multicast Source Address Range
===================================================

You can configure multicast source addresses-based filtering policies by creating ACLs. Then, a PIM Router forwards only the multicast packets whose source address or source/group addresses match the ACLs.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure a basic or an advanced ACL as needed.
   
   
   * Configure a basic ACL.
     
     1. Run [**acl**](cmdqueryname=acl) [ **number** ] *basic-acl-number* [ **match-order** { **auto** | **config** } ]
        
        A basic ACL is created, and the basic ACL view is displayed.
     2. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** }
        
        Rules are configured for the basic ACL.
   * Configure an advanced ACL.
     
     1. Run [**acl**](cmdqueryname=acl) { **name** *advance-acl-name* [ **advance** | [ **advance** ] **number** *advance-acl-number* ] | [ **number** ] *advance-acl-number* } [ **match-order** { **config** | **auto** } ]
        
        An advanced ACL is created, and the advanced ACL view is displayed.
     2. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **ip** [ **destination** { *destination-ip-address* { *destination-wildcard* | **0** } | **any** } | **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** } ] \*
        
        Rules are configured for the advanced ACL.
   
   If a basic ACL is used, run the [**rule**](cmdqueryname=rule) command and set the **source** parameter to a multicast source address.
   
   If an advanced ACL is used, run the [**rule**](cmdqueryname=rule) command, set the **source** parameter to a multicast source address, and set the **destination** parameter to a multicast group address.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**pim**](cmdqueryname=pim) [ **vpn-instance***vpn-instance-name* ]
   
   
   
   The PIM view is displayed.
5. Run [**source-policy**](cmdqueryname=source-policy) { *acl-number* | **acl-name** *acl-name* }
   
   
   
   A multicast source address range is configured.
   
   The [**source-policy**](cmdqueryname=source-policy) command configuration cannot be used to filter static (S, G) entries.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * If a multicast data packet matches an ACL rule and the action is **permit**, the device permits this packet.
   * If a multicast data packet matches an ACL rule and the action is **deny**, the device denies this packet.
   * If a multicast data packet does not match any ACL rule, the device denies this packet.
   * If a specified ACL does not exist or does not contain rules, the device denies all multicast data packets.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.