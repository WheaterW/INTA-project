Setting a Valid BSR Address Range
=================================

You can create IPv6 ACL rules on all devices to filter BootStrap router (BSR) addresses. The devices then receive only the Bootstrap messages with the source addresses being in the valid BSR address range. Thus, BSR spoofing is prevented.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure a basic numbered ACL6 or a naming ACL6 as needed.
   
   
   * Configure a basic numbered ACL6.
     
     1. Run [**acl ipv6**](cmdqueryname=acl+ipv6) [ **number** ] *basic-acl6-number* [ **match-order** { **auto** | **config** } ]
        
        A basic numbered ACL6 is created, and the basic numbered ACL6 view is displayed.
     2. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment** | **source** { *source-ipv6-address* *prefix-length* | *source-ipv6-address*/*prefix-length* | **any** } ] \*
        
        Rules are configured for the basic numbered ACL6.
   * Configure a naming ACL6.
     1. Run [**acl ipv6**](cmdqueryname=acl+ipv6) **name** *acl6-name* **basic** [ **match-order** { **auto** | **config** } ]
        
        A naming ACL6 is created, and the naming ACL6 view is displayed.
     2. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment** | **source** { *source-ipv6-address* *prefix-length* | *source-ipv6-address*/*prefix-length* | **any** } ] \*
        
        Rules are configured for the naming ACL6.
   
   If a basic numbered ACL6 is used, run the [**rule**](cmdqueryname=rule) command and set the **source** parameter to the source address range of multicast packets.
   
   If a naming ACL6 is used, run the [**rule**](cmdqueryname=rule) command and set the **source** parameter to the source address range of multicast packets.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**pim-ipv6**](cmdqueryname=pim-ipv6)
   
   
   
   The IPv6 PIM view is displayed.
5. Run [**bsr-policy**](cmdqueryname=bsr-policy) { *basic-acl6-number* | **acl6-name** *acl6-name* }
   
   
   
   A valid BSR address range is set.
   
   
   
   * If the source address carried in a Bootstrap message is denied by the IPv6 ACL or no action is defined in the IPv6 ACL for processing such a Bootstrap message, the Router discards this Bootstrap message.
   * If *basic-acl6-number* or **acl6-name** *acl6-name* is specified but the corresponding IPv6 ACL is not configured, the Router denies all Bootstrap messages.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * If a BSR message matches an ACL rule and the action is **permit**, the device permits this message.
   * If a BSR message matches an ACL rule and the action is **deny**, the device denies this message.
   * If a BSR message does not match any ACL rule, the device denies this message.
   * If a specified ACL does not exist or does not contain rules, the device denies all BSR messages.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.