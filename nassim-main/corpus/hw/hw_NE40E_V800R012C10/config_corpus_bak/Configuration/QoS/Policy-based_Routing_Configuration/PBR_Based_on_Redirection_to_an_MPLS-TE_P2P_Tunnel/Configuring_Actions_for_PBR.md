Configuring Actions for PBR
===========================

Configuring_Actions_for_PBR

#### Context

Each **node** in each policy for PBR needs to be configured with rules and an action. The action is redirecting matching IP packets to an outbound interface.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**policy-based-route**](cmdqueryname=policy-based-route) *policy-name* **permit** **node** *node-id* **map-instance** *map-instance-id*
   
   
   
   A policy or node is created, and the policy-based-route view is displayed.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   A maximum of 100 policies can be configured.
   
   A maximum of 200 nodes can be configured.
   
   The *map-instance-id* value must be the same as the *node-id* value.
3. Run [**if-match acl**](cmdqueryname=if-match+acl) **name** *acl-name*
   
   
   
   An ACL is configured to match against IP addresses.
4. Run [**apply output-interface**](cmdqueryname=apply+output-interface) { *interface-name* | *interface-type* *interface-number* }
   
   
   
   The outbound interface to which packets are redirected is specified.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The outbound interface can only be a P2P TE tunnel interface. If the tunnel type is changed, the configuration is deleted automatically for the PBR.
   
   The format of *tunnel-name* can be either of the following:
   * **Tunnel** *interface-number*. The format of *interface-number* is x/y/z.
   * **Tunnel** *tunnel-number*. The value of *tunnel-number* is an integer ranging from 0 to 4294967295.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.