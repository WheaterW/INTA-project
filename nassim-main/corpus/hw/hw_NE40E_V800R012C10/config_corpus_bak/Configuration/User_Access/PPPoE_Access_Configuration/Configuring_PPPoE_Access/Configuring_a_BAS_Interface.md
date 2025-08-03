Configuring a BAS Interface
===========================

If an interface is used for broadband access, you must configure it as a BAS interface. Before PPPoE users use a BAS interface to access a network, you must specify the access type as Layer 2 subscriber access.

#### Context

When configuring a BAS interface, you need the following information:

* BAS interface number
* Access type and authentication method
* (Optional) Maximum number of users who are allowed to access through the BAS interface and maximum number of users who are allowed to access through a specified VLAN
* (Optional) Default domain, roaming domain, and domains that users are allowed to access on the BAS interface
* (Optional) Whether to enable the functions of accounting packet copy and locating a user

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**bas**](cmdqueryname=bas)
   
   
   
   A BAS interface is created and the BAS interface view is displayed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * In scenarios of BRAS access through L2VPN termination, users need to go online through a VE interface. Before entering the interface view, you need to run the [**ve-group**](cmdqueryname=ve-group) *ve-group-id* **l2-terminate** command to configure the VE interface as an L2VE interface that terminates an L2VPN and bind the L2VE interface to a VE-group.
   * You can configure an interface as the BAS interface by running the [**bas**](cmdqueryname=bas) command in the interface view. A GE interface or its sub-interface or an Eth-Trunk interface or its sub-interface can be configured as a BAS interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
5. Run [**access-type**](cmdqueryname=access-type) **layer2-subscriber** [ **default-domain** { **authentication** [ **force** | **replace** ] *dname* | **pre-authentication** *predname* } \* | **bas-interface-name** *bname* | **accounting-copy** **radius-server** *rd-name* ] \*
   
   
   
   The access type is set to Layer 2 subscriber access, and attributes are configured for this access type.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * When setting the access type on the BAS interface, you can set service attributes for the access users at the same time. You can also set these attributes in later configurations.
   * The access type cannot be configured on an Ethernet interface that has been added to an Eth-Trunk interface. You can configure the access type of such an Ethernet interface only on the associated Eth-Trunk interface.
6. (Optional) Run [**access-limit**](cmdqueryname=access-limit) *user-number*
   
   
   
   The number of users who are allowed to access through the interface is configured.
   
   
   
   * If the **access-limit** command is configured on a sub-interface enabled with BAS, the number of VLAN users who access the sub-interface is limited.
   * If this command is configured on a BAS main interface and no VLAN is specified, the maximum number of access users in all VLANs bound to the main interface is limited. If the maximum number of access users in a VLAN or VLAN range has been set on a BAS sub-interface, the configuration on the BAS sub-interface takes precedence over that on the BAS main interface. The configuration on the BAS main interface takes effect if no VLAN is specified.
7. (Optional) Run [**client-replace enable**](cmdqueryname=client-replace+enable)
   
   
   
   The function to log out an online user when a new user in the same VLAN goes online from the same BAS interface is enabled.
8. (Optional) Run [**default-domain**](cmdqueryname=default-domain) **pre-authentication** *domain-name*
   
   
   
   The default pre-authentication domain is specified. By default, the pre-authentication domain of the BAS interface is default0.
   
   
   
   * Or run [**default-domain authentication**](cmdqueryname=default-domain+authentication) [ **force** | **replace** ] *domain-name*
     
     The default authentication domain is specified. By default, the authentication domain of the BAS interface is default1.
   * Or run [**default-domain authentication ppp-user**](cmdqueryname=default-domain+authentication+ppp-user) *domain-name*
     
     The default authentication domain for PPP users is specified.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + If the [**default-domain authentication ppp-user**](cmdqueryname=default-domain+authentication+ppp-user) *domain-name* command is configured, the authentication domain specified in this step is used as the default authentication domain for PPP users.
     + If the [**default-domain authentication ppp-user**](cmdqueryname=default-domain+authentication+ppp-user) *domain-name* command is not configured but the [**default-domain**](cmdqueryname=default-domain) **authentication** [ **force** | **replace** ] *domain-name* command is configured, the authentication domain specified using the [**default-domain**](cmdqueryname=default-domain) **authentication** [ **force** | **replace** ] *domain-name* command is used as the default authentication domain for PPP users.
     + If neither of the commands is configured, the default authentication domain for PPP users is default1.
   * Or run [**roam-domain**](cmdqueryname=roam-domain) *domain-name*
     
     The roaming domain is specified.
     
     By default, the roaming domain of the BAS interface is default1.
   * Or run [**permit-domain**](cmdqueryname=permit-domain) *domain-name* &<1-16>
     
     The domain in which users are allowed to access is specified.
     
     By default, no domain for user access is specified on a BAS interface. This means that users from all domains are allowed to access.
     
     Or run [**deny-domain**](cmdqueryname=deny-domain) *domain-name* <1-16>
     
     The domains whose users are denied access to the BAS interface are configured.
     
     The [**permit-domain-list**](cmdqueryname=permit-domain-list) command cannot be configured together with the [**deny-domain-list**](cmdqueryname=deny-domain-list), [**deny-domain**](cmdqueryname=deny-domain), or [**permit-domain**](cmdqueryname=permit-domain) command on a BAS interface.
   * Or run [**permit-domain-list**](cmdqueryname=permit-domain-list) *domainlist-name*
     
     The list of domains whose users are allowed to access is specified.
     
     Or run [**deny-domain-list**](cmdqueryname=deny-domain-list) *domainlist-name*
     
     The list of domains whose users are denied to access is specified.
     
     By default, no domain for user access is specified on a BAS interface. Users are allowed to access all domains.
