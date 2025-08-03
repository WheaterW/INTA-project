(Optional) Configuring an SSM Group Address Range
=================================================

After a multicast group is configured within a Source-Specific Multicast (SSM) group address range, user hosts that join the group can use SSM services.

#### Context

If the address of the group that a user joins is within the Any-Source Multicast (ASM) group address range but the user wants to use IGMPv3 services, you can configure this group's address to be within the SSM group address range and then configure Layer 2 SSM mapping.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**acl**](cmdqueryname=acl) { **number** *basic-acl-number* | **name** *acl-name* }
   
   
   
   The basic ACL view is displayed.
3. Run [**rule**](cmdqueryname=rule) **permit** **source** *source-ip-address* *source-wildcard*
   
   
   
   A rule is configured for the basic ACL.
4. (Optional) Run [**rule**](cmdqueryname=rule) **deny** **source** **any**
   
   
   
   Multicast group addresses beyond the range defined in the ACL rule are considered as ASM addresses.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The ACL created for an SSM group address range can only take effect when you select the **permit** parameter in the [**rule**](cmdqueryname=rule) command and specify a multicast group address. If the **deny** parameter is specified in the [**rule**](cmdqueryname=rule) command or the specified address is not a multicast group address, the ACL will not take effect.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
6. Perform either of the following operations based on the VLAN or VPLS networking:
   
   
   * To enter the VLAN view, run the [**vlan**](cmdqueryname=vlan) *vlan-id* command.
   * To enter the VSI view, run the [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** ] command.
7. Run [**igmp-snooping ssm-policy**](cmdqueryname=igmp-snooping+ssm-policy){ <*SsmPolicyAclNumValue*> | *acl-name* <*SsmPolicyAclNameValue*> }
   
   
   
   A specified multicast address is added to the SSM group address range.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.