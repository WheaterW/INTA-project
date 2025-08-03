Configuring AAA Schemes for the Domain
======================================

Associate the remote authentication, authorization, and accounting schemes of the domain user with the server template by configuring a domain. Then, corresponding authentication, authorization, and accounting will be implemented for the users accessing the domain.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. (Optional) Run [**service-type terminal force-domain**](cmdqueryname=service-type+terminal+force-domain) *domain-name*
   
   
   
   A forced domain is configured for a console interface.
   
   
   
   When users logging
   in through the console interface and users logging in using other
   login methods must be distinguished, run the **service-type
   terminal force-domain** command to specify a forced domain
   for the console interface. After the configuration becomes effective,
   users logging in through the console interface automatically enter
   the forced domain and are not allocated any other domain based on
   the user names. In this manner, users logging in through the console
   interface and users logging using other methods are distinguished
   and allocated different rights.
   
   In VS mode, this command is supported only by the admin VS.
4. (Optional) Run [**default-domain**](cmdqueryname=default-domain) { **admin** | **access** } *domain-name*
   
   
   
   The domain name created in the preceding step is configured as the default domain name.
   
   
   
   After a user manually creates a domain name (for example, first\_domain) and the name is not the default domain name in the system, you must suffix @first\_domain to the username during authentication, which is inconvenient. To facilitate user authentication, run the [**default-domain**](cmdqueryname=default-domain) command to set the domain name **first\_domain** as the default domain name. With this configuration, **@first\_domain** is automatically suffixed to user names.
5. (Optional) Run [**domain-name-delimiter**](cmdqueryname=domain-name-delimiter) *delimiter*
   
   
   
   The domain name delimiter is configured.
6. (Optional) Run [**domain-location**](cmdqueryname=domain-location) { **after-delimiter** | **before-delimiter** }
   
   
   
   The domain name location is configured so that the system can correctly parse the username and domain name.
7. (Optional) Run [**domainname-parse-direction**](cmdqueryname=domainname-parse-direction) { **left-to-right** | **right-to-left** }
   
   
   
   The direction in which the domain name is parsed is configured so that the system can correctly parse the username and domain name.
   
   
   
   When a domain username contains multiple domain name delimiters, run the [**domainname-parse-direction**](cmdqueryname=domainname-parse-direction) command to configure the direction in which the domain name is parsed.Use **user1@abcd@domain1** as an example. When the domain name is parsed from left to right, the first delimiter @ from the left is considered the domain name delimiter. When the domain name is parsed from right to left, the first delimiter @ from the right is considered the domain name delimiter. The other delimiters are considered part of the user name or domain name.
8. Run [**domain**](cmdqueryname=domain) *domain-name*
   
   
   
   A domain is created and the AAA domain view is displayed.
9. Run [**authentication-scheme**](cmdqueryname=authentication-scheme) *scheme-name*
   
   
   
   The authentication scheme is configured for the domain.
10. Run [**authorization-scheme**](cmdqueryname=authorization-scheme) *authorization-scheme-name*
    
    
    
    The authorization scheme is configured for the domain.
11. Run [**accounting-scheme**](cmdqueryname=accounting-scheme) *accounting-scheme-name*
    
    
    
    The accounting scheme is configured for the domain.
12. Select the server template according to the configured authentication, authorization, and accounting modes.
    
    
    * Run the [**radius-server group**](cmdqueryname=radius-server+group) *group-name* command to configure a RADIUS server template for the domain.
      
      In VS mode, this command is supported only by the admin VS.
    * Run the [**hwtacacs-server**](cmdqueryname=hwtacacs-server) *template-name* command to configure the HWTACACS server template for the domain.
13. Run [**block**](cmdqueryname=block)
    
    
    
    The status of the domain is configured.
    
    
    
    When a domain is in block state, users of the domain cannot access the network.
14. (Optional) Run [**access-limit**](cmdqueryname=access-limit) *access-limit-number*
    
    
    
    The maximum number of access users for the domain is set.
15. (Optional) Run [**adminuser-priority**](cmdqueryname=adminuser-priority) *level*
    
    
    
    The default user level for administrators in a specific AAA domain is configured.
    
    
    
    If a user level is not assigned by the local device (using the [**local-user level**](cmdqueryname=local-user+level) command) or by a remote server, administrators are not allowed to access a specific domain in management mode. To resolve this issue, run the **adminuser-priority** command to configure a default level for administrators in a specific AAA domain. Then, the administrators will take this user level for login.
    
    A user level assigned by the local device or a remote server takes precedence over a user level configured using the **adminuser-priority** command. When the user is added to a user group, the configuration of user group takes precedence over a user level configured using the **adminuser-priority** command.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    The configured default level of the local user cannot be higher than that of the login-in user.
16. (Optional) Run [**service-type**](cmdqueryname=service-type){ **ftp** | **ppp** | **ssh** | **telnet** | **terminal** | **snmp** | **qx** | **mml** | **http** } \*
    
    
    
    The access type is set for users in the domain.
    
    
    
    The **terminal**, **qx**, and **mml** parameters can be specified only for the admin VS.
    
    The [**local-user service-type**](cmdqueryname=local-user+service-type) command configures the user access type for a specific user. When a user attempts to log in, the access type configured in the domain view and the access type configured using the [**local-user service-type**](cmdqueryname=local-user+service-type) command are checked in sequence. The user is allowed to log in only when both access types are authenticated.
17. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.