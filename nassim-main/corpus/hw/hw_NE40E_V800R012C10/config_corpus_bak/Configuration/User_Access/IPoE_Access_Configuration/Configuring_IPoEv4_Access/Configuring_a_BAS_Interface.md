Configuring a BAS Interface
===========================

When an interface is used for broadband access, you need to configure it as a BAS interface, and then specify the user access type and attributes for the interface.

#### Context

When configuring a BAS interface, you need the following parameters:

* BAS interface number
* Access type and authentication scheme
* (Optional) Maximum number of users allowed access through the BAS interface and maximum number of users allowed access in a specified VLAN
* (Optional) Default domain, roaming domain, and domains that users are allowed to access on the BAS interface
* (Optional) Whether to enable proxy ARP, DHCP broadcast, accounting packet copy, IP packet-triggered user login, and user-based multicast replication
* (Optional) Whether to trust client-reported Access-Line-Id information, user detection parameters, VPN instances of non-PPP users, and BAS interface name

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* For security purposes, use an eight-character or longer password that contains at least two types of the following: uppercase letters, lowercase letters, digits, and special characters.
* You are advised to configure your password in ciphertext mode and change it periodically.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number* [*. subinterface-number* ]
   
   
   
   The interface view is displayed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * In scenarios of BRAS access through L2VPN termination, users need to go online through a VE interface. Before entering the interface view, run the [**ve-group**](cmdqueryname=ve-group) *ve-group-id* **l2-terminate** command to configure a VE interface as an L2VE interface to terminate an L2VPN and bind the interface to a VE-group.
   * In scenarios of BRAS access through L3VPN termination, users need to go online through a VE interface. Before entering the interface view, run the [**ve-group**](cmdqueryname=ve-group) *ve-group-id* **l3-terminate** command to configure a VE interface as an L3VE interface to terminate an L3VPN and bind the interface to a VE-group. Only Layer 3 static user access is supported in scenarios of BRAS access through L3VPN termination. For details, see [[**Example for Configuring BRAS Access Through L3VPN Termination**](cmdqueryname=Example+for+Configuring+BRAS+Access+Through+L3VPN+Termination)](dc_ne_cfg_014579.html).
3. Run [**bas**](cmdqueryname=bas)
   
   
   
   A BAS interface is created, and its view is displayed.
   
   
   
   To configure an interface as a BAS interface, run the [**bas**](cmdqueryname=bas) command in the interface view.
