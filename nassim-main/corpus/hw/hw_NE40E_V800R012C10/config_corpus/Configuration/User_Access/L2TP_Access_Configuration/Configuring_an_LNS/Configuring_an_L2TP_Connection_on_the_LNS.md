Configuring an L2TP Connection on the LNS
=========================================

To allow a tunnel to be set up through negotiation after an LNS receives a tunnel setup request from a LAC, you need to configure a virtual template (VT) and user authentication domain in the L2TP group view on the LNS.

#### Context

The LNS can receive tunnel setup requests from different LACs by using different VTs. After receiving a tunnel setup request from a LAC, the LNS checks the LAC name. The LNS allows the remote end to set up the tunnel if the LAC name is consistent with the name of the remote end.

In this configuration, the L2TP group type is set to LNS (ACCEPT\_DIALIN\_L2TP).

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* When the NE40E functions as an LNS to interwork with a Huawei LAC, it is recommended that the MTU in the bound VT be set to a value less than or equal to 1462 bytes (assume that the interface MTU is 1500 bytes).
* When the NE40E functions as an LNS to interwork with a non-Huawei LAC that does not support L2TP packet fragmentation, you are advised to set the MTU in the VT to a value less than or equal to 1454 bytes (assume that the interface MTU of the non-Huawei device is 1500 bytes). This prevents L2TP packets longer than 1500 bytes from being fragmented into invalid packets on the LAC.
* If the MTU is set manually in the VT, ensure that the MTUs negotiated by the L2TP user, LAC, and LNS are the same.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**l2tp-group**](cmdqueryname=l2tp-group) *group-name*
   
   
   
   The L2TP group view is displayed.
3. Run [**allow l2tp virtual-template**](cmdqueryname=allow+l2tp+virtual-template) *virtual-template-number* **remote** *lac-name* [ **ip address** *address* ] or [**allow l2tp virtual-template**](cmdqueryname=allow+l2tp+virtual-template) *virtual-template-number* **by-source-ip**
   
   
   
   An L2TP connection is configured on the LNS.
   
   
   
   Except the default L2TP group **default-lns**, you must specify *lac-name* or *by-source-ip* for other L2TP groups when configuring an L2TP connection on the LNS.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   For the same L2TP group, the [**start l2tp**](cmdqueryname=start+l2tp) and [**allow l2tp virtual-template**](cmdqueryname=allow+l2tp+virtual-template) commands are mutually exclusive. The configuration of one command will invalidate the other.
4. Run [**tunnel lac-source-ip**](cmdqueryname=tunnel+lac-source-ip) *start-ip-address* *end-ip-address* [**password**](cmdqueryname=password) **cipher** *password*
   
   
   
   The LAC-side source IP address segment and password are specified for LNS authentication.
5. (Optional) Run [**default-domain authentication**](cmdqueryname=default-domain+authentication) { *domain-name* | **force** *domain-name* | **replace** *domain-name* }
   
   
   
   An authentication domain is configured for L2TP users.
   
   
   
   The [**default-domain authentication**](cmdqueryname=default-domain+authentication) command specifies the default authentication domain for L2TP users. When a user goes online from the LAC using a username without a domain name, the LNS logs the user in through the default domain. The authentication scheme, accounting scheme, address pool, and other user login information are configured in the default domain. If the default authentication domain is not specified, when a user goes online from the LAC using a username without a domain name, the LNS logs the user in through the domain **default1** by default.
   
   The [**default-domain authentication**](cmdqueryname=default-domain+authentication) **force** command specifies a forcible authentication domain for L2TP users. When a user goes online from the LAC, the LNS logs the user in through the forcible authentication domain without changing the user domain name. The user domain adopts the configurations of the forcible authentication domain.
   
   The [**default-domain authentication**](cmdqueryname=default-domain+authentication) **replace** command specifies a substitute authentication domain for L2TP users. When a user goes online from the LAC, the LNS replaces the user domain with the substitute authentication domain, replaces the user domain name with the substitute authentication domain name, and adopts the configurations of the substitute authentication domain for the user domain.
6. (Optional) Run [**roam-domain**](cmdqueryname=roam-domain) *domain-name*
   
   
   
   A roaming domain is configured on the LNS.
7. (Optional) Run [**tunnel window receive**](cmdqueryname=tunnel+window+receive) *window-size*
   
   
   
   The size of the L2TP receive window is set for out-of-order packets.
8. (Optional) Run [**lns calling-station-id format agent-remote-id**](cmdqueryname=lns+calling-station-id+format+agent-remote-id)
   
   
   
   The LNS is configured to parse the Agent-Remote-Id attribute in IRCQ packets sent by the LAC and encapsulate this attribute into the Calling-Station-Id attribute to be sent to the RADIUS server.
9. Run [**quit**](cmdqueryname=quit)
   
   
   
   The system view is displayed.
10. (Optional) Run [**qos link-adjustment vendor redback**](cmdqueryname=qos+link-adjustment+vendor+redback) { **lns** | **lac** } \* [ **slot** *slot-id* ]
    
    
    
    User traffic compensation is configured so that the compensated user traffic statistics are collected in redback mode.
    
    
    
    In VS mode, this command is supported only by the admin VS.
    
    The compensation in redback mode is implemented as follows:
    
    | Layer 2 | LAC (UP) (Unit: Byte) | LAC (DOWN) (Unit: Byte) | LNS (UP) | LNS (DOWN) |
    | --- | --- | --- | --- | --- |
    | Compensation value (default statistics) | * Double-tagged: 12 * Single-tagged: 16 * Without a VLAN: 20 | 4 | 6 | 4 |
    | Compensation value (CAR) | * Double-tagged: 12 * Single-tagged: -16 * Without a VLAN: -20 | -4 | 6 | -4 |
    | Compensation value (SQ) | * Double-tagged: -8 * Single-tagged: -12 * Without a VLAN: -16 | * Double-tagged: 24 * Single-tagged: 20 * Without a VLAN: 16 | 10 | 38 |
11. Run [**l2tp-group**](cmdqueryname=l2tp-group) *group-name*
    
    
    
    The L2TP group view is displayed.
12. (Optional) Run [**avp nas-port enable**](cmdqueryname=avp+nas-port+enable)
    
    
    
    The LNS is configured to parse NAS-PORT information carried in AVP 100 of ICRQ packets.
13. (Optional) Configure the LNS to encapsulate user IDs into RADIUS accounting packets.
    1. Run [**quit**](cmdqueryname=quit)
       
       
       
       The system view is displayed.
    2. Run [**radius-server group**](cmdqueryname=radius-server+group) *group-name*
       
       
       
       The RADIUS server group view is displayed.
    3. Run [**radius-attribute include nas-port lns with-user-id accounting-request**](cmdqueryname=radius-attribute+include+nas-port+lns+with-user-id+accounting-request)
       
       
       
       The LNS is configured to encapsulate the NAS-Port attribute sent from the LAC into accounting packets to be sent to the RADIUS server.
    4. Run [**quit**](cmdqueryname=quit)
       
       
       
       The system view is displayed.
    5. Run [**l2tp-group**](cmdqueryname=l2tp-group) *group-name*
       
       
       
       The L2TP group view is displayed.
14. (Optional) Run [**lns avp calling-number translate agent-remote-id**](cmdqueryname=lns+avp+calling-number+translate+agent-remote-id)
    
    
    
    The LNS is configured to copy the value of the Calling-Number attribute carried in an ICRQ message from an LAC to the Agent-Remote-Id field.
15. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.