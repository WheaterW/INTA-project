Setting an SSM Group Address Range
==================================

Protocol Independent Multicast-Source-Specific Multicast (PIM-SSM) and PIM-SM have different group address ranges. If the group that a host joins is in the SSM group address range, PIM-SSM is adopted for multicast data forwarding; otherwise, PIM-SM is adopted. The default SSM group address range is 232.0.0.0/8, and the SSM group address range can be modified.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Ensure that the SSM group address ranges of all Routers are the same. Otherwise, faults may occur.



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
     
     1. Run [**acl**](cmdqueryname=acl) **name**  *basic-acl-name* **basic** [ **match-order** { **auto** | **config** } ]
        
        A named ACL is created, and the named ACL view is displayed.
     2. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** }
        
        Rules are configured for the named ACL.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**pim**](cmdqueryname=pim) [ **vpn-instance***vpn-instance-name* ]
   
   
   
   The PIM view is displayed.
5. Run [**ssm-policy**](cmdqueryname=ssm-policy) { *basic-acl-number* | **acl-name** *acl-name* }
   
   
   
   An SSM group address range is configured.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * If a group address matches an ACL rule and the action is **permit**, the device determines that this group is in the SSM group address range.
   * If a group address matches an ACL rule and the action is **deny**, the device determines that this group is not in the SSM group address range.
   * If a group address does not match any ACL rule, the device determines that this group is not in the SSM group address range.
   * If a specified ACL does not exist or does not contain rules, the device determines that no groups are in the SSM group address range.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.