4. Configure a user access type and related attributes:
   
   
   * To set the access type to Layer 2 common users and configure related attributes, run the [**access-type**](cmdqueryname=access-type) **layer2-subscriber** [ **bas-interface-name** *bname* | **default-domain** { **pre-authentication** *predname* | **authentication** [ **force** | **replace** ] *dname* } \* | **accounting-copy** **radius-server** *rd-name* ] \* command.
   * To configure the access type and related attributes for Layer 3 common users, run the [**access-type**](cmdqueryname=access-type) **layer3-subscriber** [ **default-domain** { [ **pre-authentication** *predname* ] **authentication** [ **force** | **replace** ] *dname* }\* ] command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     When setting the user access type on a BAS interface, you can set the service attributes of the access users at the same time or later.
     
     + To specify an IP address segment and an associated authentication domain name for Layer 3 common users, run the [**layer3-subscriber**](cmdqueryname=layer3-subscriber) { *start-ip-address* [ *end-ip-address* ] | *start-ipv6-address* [ *end-ipv6-address* ] | **delegation-prefix** *start-ipv6-address* [ *end-ipv6-address* ] [ *end-ip-address* ] *mask-length*} \* [ **vpn-instance** *instance-name* ] **domain-name** *domain-name* and [**layer3-subscriber ip-address any**](cmdqueryname=layer3-subscriber+ip-address+any) **domain-name** *domain-name* commands in the system view.
     + To specify an IPv4 address segment and an associated authentication domain name for Layer 3 static users using the mask mode, run the [**layer3-subscriber subnet-session**](cmdqueryname=layer3-subscriber+subnet-session) *start-ip-address* { *mask-address* | *mask-length* } [ **vpn-instance** *instance-name* ] **domain-name** *domain-name* command in the system view.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + The access type cannot be configured on an Ethernet interface that is added to an Eth-Trunk interface. You can configure the access type of such an Ethernet interface only on the associated Eth-Trunk interface.
     + When configuring static routes for Layer 3 users, specify the next hop as the user IP address and do not specify the outbound interface. Otherwise, network-to-user traffic may fail to be forwarded.
   
   
   * To set the access type and configure related attributes for Layer 2 or Layer 3 leased line users, run the [**access-type**](cmdqueryname=access-type) **layer2-leased-line** **user-name** *uname* **password** { **cipher** *password* | **simple** *password* } [ **bas-interface-name** *bname* | **default-domain** **authentication** *dname* | **accounting-copy** **radius-server** *rd-name* | **nas-port-type** { **async** | **sync** | **isdn-sync** | **isdn-async-v120** | **isdn-async-v110** | **virtual** | **piafs** | **hdlc** | **x.25** | **x.75** | **g.3-fax** | **sdsl** | **adsl-cap** | **adsl-dmt** | **idsl** | **ethernet** | **xdsl** | **cable** | **wireless-other** | **802.11** } ] \* or [**access-type**](cmdqueryname=access-type) **layer3-leased-line** { **user-name** *uname* | **user-name-template** } **password** { **cipher** *password* | **simple** *password* } [ **default-domain** **authentication** *dname* | **bas-interface-name** *bname* | **accounting-copy** **radius-server** *rd-name* | **nas-port-type** { **async** | **sync** | **isdn-sync** | **isdn-async-v120** | **isdn-async-v110** | **virtual** | **piafs** | **hdlc** | **x.25** | **x.75** | **g.3-fax** | **sdsl** | **adsl-cap** | **adsl-dmt** | **idsl** | **ethernet** | **xdsl** | **cable** | **wireless-other** | **802.11** } | **mac-address** *mac-address* | **client-id** *client-id* ] \* command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * If a BAS interface has an online user, you can change the access type of the BAS interface only when the online user is a leased line user.
   * After the access type is set to leased line access, the NE40E performs authentication on the leased line user immediately.
5. (Optional) Run [**trust 8021p-protocol**](cmdqueryname=trust+8021p-protocol)
   
   
   
   The BAS interface is configured to trust the 802.1p priority of user packets.
   
   
   
   The [**trust 8021p-protocol**](cmdqueryname=trust+8021p-protocol) command can be run only when the access type is set to Layer 2 common users.
6. (Optional) Run [**access-limit**](cmdqueryname=access-limit) *user-number* [ **start-vlan** *start-vlan* [ **end-vlan** *end-vlan* ] [ **qinq** *qinq-vlan* ] [ **user-type** { **ipoe** { **ipv4** | **ipv6** } | **pppoe** } ] ]
   
   
   
   The maximum number of users allowed access through the interface is configured.
   
   
   
   * If this command is configured on a BAS sub-interface, the maximum number of access users in a VLAN or VLAN range are limited.
   * If this command is configured on a BAS main interface and no VLAN is specified, the maximum number of access users in all VLANs bound to the main interface is limited. If the maximum number of access users in a VLAN or VLAN range has been set on a BAS sub-interface, the configuration on the BAS sub-interface takes precedence over that on the BAS main interface. The configuration on the BAS main interface takes effect if no VLAN is specified.
   * You can also limit the maximum number of access users based on a specified access user type.
7. (Optional) Run [**client-replace enable**](cmdqueryname=client-replace+enable)
   
   
   
   The device is enabled to log out an existing user when a new user whose login request packets carry the same VLAN information as the former requests to go online from the same BAS interface.
8. (Optional) Run **[**default-user-name include user-defined**](cmdqueryname=default-user-name+include+user-defined)** **uname** **[**ipoe**](cmdqueryname=ipoe)**
   
   
   
   A username is specified for a Layer 2 IPoE user on the BAS interface.
   
   
   
   You need to run this command if a username needs to be specified for a Layer 2 IPoE user accessing through an interface. The username specified using this command takes precedence over that generated using the username template.
