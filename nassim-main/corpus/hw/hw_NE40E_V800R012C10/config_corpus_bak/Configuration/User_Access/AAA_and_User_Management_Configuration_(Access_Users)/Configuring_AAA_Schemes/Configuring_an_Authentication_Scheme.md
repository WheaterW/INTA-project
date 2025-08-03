Configuring an Authentication Scheme
====================================

After configuring an authentication scheme, you need to configure relevant user information on the authentication server. Otherwise, users cannot pass the authentication.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**authentication-scheme**](cmdqueryname=authentication-scheme) *scheme-name*
   
   
   
   An authentication scheme is created, and its view is displayed.
   
   
   
   The NE40E supports three fixed authentication schemes: default, default0, and default1. They can be modified but cannot be deleted.
4. Run [**authentication-mode**](cmdqueryname=authentication-mode) { **radius** | **local** }\*[ **none** ], [**authentication-mode**](cmdqueryname=authentication-mode) **none** or [**authentication-mode**](cmdqueryname=authentication-mode) **radius-proxy**
   
   
   
   An authentication mode is configured.
   
   
   
   * If **radius** is configured in the command, RADIUS authentication is used. In this case, you need to configure a RADIUS authentication server. For details, see [Configuring a RADIUS Server Group](dc_ne_aaa_cfg_0602.html).
   * If **local** is configured in the command, local authentication is used. In this case, you need to run the [**local-user**](cmdqueryname=local-user) *user-name* **password** { **cipher** *cipher-password* | **irreversible-cipher** *irreversible-password* } command to create a local user.
   * If **radius-proxy** is configured in the command, RADIUS proxy authentication is used. In this case, you need to configure RADIUS proxy authentication. For details, see [(Optional) Configuring RADIUS Proxy Authentication](dc_ne_aaa_cfg_0605.html).
5. (Optional) Run [**authening authen-fail**](cmdqueryname=authening+authen-fail) { **offline** | **online** **authen-domain** *domain-name* }
   
   
   
   A policy is configured for handling authentication failures.
   
   
   
   The policy for handling authentication failures refers to the policy used by the NE40E after users fail authentication.
6. (Optional) [**authening quota-out-redirect-enable**](cmdqueryname=authening+quota-out-redirect-enable)
   
   
   
   The function of redirecting a user to a specified domain when the quota of the user is zero is enabled.
7. (Optional) Run [**authening authen-redirect online authen-domain**](cmdqueryname=authening+authen-redirect+online+authen-domain) *domain-name*
   
   
   
   A redirection domain is configured.
   
   
   
   This configuration allows users who pass and fail the authentication to go online from different domains.
   
   By configuring a private IP address pool, ACL-based access control, and security domain in the redirection domain, you can perform differentiated configuration and isolation of functions such as public/private address assignment and access control based on user domains. This saves public IP addresses and prevents unauthorized users from occupying many public IP addresses.
8. (Optional) Configure MAC address authentication.
   1. Run the [**domain**](cmdqueryname=domain) *domain-name* command to enter the domain view.
   2. (Optional) Run the [**mac-authentication enable**](cmdqueryname=mac-authentication+enable) command to enable MAC address authentication in the AAA domain view.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   MAC address authentication is mainly used to simplify web authentication. If MAC address authentication is enabled, a web authentication user needs to enter the username and password only for the first authentication, and the RADIUS server records the user's MAC address. For subsequent web authentication of the user, the RADIUS server authenticates the user based on the user's MAC address without requiring the user to enter the username and password again.
   
   On the live network, this command is often used together with the [**authening authen-fail**](cmdqueryname=authening+authen-fail) **online** **authen-domain** *domain-name* command. In other words, if a user fails MAC address authentication, the user enters the redirection domain in which web authentication is performed for the user based on the username and password. If the user passes web authentication, the user enters the authentication domain and can access network resources.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.