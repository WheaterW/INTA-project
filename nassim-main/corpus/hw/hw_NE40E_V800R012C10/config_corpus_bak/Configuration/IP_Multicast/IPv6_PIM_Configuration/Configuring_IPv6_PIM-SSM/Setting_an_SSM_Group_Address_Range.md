Setting an SSM Group Address Range
==================================

The group address range in the Protocol Independent Multicast-Source-Specific Multicast (PIM-SSM) model is different from that in the PIM-SM model. If a multicast group that a user wants to join is within the SSM group address range, the PIM-SSM model is used to forward packets. If a multicast group that a user wants to join is beyond the SSM group address range, the PIM-SM model is used to forward packets. In PIM-SSM model, the default group address range is FF3x::/32. The SSM group address range can be changed as needed.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

Ensure that the SSM group address ranges of all Routers on an IPv6 network are the same. Otherwise, faults may occur.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure a basic numbered ACL6 or a named ACL6 as needed.
   
   
   * Configure a basic numbered ACL6.
     
     1. Run [**acl ipv6**](cmdqueryname=acl+ipv6) [ **number** ] *basic-acl6-number* [ **match-order** { **auto** | **config** } ]
        
        A basic numbered ACL6 is created, and the basic numbered ACL6 view is displayed.
     2. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment** | **source** { *source-ipv6-address* *prefix-length* | *source-ipv6-address*/*prefix-length* | **any** } ] \*
        
        Rules are configured for the basic numbered ACL6.
   * Configure a named ACL6.
     1. Run [**acl ipv6**](cmdqueryname=acl+ipv6) **name** *basic-acl6-name* **basic** [ **match-order** { **auto** | **config** } ]
        
        A named ACL6 is created, and the named ACL6 view is displayed.
     2. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment** | **source** { *source-ipv6-address* *prefix-length* | *source-ipv6-address*/*prefix-length* | **any** } ] \*
        
        Rules are configured for the named ACL6.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**pim-ipv6**](cmdqueryname=pim-ipv6)
   
   
   
   The IPv6 PIM view is displayed.
5. Run [**ssm-policy**](cmdqueryname=ssm-policy) { *basic-acl6-number* | **acl6-name** *acl6-name* }
   
   
   
   An SSM group address range is set.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * If a group address matches an ACL rule and the action is **permit**, the device determines that this group is in the SSM group address range.
   * If a group address matches an ACL rule and the action is **deny**, the device determines that this group is not in the SSM group address range.
   * If a group address does not match any ACL rule, the device determines that this group is not in the SSM group address range.
   * If a specified ACL does not exist or does not contain rules, the device determines that no groups are in the SSM group address range.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.