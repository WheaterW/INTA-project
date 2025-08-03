Configuring a BAS interface
===========================

When an interface is used for broadband access, you need to configure it as a BAS interface and set the access type and relevant attributes for this interface.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number* [*. subinterface-number*  ]
   
   
   
   The user-side interface view is displayed.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
4. Run [**bas**](cmdqueryname=bas)
   
   
   
   A BAS interface is created, and the BAS interface view is displayed.
   
   
   
   You can configure an interface as the BAS interface by running the [**bas**](cmdqueryname=bas) command in the interface view. An Ethernet interface, an Eth-Trunk interface, a Virtual Ethernet (VE) interface or a sub-interface of the preceding interfaces can be configured as a BAS interface.
5. Perform one or more operations in [Table 1](#EN-US_TASK_0172374176__tab_1) to set the desired interface parameters.
   
   
   
   **Table 1** Configure a BAS interface.
   | BAS Interface Parameter | Command | Description |
   | --- | --- | --- |
   | Access type and relevant attributes for Layer 2 common users | [**access-type**](cmdqueryname=access-type) [**layer2-subscriber**](cmdqueryname=layer2-subscriber) [ [**default-domain**](cmdqueryname=default-domain) { [**authentication**](cmdqueryname=authentication) [ [**force**](cmdqueryname=force) | [**replace**](cmdqueryname=replace) ] *dname* | [**pre-authentication**](cmdqueryname=pre-authentication) *prename* } \* | [**bas-interface-name**](cmdqueryname=bas-interface-name) *bname* | [**accounting-copy**](cmdqueryname=accounting-copy) [**radius-server**](cmdqueryname=radius-server) *rd-name* ] \* | Configure a user who accesses a network from a BAS interface as a Layer 2 common user, allowing such users to have independent service attributes and directly access a Layer 2 network. A BRAS performs authentication and accounting on these users separately. When setting the access type on the BAS interface, you can set the service attributes of the access users at the same time or later. The access type cannot be configured on the Ethernet interface that is added to an Eth-Trunk interface. You can configure the access type only on the Eth-Trunk interface. |
   | User authentication method | [**authentication-method**](cmdqueryname=authentication-method) | Configure 802.1X authentication for user access through a BAS interface. |
   | Maximum number of users on a BAS interface | [**access-limit**](cmdqueryname=access-limit) *user-number* | Limit the number of online users in a domain. If the number of online users exceeds the specified upper limit, the system rejects users' access requests and notifies the users of authentication failures. This facilitates the management of access users. |
   | The function to trust the access-line-id information reported by clients | [**client-option82**](cmdqueryname=client-option82) [ { **basinfo-insert** { **cn-telecom** | **version3** } | **version1** } ] | Enable the function to locate a user through DHCP Option 82 or PPPoE+. |
   | The function to enable VBAS on a BAS interface | [**vbas**](cmdqueryname=vbas) | Enable the function to locate a user through the virtual BAS (VBAS). You do not need to run this command if the function to locate a user through DHCP Option 82 or PPPoE+ is enabled. |
   | The function to enable the NE40E to carry link-account information in the accounting request packets sent to a RADIUS server | [**link-account resolve**](cmdqueryname=link-account+resolve) | When a RADIUS server performs accounting for users who go online in non-authentication mode, the server needs to differentiate users. Run this command to enable the NE40E to carry link-account information in the accounting request packets sent to the RADIUS server. |
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.