9. (Optional) Run either of the following commands:
   
   
   
   To configure the NE40E to trust the access-line-id information reported by the client, run the [**client-option82**](cmdqueryname=client-option82) [ **basinfo-insert** { **cn-telecom** [ **version2** ] | **version3** } | **version1** ] or [**client-access-line-id**](cmdqueryname=client-access-line-id) [ **basinfo-insert** { **cn-telecom** [ **version2** ] | **version3** } | **version1** ] command.
   
   
   
   To configure the NE40E to insert the access-line-id information in the cn-telecom format when it does not trust the access-line-id information reported by the client, run the [**basinfo-insert cn-telecom**](cmdqueryname=basinfo-insert+cn-telecom) command.
   
   To configure the NE40E to insert the access-line-id information in version2 format when it does not trust the access-line-id information reported by the client, run the [**basinfo-insert version2**](cmdqueryname=basinfo-insert+version2) command.
   
   
   
   The NE40E transmits access-line-id information to the RADIUS server based on the following configurations:
   
   * If the [**option82-relay-mode dslam**](cmdqueryname=option82-relay-mode+dslam) { **auto-identify** | **config-identify** } command is run, the device fills in the Agent-Circuit-Id attribute and Agent-Remote-Id attribute to be sent to the RADIUS server with a DSLAM's access-line-id field. If the [**option82-relay-mode include**](cmdqueryname=option82-relay-mode+include) { **allvalue** | { **agent-circuit-id** | **agent-remote-id** [ *separator* ] }\* } command is run, the device is configured to add access-line-id information to the NAS-Port-Id attribute of packets to be sent to the RADIUS server.
   * If the [**option82-relay-mode subopt**](cmdqueryname=option82-relay-mode+subopt) { **agent-circuit-id** { **hex** | *string* } | **agent-remote-id** { **hex** | *string* } }\* command is run, the format in which the Agent-Circuit-Id or Agent-Remote-Id attribute is sent is specified.
   
   
   
   To enable the function of locating a user in virtual BAS (VBAS) mode, run the [**vbas**](cmdqueryname=vbas) *vbas-mac-address* [ **auth-mode** { **ignore** | **reject** } ] command.
10. (Optional) Run [**link-account resolve**](cmdqueryname=link-account+resolve)
    
    
    
    The NE40E is enabled to carry link-account information in an Accounting-Request packet to be sent to a RADIUS server.
    
    
    
    Before running the command, set the access type to Layer 2 subscriber access.
    
    The command affects the RADIUS No. 25 attribute in Accounting-Request packets sent by the device to a RADIUS accounting server.
    
    Link-account information is filled into the RADIUS No. 25 attribute (Class) if both of the following conditions are met:
    * None authentication and RADIUS accounting are configured for users going online through the interface.
    * For Layer 2 common users, VLANs and VLAN descriptions are configured on the interface.
11. (Optional) Run [**accounting-copy radius-server**](cmdqueryname=accounting-copy+radius-server) *radius-name*
    
    
    
    The accounting packet copy function is enabled.
12. (Optional) Run [**block**](cmdqueryname=block) [ **start-vlan** { *start-vlan* [ **end-vlan** *end-vlan* ] [ **qinq** *qinq-vlan* ] | **any** **qinq** *start-qinq-vlan* [ *end-qinq-vlan* ] } ]
    
    
    
    The BAS interface is blocked.
    
    
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    If you run the [**block start-vlan any qinq**](cmdqueryname=block+start-vlan+any+qinq) command in the interface view to set the interface to be blocked, all the users who go online from this interface with a specified VLAN ID are prohibited from access.
13. (Optional) Run [**authentication-method**](cmdqueryname=authentication-method) **ppp** [ **web** ]
    
    
    
    PPP or PPP+web authentication is configured.
14. (Optional) Run [**ppp keepalive slow**](cmdqueryname=ppp+keepalive+slow)
    
    
    
    PPP slow reply is configured on the BAS interface, allowing the BAS interface to send PPP echo packets to the CPU for processing.
15. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.