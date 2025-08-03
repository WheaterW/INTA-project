Configuring LAC-Side User Access
================================

This section describes how to configure LAC-side user access to implement control and accounting for each access host.

#### Context

In L2TP access scenarios, users access the network through a LAC. Therefore, you need to configure an access mode and access interface on the LAC.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface virtual-template**](cmdqueryname=interface+virtual-template) *vt-number*
   
   
   
   A VT is created and its view is displayed, or the view of an existing VT is displayed.
3. Run [**ppp authentication-mode**](cmdqueryname=ppp+authentication-mode) { **auto** | { **pap** | **chap** | **mschapv1** | **mschapv2** } \* }
   
   
   
   A PPP authentication mode is configured.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
5. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number* [ . *subinterface-number* ]
   
   
   
   The interface or sub-interface view is displayed.
   
   
   
   This interface is the physical interface through which users go online. The main interface view is displayed for PPPoE access users and the sub-interface view is displayed for PPPoEoVLAN access users.
6. Run [**pppoe-server bind**](cmdqueryname=pppoe-server+bind) **virtual-template** *virtual-template-number*
   
   
   
   The interface or sub-interface is bound to the VT.
7. Run [**user-vlan**](cmdqueryname=user-vlan) { *start-vlan* [ *end-vlan* ] [ **qinq** *start-qinq-id* [ *end-qinq-id* ] ] | **any-other** }
   
   
   
   User-side VLANs are created.
8. Run [**bas**](cmdqueryname=bas)
   
   
   
   The interface or sub-interface is configured as a BAS interface, and the BAS interface view is displayed.
9. Run [**access-type**](cmdqueryname=access-type) **layer2-subscriber** [ **default-domain** { **authentication** [ **force** | **replace** ] *dname* | **pre-authentication** *predname* } \* | **bas-interface-name** *bname* | **accounting-copy** **radius-server** *rd-name* ] \*
   
   
   
   An access type and relevant attributes are configured for Layer 2 access users.
   
   
   
   When setting an access type for a BAS interface, you can set the service attributes of the access users at the same time or later.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.