9. (Optional) Configure a domain.
   * To specify the default pre-authentication domain, run the [**default-domain**](cmdqueryname=default-domain) **pre-authentication** *domain-name* command.
   * To specify the default authentication domain, run the [**default-domain**](cmdqueryname=default-domain) **authentication** [ **force** | **replace** ] *domain-name* command.
   * To specify domains whose users are allowed to access the BAS interface, run the [**permit-domain**](cmdqueryname=permit-domain) *domain-name* &<1-16> command.
     
     To specify domains whose users are denied access to the BAS interface, run the [**deny-domain**](cmdqueryname=deny-domain) *domain-name* &<1-16> command.
   * To specify a list of domains whose users are allowed to access the BAS interface, run the [**permit-domain-list**](cmdqueryname=permit-domain-list) command.
     
     To specify a list of domains whose users are denied access to the BAS interface, run the [**deny-domain-list**](cmdqueryname=deny-domain-list) command.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The [**permit-domain**](cmdqueryname=permit-domain) command cannot be used together with the [**deny-domain**](cmdqueryname=deny-domain), [**deny-domain-list**](cmdqueryname=deny-domain-list), or [**permit-domain-list**](cmdqueryname=permit-domain-list) command.
10. (Optional) Run either of the following commands:
    
    
    
    To configure the NE40E to trust the access-line-id information reported by the client, run the [**client-option82**](cmdqueryname=client-option82) [ **basinfo-insert** { **cn-telecom** [ **version2** ] | **version3** } | **version1** ] or [**client-access-line-id**](cmdqueryname=client-access-line-id) [ **basinfo-insert** { **cn-telecom** [ **version2** ] | **version3** } | **version1** ] command.
    
    
    
    To configure the NE40E to insert the access-line-id information in the cn-telecom format when it does not trust the access-line-id information reported by the client, run the [**basinfo-insert cn-telecom**](cmdqueryname=basinfo-insert+cn-telecom) command.
    
    To configure the NE40E to insert the access-line-id information in version2 format when it does not trust the access-line-id information reported by the client, run the [**basinfo-insert version2**](cmdqueryname=basinfo-insert+version2) command.
    
    
    
    The NE40E transmits access-line-id information to the RADIUS server based on the following configurations:
    
    * If the [**option82-relay-mode dslam**](cmdqueryname=option82-relay-mode+dslam) { **auto-identify** | **config-identify** } command is run, the device fills in the Agent-Circuit-Id attribute and Agent-Remote-Id attribute to be sent to the RADIUS server with a DSLAM's access-line-id field. If the [**option82-relay-mode include**](cmdqueryname=option82-relay-mode+include) { **allvalue** | { **agent-circuit-id** | **agent-remote-id** [ *separator* ] }\* } command is run, the device is configured to add access-line-id information to the NAS-Port-Id attribute of packets to be sent to the RADIUS server.
    * If the [**option82-relay-mode subopt**](cmdqueryname=option82-relay-mode+subopt) { **agent-circuit-id** { **hex** | *string* } | **agent-remote-id** { **hex** | *string* } }\* command is run, the format in which the Agent-Circuit-Id or Agent-Remote-Id attribute is sent is specified.
    
    
    
    To enable the function of locating a user in virtual BAS (VBAS) mode, run the [**vbas**](cmdqueryname=vbas) *vbas-mac-address* [ **auth-mode** { **ignore** | **reject** } ] command.
11. (Optional) Run [**access-line-id update online**](cmdqueryname=access-line-id+update+online)
    
    
    
    The device is enabled to update the Option 82 information of an online user through a DHCP Request message for lease renewal.
12. (Optional) Run [**dhcp option82-mismatch action offline**](cmdqueryname=dhcp+option82-mismatch+action+offline)
    
    
    
    The device is configured to log out an online user when the Option 82 information carried in the Discover, Request, or lease renewal messages sent by the user changes.
    
    
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    Before running this command, perform the following operations:
    
    * Run the [**access-type layer2-subscriber**](cmdqueryname=access-type+layer2-subscriber) or [**access-type layer2-leased-line**](cmdqueryname=access-type+layer2-leased-line) command to set the user type to Layer 2 subscriber access.
    * Run the [**client-option82**](cmdqueryname=client-option82) command to configure the device to trust the access-line-id information reported by a client.
