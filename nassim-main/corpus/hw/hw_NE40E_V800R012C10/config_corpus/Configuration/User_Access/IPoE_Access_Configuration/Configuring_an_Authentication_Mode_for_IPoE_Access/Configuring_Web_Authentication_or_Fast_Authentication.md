Configuring Web Authentication or Fast Authentication
=====================================================

Web authentication requires a user who wants to access the network to enter the username and password on the authentication page of a web authentication server for authentication. Fast authentication is an authentication mode in which a user accesses the authentication page of a web authentication server for authentication, without entering the username and password.

#### Context

When configuring web authentication or fast authentication, you need the following parameters:

* IP address and VPN instance of the server
* Port number of the server
* Shared key of the server
* Whether the NE40E reports its own IP address to the server
* Portal protocol version, listening port number, and source interface sending portal packets
* Pages to which users are redirected

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* For security purposes, use an eight-character or longer password that contains at least two types of the following: uppercase letters, lowercase letters, digits, and special characters.
* You are advised to configure your password in ciphertext mode and change it periodically.


#### Procedure

1. Configure a web authentication server.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**web-auth-server**](cmdqueryname=web-auth-server) { *i*p-address** | **ipv6-address** } [ **vpn-instance** *instance-name* ] [ **port** *port-number* ] [ **key** { **simple** *simple-key* | **cipher** *cipher-key* } ] [ **nas-ip-address** ][ **detect-time** *detect-time* ] [ **user-query** { **exclude** **pre-domain** | **version1** } ]
      
      
      
      A web authentication server is configured.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      For security purposes, you are advised to use CHAP authentication on the web server and encrypt user names and passwords during authentication.
   3. Run [**quit**](cmdqueryname=quit)
      
      
      
      The system view is displayed.
2. Specify an IP address to be used by the keyword to receive portal packets from the web authentication server.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run **[**web-auth-server**](cmdqueryname=web-auth-server)** { ****source-ip**** **source-ip** | ****source-ipv6**** **source-ipv6** } [ ****vpn-instance**** **vpn-instance** ]
      
      
      
      An IP address is specified. It is used by the NE40E to receive portal packets from the web authentication server.
      
      
      
      By default, the NE40E is disabled from using any IP addresses to receive portal packets from the web authentication server, and therefore the NE40E cannot receive portal packets from the server. To allow the device to use all IP addresses to receive portal packets from the web authentication server, run the **[**web-auth-server**](cmdqueryname=web-auth-server)** { ****source-ip**** | ****source-ipv6**** } ****all**** command.
   3. Run [**quit**](cmdqueryname=quit)
      
      
      
      The system view is displayed.
3. (Optional) Configure the portal protocol.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**web-auth-server version**](cmdqueryname=web-auth-server+version) { **v2** [ **v1** ] | **v3** }
      
      
      
      The version of the portal protocol is set.
   3. (Optional) Run [**web-auth-server listening-port**](cmdqueryname=web-auth-server+listening-port) *port*
      
      
      
      The number of the port for receiving portal packets from the web authentication server is specified on the NE40E.
   4. Run [**web-auth-server source from packet-destination-ip**](cmdqueryname=web-auth-server+source+from+packet-destination-ip)
      
      
      
      The source IP address in the packets sent to the web authentication server as the destination IP address of the received packets is configured.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      [**web-auth-server source from packet-destination-ip**](cmdqueryname=web-auth-server+source+from+packet-destination-ip) command and [**web-auth-server source**](cmdqueryname=web-auth-server+source) **interface** { *interface-type* *interface-number* | *interface-name* } command are mutually exclusive.
   5. (Optional) Run [**web-auth-server source**](cmdqueryname=web-auth-server+source) **interface** *interface-type* *interface-number*
      
      
      
      The source interface for sending packets to the web authentication server is configured on the NE40E.
   6. (Optional) Run [**web-auth-server packet**](cmdqueryname=web-auth-server+packet) **dscp** *dscp-value*
      
      
      
      The DSCP value for Portal packets sent by the device to a Portal server is configured.
   7. (Optional) Run [**web-auth-server reply-message**](cmdqueryname=web-auth-server+reply-message)
      
      
      
      The NE40E is configured to transparently transmit response packets from the RADIUS server to the web authentication server.
   8. (Optional) Run [**web response-error-id enable**](cmdqueryname=web+response-error-id+enable)
      
      
      
      The NE40E is enabled to send an Access-Reject packet carrying an error code to the portal server.
   9. (Optional) Run [**whitelist session-car web-auth-server disable**](cmdqueryname=whitelist+session-car+web-auth-server+disable)
      
      
      
      The whitelist session CAR function is disabled.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      Disabling this function is not usually recommended.
   10. (Optional) Run [**whitelist session-car web-auth-server**](cmdqueryname=whitelist+session-car+web-auth-server) { **cir** *cir-value* | **cbs** *cbs-value* | **pir** *pir-value* | **pbs** *pbs-value* } \*
       
       
       
       The bandwidth parameters of whitelist session CAR are configured.
