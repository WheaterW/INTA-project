Configuring IPv6 SSM Mapping
============================

Some hosts can run only MLDv1. To enable such hosts to obtain the MLDv2 service, configure SSM mapping.

#### Context

Compared to the traditional any-source multicast (ASM) technology, source-specific multicast (SSM) can conserve multicast addresses and has higher security, but MLDv2 only supports SSM. The majority of the latest multicast devices support MLDv2, but most legacy multicast terminals only support MLDv1 and hope to enjoy the MLDv2 multicast service. SSM mapping enables the compatibility in the SSM range by supporting hosts running MLDv1.

When the upstream Layer 3 device runs MLDv2, SSM mapping maps (\*, G) information in MLDv1 messages to (S, G) information in MLDv2 messages. In this manner, hosts running MLD of an earlier version can also obtain multicast services within the SSM group address range.

If a user joins an ASM group and wants to use MLDv2 services, add the multicast group address to the SSM group address range and then configure Layer 2 SSM mapping.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**acl ipv6**](cmdqueryname=acl+ipv6) { **number** *basic-acl6-number* | **name** *basic-acl-name* }
   
   
   
   The ACL6 view is displayed.
3. Run [**rule**](cmdqueryname=rule) **permit** **source** *source-ipv6-address* *prefix-length*
   
   
   
   A rule is configured for the basic ACL.
4. (Optional) Run [**rule**](cmdqueryname=rule) **deny** **source** **any**
   
   
   
   The device is configured to process other multicast group addresses as ASM ones.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Set **permit** in the [**rule**](cmdqueryname=rule) command when configuring a rule for the ACL6. Otherwise, the SSM group range configuration does not take effect. If you set **deny** or the specified address is not a multicast address, the configuration does not take effect either.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
6. Perform either of the following operations based on the VLAN or VPLS networking:
   
   
   * To enter the VLAN view, run the [**vlan**](cmdqueryname=vlan) *vlan-id* command.
   * To enter the VSI view, run the [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** ] command.
7. Run [**mld-snooping enable**](cmdqueryname=mld-snooping+enable)
   
   
   
   MLD snooping is enabled for the VLAN or VSI.
8. Run [**mld-snooping version 2**](cmdqueryname=mld-snooping+version+2)
   
   
   
   MLDv2 is set as the version of MLD snooping.
9. Run [**mld-snooping ssm-policy**](cmdqueryname=mld-snooping+ssm-policy) { *basic-acl6-number* | **acl6-name** *acl6-name* }
   
   
   
   The specified multicast address is added to the SSM group address range.
10. Run [**mld-snooping ssm-mapping enable**](cmdqueryname=mld-snooping+ssm-mapping+enable) **policy** *policy-name*
    
    
    
    SSM mapping is enabled for the VLAN or VSI.
11. Run [**mld-snooping ssm-mapping**](cmdqueryname=mld-snooping+ssm-mapping) *group-address* *mask-length* *source-address*
    
    
    
    The multicast address in the specified range is mapped to a specified source address.
    
    
    
    The specified multicast address is in the SSM address range.
12. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.