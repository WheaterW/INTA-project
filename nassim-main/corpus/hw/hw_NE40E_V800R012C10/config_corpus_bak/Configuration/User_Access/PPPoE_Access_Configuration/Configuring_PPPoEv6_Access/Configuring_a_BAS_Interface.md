Configuring a BAS Interface
===========================

If an interface is used for broadband user access, you must configure it as a BAS interface and set an access type and other attributes.

#### Context

When configuring a BAS interface, you need the following information:

* BAS interface number
* Access type and authentication method
* (Optional) Specify domains on the BAS interface.
* (Optional) Additional functions of the BAS interface
* (Optional) Packet processing methods

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number* [*. subinterface-number* ]
   
   
   
   The interface view is displayed.
3. Run [**bas**](cmdqueryname=bas)
   
   
   
   A BAS interface is created, and its view is displayed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   You can configure an interface as the BAS interface by running the [**bas**](cmdqueryname=bas) command in the interface view. An Ethernet interface or its sub-interface, or an Eth-Trunk interface or its sub-interface can be configured as a BAS interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
5. Configure an access type.
   
   
   * Run [**access-type**](cmdqueryname=access-type) **layer2-subscriber** [ **default-domain** [ **authentication** *dname* ] ]
     
     The access type is set to Layer 2 subscriber access, and attributes are configured for this access type.
6. Configure an authentication method.
   
   
   
   Run [**authentication-method-ipv6**](cmdqueryname=authentication-method-ipv6) **ppp** [ **web** ]
   
   PPP or PPP+web authentication is configured for IPv6 users.
7. (Optional) Specify domains on the BAS interface.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The [**permit-domain**](cmdqueryname=permit-domain) command cannot be configured together with the [**deny-domain**](cmdqueryname=deny-domain), [**deny-domain-list**](cmdqueryname=deny-domain-list), or [**permit-domain-list**](cmdqueryname=permit-domain-list) command on a BAS interface.
   
   * Default authentication domain
     
     To configure a default authentication domain, run the [**default-domain**](cmdqueryname=default-domain) **authentication** *domain-name* command.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     To specify the default authentication domain for PPP users, run the [**default-domain authentication ppp-user**](cmdqueryname=default-domain+authentication+ppp-user) *domain-name* command.
     
     + If the [**default-domain authentication ppp-user**](cmdqueryname=default-domain+authentication+ppp-user) *domain-name* command is configured, the authentication domain specified in this step is used as the default authentication domain for PPP users.
     + If the [**default-domain authentication ppp-user**](cmdqueryname=default-domain+authentication+ppp-user) *domain-name* command is not configured but the [**default-domain**](cmdqueryname=default-domain) **authentication** [ **force** | **replace** ] *domain-name* command is configured, the authentication domain specified using the [**default-domain**](cmdqueryname=default-domain) **authentication** [ **force** | **replace** ] *domain-name* command is used as the default authentication domain for PPP users.
     + If neither of the commands is configured, the default authentication domain for PPP users is default1.
   * Roaming domain
     
     To configure a roaming domain, run the [**roam-domain**](cmdqueryname=roam-domain) *domain-name* command.
   * Domains whose users are allowed to access the BAS interface
     
     To configure a domain for user access, run the [**permit-domain**](cmdqueryname=permit-domain) *domain-name* &**count** command.
   * Domains whose users are denied access to the BAS interface
     
     To configure domains whose users are denied access to the BAS interface, run the [**deny-domain**](cmdqueryname=deny-domain) *domain-name* &<1-16> command.
     
     To configure a list of domains whose users are denied access to the BAS interface, run the [**deny-domain-list**](cmdqueryname=deny-domain-list) **domainlist-name** command.
