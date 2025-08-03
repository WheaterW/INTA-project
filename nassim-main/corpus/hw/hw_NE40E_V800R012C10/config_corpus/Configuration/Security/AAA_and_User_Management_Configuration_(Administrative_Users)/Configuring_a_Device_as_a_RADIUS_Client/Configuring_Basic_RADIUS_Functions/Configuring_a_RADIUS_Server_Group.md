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
3. Run [**radius-server**](cmdqueryname=radius-server+shared-key) { **shared-key** *key-string* | **shared-key-cipher** *key-cipher-string* } [ { **accounting** | **authentication** } { *ip-address* | *ipv6-address* [ **vpn-instance** *instance-name* ] } [ **source** { { interface-name | interface-type interface-number } | **ip-address** *ip-address* } ] *port* [ **weight** *weight* ]
   
   
   
   A shared key is configured for the communication with the RADIUS server.
4. Configure the RADIUS authentication server as required.
   
   
   
   **Table 1** Configuring a RADIUS authentication server
   | Operation | Command | Description |
   | --- | --- | --- |
   | Specify an IPv4 RADIUS authentication server. | * [**radius-server**](cmdqueryname=radius-server) **authentication** *ip-address* *port* { **vpn-instance** *instance-name* | { **shared-key** *key-string* | **shared-key-cipher** *cipher-string* | **dtls-policy** *dtls-policy-name* } | **source** { *interface-name* | *interface-type* *interface-num* | **ip-address** *ip-address* } } \* [ **weight** *weight-value* ] * [**radius-server**](cmdqueryname=radius-server) **authentication** *ip-address* [ **vpn-instance** *instance-name* | **source** { { *interface-name* | *interface-type* *interface-num* } | **ip-address** *source-ip-address* } | { **shared-key** *key-string* | **shared-key-cipher** *cipher-string* | **dtls-policy** *dtls-policy-name* } ] \* *port* [ **weight** *weight-value* ] * [**radius-server**](cmdqueryname=radius-server) **authentication** *ip-address* [ **vpn-instance** *instance-name* ] **ppp-user-port** *port* | * Weights of RADIUS authentication servers apply only to load balancing scenarios, and the default value is 0. * The specified DTLS policy takes effect only for administrators. For details about how to configure a DTLS policy, see Basic Configuration > Accessing Other Devices Configuration > Configuring and Binding an SSL Policy. * To improve the security of administrators, you are advised to specify a DTLS policy for the RADIUS server. |
   | Specify an IPv6 RADIUS authentication server. | [**radius-server**](cmdqueryname=radius-server) **authentication** *ipv6-address* [ **vpn-instance** *instance-name* | **source** { *interface-name* | *interface-type* *interface-num* } | { **shared-key** *key-string* | **shared-key-cipher** *cipher-string* | **dtls-policy** *dtls-policy-name* } ] \* *port* [ **weight** *weight-value* ] |
5. Configure the RADIUS accounting server as required.
   
   
   
   **Table 2** Configuring a RADIUS accounting server
   | Operation | Command | Description |
   | --- | --- | --- |
   | Specify an IPv4 RADIUS accounting server. | * [**radius-server**](cmdqueryname=radius-server) **accounting** *ip-address* *port* { **vpn-instance** *instance-name* | { **shared-key** *key-string* | **shared-key-cipher** *cipher-string* | **dtls-policy** *dtls-policy-name* } | **source** { *interface-name* | *interface-type* *interface-num* | **ip-address** *ip-address* } } \* [ **weight** *weight-value* ] * [**radius-server**](cmdqueryname=radius-server) **accounting** *ip-address* [ **vpn-instance** *instance-name* | **source** { { *interface-name* | *interface-type* *interface-num* } | **ip-address** *source-ip-address* } | { **shared-key** *key-string* | **shared-key-cipher** *cipher-string* | **dtls-policy** *dtls-policy-name* } ] \* *port* [ **weight** *weight-value* ] | * Weights of RADIUS accounting servers apply only to load balancing scenarios, and the default value is 0. * The specified DTLS policy takes effect only for administrators. For details about how to configure a DTLS policy, see Basic Configuration > Accessing Other Devices Configuration > Configuring and Binding an SSL Policy. * To improve the security of administrators, you are advised to specify a DTLS policy for the RADIUS server. |
   | Specify an IPv6 RADIUS accounting server. | [**radius-server**](cmdqueryname=radius-server) **accounting** *ipv6-address* [ **vpn-instance** *instance-name* | **source** { *interface-name* | *interface-type* *interface-num* } | { **shared-key** *key-string* | **shared-key-cipher** *cipher-string* | **dtls-policy** *dtls-policy-name* } ] \* *port* [ **weight** *weight-value* ] |
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   RADIUS authentication and accounting servers can use the same IP address, indicating that one server can perform both RADIUS authentication and accounting functions. If a server performs both RADIUS authentication and accounting functions, it uses a separate interface for each function.
6. (Optional) Run [**radius-server algorithm**](cmdqueryname=radius-server+algorithm) { **loading-share** | **master-backup** { **strict** | **sequence** } \* }
   
   
   
   The algorithm for selecting RADIUS servers is configured.
   
   
   
   After **strict** is configured, the accounting server is strictly selected based on the configured algorithm. The primary accounting server is preferentially selected, regardless of the authentication server selection result. Otherwise, the RADIUS accounting server is selected based on the authentication server selection result. In other words, the RADIUS server that authenticates a user is the RADIUS server that performs accounting for the user.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.