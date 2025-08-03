Configuring L2TP Attributes for Users
=====================================

The L2TP attributes of a user include the tunnel type, LAC source address, LNS address, tunnel name, tunnel password, and tunnel ID. The L2TP attributes delivered by the RADIUS server have a higher priority than those configured locally.

#### Context

After an L2TP group is configured, you can specify the L2TP group in a domain so that the domain is associated with the L2TP tunnel. In this way, the NE40E can wholesale services of an ISP to the access server (LNS) of the ISP through the associated L2TP tunnel. This allows the services of multiple ISPs to be wholesaled.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**domain**](cmdqueryname=domain) *domain-name*
   
   
   
   The domain view is displayed.
4. (Optional) Run [**l2tp-group**](cmdqueryname=l2tp-group) *group-name*
   
   
   
   An L2TP group is specified for the domain.
5. (Optional) Run [**l2tp-user radius-force**](cmdqueryname=l2tp-user+radius-force)
   
   
   
   The L2TP attributes delivered by the RADIUS server are specified for domain users.
   
   
   
   The L2TP attributes of domain users can be specified by the L2TP group in the domain or delivered by the RADIUS server. When the L2TP attributes delivered by the RADIUS server are specified for domain users, no L2TP group needs to be specified in the domain. (The L2TP group is invalid even if it is specified.)
   
   The RADIUS server can deliver attributes such as Tunnel-Type (64), Tunnel-Client-Endpoint (66), Tunnel-Server-Endpoint (67), Tunnel-Client-Auth-ID (90), Tunnel-Password (69), and Tunnel-Assignment-ID (82). If the RADIUS server does not deliver the L2TP group name, the NE40E considers the user as a common PPP user.
   
   The L2TP attributes delivered by the RADIUS server have a higher priority than those configured locally. For example, if the LNS address configured in the L2TP group **lac1** on the NE40E is 10.10.10.1, and the RADIUS server delivers the LNS address 10.20.20.1 and the L2TP group **lac1**, the valid LNS address is 10.20.20.1. If the RADIUS server delivers only the L2TP group **lac1**, the valid LNS address is 10.10.10.1.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   For the RADIUS-delivered L2TP attributes and L2TP functions to take effect, the L2TP group name and tunnel type attributes must be delivered at the same time.
   
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   The L2TP attributes delivered by the RADIUS server have a higher priority than the local L2TP attributes. If the L2TP attributes are not delivered by the RADIUS server, do not run this command. Otherwise, L2TP dial-up fails.
6. (Optional) Run [**l2tp-authorize**](cmdqueryname=l2tp-authorize) **password** { **simple** *simple-password* | **cipher** *cipher-password* }
   
   
   
   The LAC is configured to authenticate an L2TP user using the domain name of the user. This means that the LAC sends the domain name and password of the user to the RADIUS server for authentication.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * The password must be at least eight characters long and contains at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters.
   * For security purposes, you are advised to specify the ciphertext mode. To ensure device security, change the password periodically.
   If the [**l2tp-authorize**](cmdqueryname=l2tp-authorize) command is run in a domain, the authentication rules are as follows:
   * When a new PPP user is authenticated, if the [**l2tp-authorize**](cmdqueryname=l2tp-authorize) command is run in the domain of the user and RADIUS authentication is used, virtual user authentication is set in the user information table. Otherwise, the original process is followed.
   * When sending an authentication request to the RADIUS server for a virtual user, the device sends the domain name of the user as the username and the configured password (**huawei** by default) to the RADIUS server.
   * If the RADIUS server denies the authentication or the authentication request fails to be sent, the device uses the original PPP username for secondary authentication.
   * If RADIUS authentication is successful but the Tunnel-Type and Tunnel-Server-Endpoint attributes delivered by the RADIUS server are incorrect, the device also uses the original PPP username for secondary authentication.
   * If RADIUS authentication is successful and the Tunnel-Type and Tunnel-Server-Endpoint attributes delivered by the RADIUS server are correct, accounting is performed for the user, and the original PPP username is used as the username for accounting.
   
   If the [**l2tp-authorize**](cmdqueryname=l2tp-authorize) command is not run, the LAC sends the username and password entered by a user to the RADIUS server for authentication.
7. Run **idle-cut** *idle-time* { *idle-data* | **zero-rate** } [ **inbound** | **outbound** ]
   
   
   
   The idle-cut function is configured for the domain. After the command is run, a user is logged out when the user's traffic volume in a specified period is lower than a configured threshold. This command prevents a user from occupying bandwidth resources when no traffic is transmitted for the user for a long time.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.