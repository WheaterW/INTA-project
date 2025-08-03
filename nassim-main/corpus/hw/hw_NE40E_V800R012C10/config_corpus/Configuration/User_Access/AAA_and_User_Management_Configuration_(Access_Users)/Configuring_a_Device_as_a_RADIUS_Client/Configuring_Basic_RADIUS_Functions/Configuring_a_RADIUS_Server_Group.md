Configuring a RADIUS Server Group
=================================

Configuring a RADIUS Server Group

#### Context

If remote authentication, authorization, and accounting are performed for users through a RADIUS server, you need to configure a RADIUS server group.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**radius-server group**](cmdqueryname=radius-server+group) *group-name*
   
   
   
   The RADIUS server group view is displayed.
3. Run [**radius-server**](cmdqueryname=radius-server+shared-key) { **shared-key** *key-string* | **shared-key-cipher** *key-string-cipher* } [ { **authentication** | **accounting** } { *ip-address* | *ipv6-address* [ **vpn-instance** *instance-name* ] } [ **source** { { interface-name | interface-type interface-number } | **ip-address** *ip-address* } ] *port* [ **weight** *weight* ] ]
   
   
   
   The shared key for the communication with the RADIUS server is configured.
4. Configure the RADIUS authentication server as required.
   
   
   
   **Table 1** Configuring a RADIUS authentication server
   | Operation | Command | Description |
   | --- | --- | --- |
   | Specify an IPv4 RADIUS authentication server. | * [**radius-server**](cmdqueryname=radius-server) **authentication** *ip-address* *port* { **vpn-instance** *instance-name* | { **shared-key** *key-string* | **shared-key-cipher** *cipher-string* } | **source** { *interface-name* | *interface-type* *interface-num* | **ip-address** *ip-address* } } \* [ **weight** *weight-value* ] * [**radius-server**](cmdqueryname=radius-server) **authentication** *ip-address* [ **vpn-instance** *instance-name* | **source** { { *interface-name* | *interface-type* *interface-num* } | **ip-address** *source-ip-address* } | { **shared-key** *key-string* | **shared-key-cipher** *cipher-string* } ] \* *port* [ **weight** *weight-value* ] * [**radius-server**](cmdqueryname=radius-server) **authentication** *ip-address* [ **vpn-instance** *instance-name* ] **ppp-user-port** *port* | * Weights of authentication servers apply only to load balancing scenarios, and the default value is 0. * **ppp-user-port** specifies that PPP users use different ports. |
   | Specify an IPv6 RADIUS authentication server. | [**radius-server**](cmdqueryname=radius-server) **authentication** *ipv6-address* [ **vpn-instance** *instance-name* | **source** { *interface-name* | *interface-type* *interface-num* } | { **shared-key** *key-string* | **shared-key-cipher** *cipher-string* } ] \* *port* [ **weight** *weight-value* ] |
5. Configure the RADIUS accounting server as required.
   
   
   
   **Table 2** Configuring a RADIUS accounting server
   | Operation | Command | Description |
   | --- | --- | --- |
   | Specify an IPv4 RADIUS accounting server. | * [**radius-server**](cmdqueryname=radius-server) **accounting** *ip-address* *port* { **vpn-instance** *instance-name* | { **shared-key** *key-string* | **shared-key-cipher** *cipher-string* } | **source** { *interface-name* | *interface-type* *interface-num* | **ip-address** *ip-address* } } \* [ **weight** *weight-value* ] * [**radius-server**](cmdqueryname=radius-server) **accounting** *ip-address* [ **vpn-instance** *instance-name* | **source** { { *interface-name* | *interface-type* *interface-num* } | **ip-address** *source-ip-address* } | { **shared-key** *key-string* | **shared-key-cipher** *cipher-string* } ] \* *port* [ **weight** *weight-value* ] | * Weights of accounting servers apply only to load balancing scenarios, and the default value is 0. * **ppp-user-port** specifies that PPP users use different ports. |
   | Specify an IPv6 RADIUS accounting server. | [**radius-server**](cmdqueryname=radius-server) **accounting** *ipv6-address* [ **vpn-instance** *instance-name* | **source** { *interface-name* | *interface-type* *interface-num* } | { **shared-key** *key-string* | **shared-key-cipher** *cipher-string* } ] \* *port* [ **weight** *weight-value* ] |
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   RADIUS authentication and accounting servers can use the same IP address, indicating that one server can perform both RADIUS authentication and accounting functions. If a server performs both RADIUS authentication and accounting functions, it uses a separate interface for each function.
6. (Optional) Run [**radius-server authentication rollover-on-reject**](cmdqueryname=radius-server+authentication+rollover-on-reject)
   
   
   
   The device is enabled to poll RADIUS servers for authentication after receiving a RADIUS Access-Reject packet.
7. (Optional) Run [**radius-server algorithm**](cmdqueryname=radius-server+algorithm) { **loading-share** | **master-backup** { **strict** | **sequence** } \* }
   
   
   
   The algorithm for selecting a RADIUS server is configured.
   
   
   
   After **strict** is configured, the accounting server is strictly selected based on the configured algorithm. The primary accounting server is preferentially selected, regardless of the selection result of the authentication server. If **strict** is not configured, the RADIUS accounting server is selected based on the selection result of the authentication server. Specifically, the RADIUS server that performs authentication for a user also performs accounting for the user.
8. (Optional) Run [**radius-server alarm disable**](cmdqueryname=radius-server+alarm+disable)
   
   
   
   The device is disabled from generating a RADIUS server down alarm if communication between it and the RADIUS server is interrupted.
9. (Optional) Run [**radius-server accounting-start-packet send after-ppp**](cmdqueryname=radius-server+accounting-start-packet+send+after-ppp)
   
   
   
   The device is configured to send Accounting Start packets to the RADIUS server immediately after NCP goes up for PPPoEv6 single-stack users who use DHCPv6 to obtain IPv6 addresses.
10. (Optional) Run [**radius-server accounting-stop-packet send force**](cmdqueryname=radius-server+accounting-stop-packet+send+force)
    
    
    
    The device is configured to forcibly send Accounting Stop packets.
    
    
    
    In normal cases, a RADIUS server generates user entries only after accounting succeeds. In some cases, however, it may generate user entries in the database after authentication succeeds but before accounting starts. For example, if accounting fails after a user requesting an IP address is successfully authenticated, the requested IP address cannot be released and the user fails to go online using this IP address. In such case, run this command to configure the device to forcibly send an Accounting Stop packet to the RADIUS server to release the requested IP address.
    
    This command applies only to scenarios where user authentication succeeds but accounting fails and residual user entries generated by the RADIUS server exist in the database.
11. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.