13. (Optional) Run [**client-option60**](cmdqueryname=client-option60)
    
    
    
    The NE40E is configured to trust the Option 60 information reported by clients.
    
    
    
    If user domain information is obtained from Option 60, the character string following the domain name delimiter (@ is the default) in the Option 60 field is used as the domain name. If no user domain information is obtained from Option 60, the NE40E performs the following procedure to continue searching for the information. If there is no domain name delimiter in the field, the NE40E performs a fuzzy or exact match of the domain name information based on the configured mode. The procedure will stop if user domain information is obtained.
    
    * Check whether the [**client-option60**](cmdqueryname=client-option60) command is configured on the BAS interface. If the command is configured, obtain user domain information based on the command configuration.
    * Check whether the [**dhcp option-60**](cmdqueryname=dhcp+option-60) command is configured in the system view. If the command is configured, obtain user domain information based on the command configuration.
    * Use the authentication domain configured on the BAS interface as the user domain.
14. (Optional) Run [**option37-relay-mode include remote-id**](cmdqueryname=option37-relay-mode+include+remote-id)
    
    
    
    The device is enabled to discard the enterprise code in Option 37.
    
    
    
    The following operations must have been performed:
    
    * Run the [**client-option37**](cmdqueryname=client-option37) [ **basinfo-insert ft-telecom** ] command to enable the NE40E to trust the information in the Option 37 field of DHCPv6 messages sent by clients.
    * Run the [**client-option18**](cmdqueryname=client-option18) command to configure the NE40E to trust the information in the Option 18 field of DHCPv6 messages sent by clients.
15. (Optional) Run [**accounting-copy**](cmdqueryname=accounting-copy) **radius-server** *radius-name*
    
    
    
    The accounting packet copy function is enabled.
16. (Optional) Run [**link-account resolve**](cmdqueryname=link-account+resolve)
    
    
    
    The NE40E is enabled to carry link-account information in an Accounting-Request packet to be sent to a RADIUS server.
    
    
    
    Before running the command, set the access type to Layer 2 subscriber access.
    
    The command affects the RADIUS No. 25 attribute in Accounting-Request packets sent by the device to a RADIUS accounting server.
    
    Link-account information is filled into the RADIUS No. 25 attribute (Class) if both of the following conditions are met:
    * None authentication and RADIUS accounting are configured for users going online through the interface.
    * For Layer 2 common users, VLANs and VLAN descriptions are configured on the interface.
17. Perform the following configurations by service type:
    
    
    * For IPoE access services:
      
      Run the [**ip-trigger**](cmdqueryname=ip-trigger) command to enable user access triggered by IP packets or run the [**arp-trigger**](cmdqueryname=arp-trigger) command to enable user access triggered by ARP packets.
    * For IPoEv6 access services:
      
      Run the [**ipv6-trigger**](cmdqueryname=ipv6-trigger) command to enable user access triggered by IPv6 packets or run the [**nd-trigger**](cmdqueryname=nd-trigger) command to enable user access triggered by NS/NA packets.
18. (Optional) Run [**wlan-switch enable**](cmdqueryname=wlan-switch+enable) [ **switch-group** *switch-group-name* ]
    
    
    
    WLAN user roaming switchover is enabled.
    
    
    
    After WLAN user roaming switchover is enabled on a BAS interface, you need to configure the interface to use received user packets to trigger roaming procedures for WLAN users. Perform the following configurations based on specific roaming scenarios:
    * If users do not pass through areas without Wi-Fi signals when roaming between different APs, run the [**ip-trigger**](cmdqueryname=ip-trigger), [**arp-trigger**](cmdqueryname=arp-trigger), or [**ipv6-trigger**](cmdqueryname=ipv6-trigger) command to configure the interface to use received IP/ARP packets or NS/NA/IPv6 packets to trigger roaming procedures for the WLAN users. You can run either the [**ip-trigger**](cmdqueryname=ip-trigger) or [**arp-trigger**](cmdqueryname=arp-trigger) command, or both as required. To trigger roaming procedures for Layer 2 IPv6 users, run the [**ipv6-trigger**](cmdqueryname=ipv6-trigger) command.
    * If users pass through areas without Wi-Fi signals when roaming between different APs, run the [**dhcp session-mismatch**](cmdqueryname=dhcp+session-mismatch) **action** **roam** { [**ipv4**](cmdqueryname=ipv4) | **ipv6**| **nd** } \* command to configure the interface to allow users to send DHCPv4 Discover or Request messages, DHCPv6 Solicit messages, or ND RS messages for re-login.![](../../../../public_sys-resources/note_3.0-en-us.png) 
      + The [**dhcp session-mismatch**](cmdqueryname=dhcp+session-mismatch) **action** **roam** { [**ipv4**](cmdqueryname=ipv4) | **ipv6** | **nd** } \* and [**dhcp session-mismatch**](cmdqueryname=dhcp+session-mismatch) **action** **offline** commands override one another. If the two commands are run on the same interface, the command run later takes effect.
    
    After the preceding steps are performed, WLAN users do not need to be re-authenticated for login after being logged out when roaming between different APs. This ensures that services are not interrupted.