4. (Optional) Configure the Portal Server.
   1. Run [**aaa**](cmdqueryname=aaa)
      
      
      
      The AAA view is displayed.
   2. Run [**domain**](cmdqueryname=domain) *domain-name*
      
      
      
      The view of the domain is displayed.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   4. Configure the Portal Server.
      
      
      * Run **portal-server** { *ip-address* | *ipv6-address* | **redirect-limit** *limit-value* | **url** *url-string* | **url-parameter** } command to set the mandatory portal service parameters for the domain, including the port server's IP address, number of mandatory redirects, URL for mandatory redirect, and URL parameters carried in the redirect URL.
      * (Optional) Run **[**portal-server redirect-key user-mac-address**](cmdqueryname=portal-server+redirect-key+user-mac-address)** *user-mac-address*[ **simple** [ **type1** ] | **cipher** { **aes128** { **cbc** | **gcm** } | **des** } ] command to configure the user MAC address carried in the redirect packets of mandatory portal service.
        
        (Optional) Run **portal-server url-parameter shared-key-cipher** [ *shared-key-cipher* ] command to configure the key required for carrying the encrypted MAC address in the redirect packet.
        
        ![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        If the [**portal-server redirect-key user-mac-address**](cmdqueryname=portal-server+redirect-key+user-mac-address) *user-mac-address* [ **cipher** **aes128** { **cbc** | **gcm** } | **des** ] command, but not the [**portal-server url-parameter shared-key-cipher**](cmdqueryname=portal-server+url-parameter+shared-key-cipher) [ *shared-key-cipher* ], the MAC address is not carried in the redirect packet of the portal service.
      * (Optional) Run the **portal-server user-first-url-key** { *user-number* | **default-name** } command to enable the function of redirecting to the homepage URL for the portal server.
      * (Optional) Run the **portal-server identical-url** command to enable the function of using the unified URL for the portal server.
      * (Optional) Run the **portal-redirect** command to configure the captive portal timeout period.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      The AAA view is displayed.
5. (Optional) Configure mandatory web authentication.
   
   
   
   Mandatory web authentication enables the NE40E to redirect the access request of a user to a specified web server when the user accesses an unauthorized address before being authenticated, facilitating user authentication.
   
   
   
   1. Run [**aaa**](cmdqueryname=aaa)
      
      
      
      The AAA view is displayed.
   2. (Optional) Run [**access-user logout stop-accounting before authentication**](cmdqueryname=access-user+logout+stop-accounting+before+authentication)
      
      
      
      The NE40E is enabled to send an Accounting Stop packet and then authenticate a user in the user's switchover process from the authentication domain to the pre-authentication domain.
   3. Run [**domain**](cmdqueryname=domain) *domain-name*
      
      
      
      The view of the default pre-authentication domain is displayed.
   4. (Optional) Run any of the following commands:
      
      
      * To configure a redirection URL for mandatory web authentication, run the [**web-server**](cmdqueryname=web-server) **url** *url-string* command.
      * To configure specified keywords carried in the URL of a web page pushed by the portal server, run the [**web-server**](cmdqueryname=web-server) **url-parameter** command.
      * To configure an IPv4 address or both IPv4 and IPv6 addresses for the web server, run the [**web-server**](cmdqueryname=web-server) *ip-address* [ *ipv6âaddress* ] [ **slave** ] command.
        
        *ipv6âaddress* must be specified for dual-stack web users.
      * To configure the HTTP mode of the web server, run the [**web-server**](cmdqueryname=web-server) **mode** { **get** | **post** } command.
      * To configure the keyword of a customized portal attribute, run the [**web-serve**](cmdqueryname=web-serve)[**r**](cmdqueryname=r) **redirect-key** { **mscg-ip** *mscg-ip-key* | **mscg-name** *mscg-name-key* | **user-ip-address** *user-ip-key* | **user-location**  *user-location-key* | **nas-logic-sysname** *nas-logic-sysname-key*  | **user-mac-address** { *user-mac-key* [ **simple** [ **type1** ] | **cipher** { **aes128** [ **cbc** | **gcm** ] | **des** }  ] }, [**web-server**](cmdqueryname=web-server) **redirect-key** **mscg-ipv6** *mscg-ipv6-key*,[**web-server redirect-key**](cmdqueryname=web-server+redirect-key) **ap-mac-address** *ap-mac-key* [ **simple** [ **type1** ] | **cipher** { **aes128** [ **cbc** | **gcm** ] | **des** } ], [**web-server**](cmdqueryname=web-server) **redirect-key** **ssid** *ssid-key*, or [**web-server**](cmdqueryname=web-server) **redirect-key** **agent-remote-id** *agent-remote-id-key* command.
      * (Optional) To configure the keyword for generating ciphertext user MAC address or AP MAC address to be displayed, run the [**web-server**](cmdqueryname=web-server) **url-parameter** { **shared-key** [ *shared-key* ] | **shared-key-cipher** [ *shared-key-cipher* ] } command.
        
        This step is mandatory only if the [**web-server**](cmdqueryname=web-server) **redirect-key** command with **cipher** **aes128** configured has been run.
      * To configure the keyword of a user IP address, run the [**web-server**](cmdqueryname=web-server) **user-first-url-key** { *key-name* | **default-name** } command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      A redirection URL must be configured in the pre-authentication domain for a dual-stack web user. Otherwise, mandatory web authentication may fail.
   5. (Optional) Run [**web-server**](cmdqueryname=web-server) { { *ip-address* | *ipv6-address* } \* | **url** *url* } [ **bind web-auth-server** {  *auth-server-ip* | *auth-server-ipv6* }[ **vpn-instance** *vpn-instance* ] ]
      
      
      
      The web authentication server bound to the mandatory web server is configured.
   6. (Optional) Run [**web-server**](cmdqueryname=web-server) { { *ip-address* | *ipv6-address* } \* | **url** *url* } [ **bind web-auth-server** {  *auth-server-ip* | *auth-server-ipv6* }[ **vpn-instance** *vpn-instance* ] ] **slave**
      
      
      
      The web authentication server bound to the backup mandatory web server is configured.
   7. (Optional) Run [**mac-authentication enable**](cmdqueryname=mac-authentication+enable)
      
      
      
      MAC address authentication is enabled.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      MAC address authentication is used to simplify web authentication. If MAC address authentication is enabled, a web authentication user needs to enter the username and password only at the first authentication during which the RADIUS server records the user's MAC address. When web authentication needs to be performed for the user again, the RADIUS server authenticates the user based on the user's MAC address without the user entering the username and password again.
      
      This command is usually used together with the [**authening authen-fail**](cmdqueryname=authening+authen-fail) **online** **authen-domain** *domain-name* command on the live network. After these two commands are run, if a user fails MAC authentication, the user will enter a redirection domain in which the user can enter the username and password for web authentication. After web authentication succeeds, the user enters the authentication domain and can access network resources.
   8. Run [**quit**](cmdqueryname=quit)
      
      
      
      The AAA view is displayed.
   9. Run [**quit**](cmdqueryname=quit)
      
      
      
      The system view is displayed.
6. (Optional) Configure the function to allow web users to directly log in to the post-authentication domain.
   1. Run the [**access post-domain auto-login-type**](cmdqueryname=access+post-domain+auto-login-type) { **web** **auth-server** { *ipaddr* | *ipv6addr*} [ **vpn-instance** *vpnname* ] | **coa** } command to configure this function.
      
      
      
      In scenarios where web authentication is performed in the post-authentication domain, if users do not go offline proactively or users' quotation is exhausted, the username and password do not need to be entered when users go online again. They can directly log in to the post-authentication for network access.
   2. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   3. Run the [**quit**](cmdqueryname=quit) command to return to the AAA view.
   4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
7. (Optional) Configure web performance optimization.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**http-url deny**](cmdqueryname=http-url+deny) *urlstring*
      
      
      
      A URL blacklist for mandatory web authentication or captive portal is configured.
   3. Run [**slot**](cmdqueryname=slot) *slot-id*
      
      
      
      The slot view is displayed.
   4. Run [**http-hostcar**](cmdqueryname=http-hostcar) **cir** *cir-value* [ **pir** *pir-value* ] [ **cbs** *cbs-value* **pbs** *pbs-value* ]
      
      
      
      A bandwidth limit is configured for HTTP packets sent by users for authentication.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      The system view is displayed.
   6. Run [**aaa**](cmdqueryname=aaa)
      
      
      
      The AAA view is displayed.
   7. Run [**domain**](cmdqueryname=domain) *domain-name*
      
      
      
      The domain view is displayed.
   8. Run [**quit**](cmdqueryname=quit)
      
      
      
      The AAA view is displayed.
8. (Optional) Run [**access-user login session-limit reply**](cmdqueryname=access-user+login+session-limit+reply) *error-code* *message*.
   
   
   
   The error code and message returned by the device to the portal server if web users switch from the pre-authentication domain to the authentication domain and the number of users using the same account has reached the upper limit is configured.
9. (Optional) Configure the device not to assign IPv6 addresses to users from a pre-authentication domain.
   1. Run [**aaa**](cmdqueryname=aaa)
      
      
      
      The AAA view is displayed.
   2. Run [**domain**](cmdqueryname=domain) *domain-name*
      
      
      
      The domain (pre-authentication domain) view is displayed.
   3. Run [**ipv6-address authorization disable**](cmdqueryname=ipv6-address+authorization+disable)
      
      
      
      The device is configured not to assign IPv6 addresses from a pre-authentication domain.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      The AAA view is displayed.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      The system view is displayed.
   6. (Optional) Run [**dhcpv6 reply-status-code unspecfail disable**](cmdqueryname=dhcpv6+reply-status-code+unspecfail+disable)
      
      
      
      The device is configured not to reply with an Advertise packet when the DHCPv4 stack user is online and the DHCPv6 stack user is online but is not enabled to obtain an assigned IPv6 address.
10. Configure pre-authentication and authentication domains and an authentication method on a BAS interface.
    
    
    
    Web authentication users are considered unauthorized users before they are authenticated. Therefore, they cannot obtain IP addresses or access the web authentication server.
    
    This means web authentication cannot be performed on web authentication users. To resolve this problem, all unauthenticated web authentication users are assigned to a default domain configured on an interface. This default domain is called the default pre-authentication domain. Unauthenticated web authentication users can obtain IP addresses from the default pre-authentication domain and access the web authentication server through the authorities granted to the default pre-authentication domain for web authentication.
    
    
    
    1. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
       
       
       
       The interface view is displayed.
    2. Run [**bas**](cmdqueryname=bas)
       
       
       
       The BAS interface view is displayed.
    3. Run [**access-type**](cmdqueryname=access-type) **layer2-subscriber**
       
       
       
       The use access type is set to Layer 2 subscriber access.
    4. Run [**default-domain**](cmdqueryname=default-domain) **pre-authentication** *domain-name*
       
       
       
       The default pre-authentication domain is specified.
    5. Run [**default-domain**](cmdqueryname=default-domain) **authentication** [ **force** | **replace** ] *domain-name*
       
       
       
       The default authentication domain is specified.
    6. Run [**authentication-method**](cmdqueryname=authentication-method) { **web** | **fast** } or [**authentication-method-ipv6**](cmdqueryname=authentication-method-ipv6) { **web** | **fast** }
       
       
       
       Web authentication or fast authentication is configured.
11. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.