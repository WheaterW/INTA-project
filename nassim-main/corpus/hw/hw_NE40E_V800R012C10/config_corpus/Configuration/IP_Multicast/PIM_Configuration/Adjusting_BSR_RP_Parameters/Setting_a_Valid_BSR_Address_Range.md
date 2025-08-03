Setting a Valid BSR Address Range
=================================

You can create ACL rules on all devices to filter BootStrap router (BSR) addresses. The devices then receive only the Bootstrap messages with the source addresses being in the valid BSR address range. Thus, BSR spoofing is prevented.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure a basic numbered ACL or a named ACL as needed.
   
   
   * Configure a basic numbered ACL.
     
     1. Run [**acl**](cmdqueryname=acl) [ **number** ] *basic-acl-number* [ **match-order** { **auto** | **config** } ]
        
        A basic numbered ACL is created, and the basic numbered ACL view is displayed.
     2. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** }
        
        Rules are configured for the basic numbered ACL.
   * Configure a named ACL.
     
     1. Run [**acl**](cmdqueryname=acl)**name***acl-name* **basic** [ **match-order** { **auto** | **config** } ]
        
        A named ACL is created, and the named ACL view is displayed.
     2. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** }
        
        Rules are configured for the named ACL.
   
   If a basic numbered ACL is used, run the [**rule**](cmdqueryname=rule) command and set the **source** parameter to the source address range of multicast packets.
   
   If a named ACL is used, run the [**rule**](cmdqueryname=rule) command and set the **source** parameter to the source address range of multicast packets.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**pim**](cmdqueryname=pim) [ **vpn-instance***vpn-instance-name* ]
   
   
   
   The PIM view is displayed.
5. Run [**bsr-policy**](cmdqueryname=bsr-policy) { *bsrPolicyAclNum* | **acl-name** *acl-name* }
   
   
   
   A valid BSR address range is set.
   
   
   
   * If the source address carried in a Bootstrap message is denied by the ACL or no action is defined in the ACL for processing such a Bootstrap message, the Router discards the Bootstrap message.
   * If no ACL rule corresponding to the specified *basic-acl-number* exists, the Router denies all Bootstrap messages.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * If a BSR message matches an ACL rule and the action is **permit**, the device permits this message.
   * If a BSR message matches an ACL rule and the action is **deny**, the device denies this message.
   * If a BSR message does not match any ACL rule, the device denies this message.
   * If a specified ACL does not exist or does not contain rules, the device denies all BSR messages.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.