19. (Optional) Run [**user detect**](cmdqueryname=user+detect) **retransmit** *num* **interval** *time* [ **datacheck** ] or [**user detect**](cmdqueryname=user+detect) **datacheck**
    
    
    
    User detection parameters are configured.
20. (Optional) Run [**dhcp session-mismatch**](cmdqueryname=dhcp+session-mismatch) **action** **offline**
    
    
    
    The device is configured to log out online users whose physical location information is changed but MAC addresses remain unchanged when they resend DHCP or ND login requests.
21. (Optional) Run [**block**](cmdqueryname=block) [ **start-vlan** { *start-vlan* [ **end-vlan** *end-vlan* ] [ **qinq** *qinq-vlan* ] | **any** **qinq** *start-qinq-vlan* [ *end-qinq-vlan* ] } ]
    
    
    
    The BAS interface is blocked.
    
    
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    If you run the [**block start-vlan any qinq**](cmdqueryname=block+start-vlan+any+qinq) command in the interface view to set the interface to be blocked, all the users who go online from this interface with a specified VLAN ID are prohibited from access.
22. Run [**authentication-method**](cmdqueryname=authentication-method) { **bind** | { **dot1x** | **ppp** | { **fast** | **web** } } \* }
    
    
    
    An authentication method is configured.
    
    
    
    You can configure authentication methods for only Layer 2 users on BAS interfaces. Multiple authentication methods can be configured on a BAS interface but you should note the following:
    
    * Web authentication conflicts with fast authentication.
    * Binding authentication conflicts with the other authentication methods.
23. (Optional) Run [**select-authentication-domain individual**](cmdqueryname=select-authentication-domain+individual)
    
    
    
    The device is enabled to use the domain carried in an EAP username as the authentication domain for an EAP-authentication-based RADIUS proxy user.
24. (Optional) Run [**dhcp-reply trust broadcast-flag**](cmdqueryname=dhcp-reply+trust+broadcast-flag)
    
    
    
    The device is enabled to use the broadcast flag value in a DHCP request packet to determine the destination MAC address type for a DHCP response packet.
    
    
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    After the [**dhcp reply trust broadcast-flag**](cmdqueryname=dhcp+reply+trust+broadcast-flag) command is run, if the broadcast flag value in a DHCP request packet is 1, the device replies with a DHCP response packet that carries the broadcast address of all Fs as the destination MAC address; if the broadcast flag value in a DHCP request packet is 0, the device replies with a DHCP response packet that carries the user MAC address as the destination MAC address.
    
    The [**dhcp-reply trust broadcast-flag**](cmdqueryname=dhcp-reply+trust+broadcast-flag) command applies only to Layer 2 access users.
    
    The [**dhcp-reply trust broadcast-flag**](cmdqueryname=dhcp-reply+trust+broadcast-flag) command is mutually exclusive with the [**dhcp-broadcast**](cmdqueryname=dhcp-broadcast) command.
25. (Optional) Run [**dhcpv6 user-identify-policy**](cmdqueryname=dhcpv6+user-identify-policy) { **option79-option38** | **option38-option79** | **option79** | **option38** } [ **no-exist-action offline** ]
    
    
    
    A method is configured for obtaining MAC addresses of Layer 3 DHCPv6 users during login.
26. (Optional) Enable suppression of leased line user access.
    
    
    1. Run the [**quit**](cmdqueryname=quit) command to return to the interface view.
    2. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
    3. Run the [**access leased-line connection chasten**](cmdqueryname=access+leased-line+connection+chasten) *request-session* *request-period* *blocking-period* **quickoffline** command to enable suppression of leased line user access.
       
       If the duration or traffic volume quota delivered by the RADIUS server to a leased line user is 0, the leased line user can go online but will be logged out immediately. This results in frequent logins and logouts of the leased line user.
       
       To resolve the problem, run this command to configure the maximum number of connection requests for a leased line user and a blocking period.
27. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.