8. (Optional) Additional functions of the BAS interface
   
   
   * Configure the accounting packet copy function.
     
     Run [**accounting-copy**](cmdqueryname=accounting-copy) **radius-server** *radius-name*
     
     The accounting packet copy function is enabled.
   * Configure user detection parameters.
     
     Run [**user detect**](cmdqueryname=user+detect) **retransmit** *num* **interval** *time*
     
     User detection parameters are configured.
   * Block the BAS interface.
     
     Run [**block**](cmdqueryname=block) [ **start-vlan** { *start-vlan* [ **end-vlan** *end-vlan* ] [ **qinq** *qinq-vlan* ] | **any** **qinq** *start-qinq-vlan* [ *end-qinq-vlan* ] } ]
     
     The BAS interface is blocked.
   * Limit the number of users on the BAS interface.
     
     Run [**access-limit**](cmdqueryname=access-limit) *user-number*
     
     The number of users on the BAS interface is limited.
     
     If the command is run and the VLAN information is specified, the number of users in specified VLAN(s) on the BAS interface is limited.
     
     If the command is run and the VLAN information is not specified, the number of users in each VLAN on the BAS interface is limited. If the two types of configurations coexist on a BAS interface, they do not conflict. The number of users in the specified VLAN is subject to the limit set for the specified VLAN. The number of users in any one of the other unspecified VLANs is subject to the limit set on the BAS interface.
   * (Optional) Run [**client-replace enable**](cmdqueryname=client-replace+enable)
     
     The device is enabled to log out an existing user when a new user whose login request packets carry the same VLAN information as the existing user requests to go online from the same BAS interface.
9. (Optional) Configure packet processing methods.
   
   
   * Configure a method for processing access-line-id information.
     
     Run [**client-option82**](cmdqueryname=client-option82) [ **basinfo-insert** { **cn-telecom** | **version3** } | **version1** ] or [**client-access-line-id**](cmdqueryname=client-access-line-id) [ **basinfo-insert** { **cn-telecom** | **version3** } | **version1** ]
     
     The NE40E is configured to trust the access-line-id information sent from the client.
     
     Or run [**basinfo-insert cn-telecom**](cmdqueryname=basinfo-insert+cn-telecom)
     
     The NE40E is configured to distrust the access-line-id information sent from the client and insert the access-line-id information in the format defined by cn-telecom.
     
     Or run [**basinfo-insert version2**](cmdqueryname=basinfo-insert+version2)
     
     The NE40E is configured to insert the access-line-id information in the format defined by **version2** if the NE40E does not trust the access-line-id information sent from the client.
     
     The Router transmits access-line-id information to the RADIUS server based on the following configurations:
     + If the [**option82-relay-mode dslam**](cmdqueryname=option82-relay-mode+dslam) { **auto-identify** | **config-identify** } or [**access-line-id dslam**](cmdqueryname=access-line-id+dslam) { **auto-identify** | **config-identify** } command is run, the device fills in the Agent-CircuitID attribute and Agent-RemoteID attribute to be sent to the RADIUS server with a DSLAM's access-line-id field. If the [**option82-relay-mode include**](cmdqueryname=option82-relay-mode+include) { **allvalue** | { **agent-circuit-id** | **agent-remote-id** [ *separator* ] }\* } or [**access-line-id include**](cmdqueryname=access-line-id+include) { **allvalue** | { **agent-circuit-id** | **agent-remote-id** [ *separator* ] }\* } command is run, the device is configured to include the access-line-id information in the NAS-Port-Id attribute to be sent to the RADIUS server.
     + If the [**option82-relay-mode subopt**](cmdqueryname=option82-relay-mode+subopt) { **agent-circuit-id** { **hex** | **string** } | **agent-remote-id** { **hex** | **string** } }\* or [**access-line-id translate**](cmdqueryname=access-line-id+translate) { **agent-circuit-id** { **hex** | **string** } | **agent-remote-id** { **hex** | **string** } }\* command is run, the format in which the Agent-CircuitID or Agent-RemoteID attribute is sent is specified.
     
     Or run [**vbas**](cmdqueryname=vbas) *vbas-mac-address* [ **auth-mode** { **ignore** | **reject** } ]
     
     The function of locating a user through the virtual BAS (VBAS) is enabled.
   * (Optional) Configure a method for processing link-account information.
     
     Run [**link-account resolve**](cmdqueryname=link-account+resolve)
     
     The accounting-request packets carrying link-account information are sent to a RADIUS server.
     
     Before running the command, set the access type to Layer 2 subscriber access.
     
     The command affects RADIUS attribute 25 for accounting-request packets sent by the device to a RADIUS accounting server.
     
     An interface fills the link-account information in RADIUS attribute 25 **class** if both the following situations are met:
     + Users getting online from the interface do not need to be authenticated and RADIUS accounting is configured on the interface.
     + For common Layer 2 users, VLANs and VLAN descriptions are configured on the interface.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.