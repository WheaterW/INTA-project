(Optional) Configuring Local Users
==================================

When the authentication and authorization are implemented in local mode, the authentication and authorization information (such as the username, password, level, maximum number of connections, and maximum number of continuous authentication failures).

#### Procedure

* In the AAA view, create a user.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**aaa**](cmdqueryname=aaa)
     
     
     
     The AAA view is displayed.
  3. Run [**local-user**](cmdqueryname=local-user) *user-name* **password** [ **cipher** *password* | **irreversible-cipher** *irreversible-cipher-password* ]
     
     
     
     A local user is created, and the password of the user is configured.
     
     
     
     + If the username contains the at sign (@), the characters before @ are the username, and the characters after @ are the domain name
     + If the username does not contain the at sign (@), the entire character string is the username, and the domain name is default\_admin.
     + The username cannot contain two or more at signs (@).
     + Input in simple text: When the user security policy is configured, the password cannot be the same as the username or its reverse. The password must contain the following characters: upper-case character, lower-case character, digit, and special character.![](../../../../public_sys-resources/note_3.0-en-us.png) 
       - The question mark (?) is not counted as a special character.
       - A space contained can only be located in the middle but not the beginning or end of the password. Use double quotation marks (") around the password.
       - If the [**local-user service-type**](cmdqueryname=local-user+service-type) command has been run to configure a user as an administrator by specifying the user type as the Telnet, FTP, SSH, SNMP, or terminal user, the system automatically changes the user password to an irreversible ciphertext key.
  4. (Optional) Run [**user-password password-force-change**](cmdqueryname=user-password+password-force-change) **disable**
     
     
     
     The function to forcibly change the initial password of the local user is disabled.
  5. (Optional) Run [**local-user**](cmdqueryname=local-user) *user-name* **password-force-change disable**
     
     
     
     Forcible modification of the initial password is disabled for a specified local user.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     To ensure device security, a local user must change the initial password upon the first login. You are not advised to disable forcible modification of the initial password for a local user.
  6. (Optional) Run [**local-user**](cmdqueryname=local-user) *user-name* **service-type** { { **terminal** | **telnet** | **ftp** | **ssh** | **qx** | **snmp** | **mml** | **http** } \* | **ppp** }
     
     
     
     The access type of the local user is configured.
     
     
     
     The **terminal**, **qx**, and **mml** parameters can be specified only for the admin VS.
  7. (Optional) Run [**local-user**](cmdqueryname=local-user) *user-name* **ftp-directory** *directory* [ **access-permission** { **read execute** | **read write execute** } ]
     
     
     
     The FTP directory right of the local user is configured.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + If the access type of the local user is set to FTP, the FTP directory of the local user must be configured and the level of local user cannot be lower than management level. Otherwise, FTP user login will fail.
     + If **access-permission** is not specified, the FTP directory permission of the local user is read-write by default.
  8. Configure the level of the local user or the group to which the local user belongs according to the command-line authorization mode.
     
     
     + Run the [**local-user**](cmdqueryname=local-user) *user-name* **level** *level* command to configure the level of the local user.![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       The configured level of the local user cannot be higher than that of the login-in user.
     + Run the [**local-user**](cmdqueryname=local-user) *user-name* **user-group** *user-group-name* command to add the local user to the specified user group.
  9. (Optional) Run [**local-user**](cmdqueryname=local-user) *user-name* **state** { **active** | **block** }
     
     
     
     The status of the local user is configured.
     
     
     
     The system processes the authentication requests of the users are as follows:
     
     + If a local user is in the active state, the system accepts the authentication request from the user and performs further processing.
     + If a local user is in the block state, the system rejects the authentication request from the user.
  10. (Optional) Run [**local-user**](cmdqueryname=local-user) *user-name* **access-limit** *max-number*
      
      
      
      The maximum number of concurrent connections that the local user can establish is set.
  11. (Optional) Run [**user-block failed-times**](cmdqueryname=user-block+failed-times) *failed-times-value* **period** *period-value*
      
      
      
      The maximum times of continuous authentication failures for the local user are configured.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      If a local user is in the locked state, you need to unlock it. Two ways are available for you to choose:
      
      + In the AAA view, run the [**user-block reactive**](cmdqueryname=user-block+reactive) *reactive-time* command to configure the interval at which a user will be automatically unlocked. If the locking time for a user exceeds the time set in the configuration, the user will be automatically unlocked.
      + In the user view, run the [**activate**](cmdqueryname=activate) **aaa** **local-user** *user-name* command to manually unlock the specified local user.
  12. Run **quit**
      
      
      
      Return to the system view.
  13. (Optional) Run [**aaa abnormal-offline-record**](cmdqueryname=aaa+abnormal-offline-record)
      
      
      
      The abnormal logout events are recorded.
      
      
      
      After this function is enabled, information about abnormal logout events can be provided for administrators to manage and maintain user information.
  14. Run **quit**
      
      
      
      Return to the user view.
  15. (Optional) Run [**local-user change-password**](cmdqueryname=local-user+change-password)
      
      
      
      The password of the local user is changed.
  16. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Configure a local user in the local AAA server view.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**local-aaa-server**](cmdqueryname=local-aaa-server)
     
     
     
     The local AAA server view is displayed.
  3. Run [**user**](cmdqueryname=user) *user-name* { **password** { **cipher** *cipher-password* | **irreversible-cipher** *irreversible-password* } | **authentication-type** *type-mask* | { **active** | **block** [ **fail-times** *fail-times-value* **interval** *interval-value* ] } | **ftp-directory** *ftp-directory* | **level** *level* | **callback-nocheck** | **callback-number** *callback-number* | **idle-cut** | **qos-profile** *qos-profile-name* | **ip-address** *ip-address* [ **vpn-instance** *vpn-instance* ] | **user-group** *user-group-name* } \*
     
     
     
     A local user account is added.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If the [**user**](cmdqueryname=user) *usr-name* **authentication-type** *authentication-type* command has been run to configure a user as an administrator by specifying the user type as the terminal user, Telnet, FTP, SNMP, or SSH, the system automatically changes the user password to an irreversible ciphertext key.
  4. (Optional) Run [**user**](cmdqueryname=user) *user-name* **expire** *expiretime*
     
     
     
     The expiration time of the local user is modified.
  5. (Optional) Run [**user**](cmdqueryname=user) *user-name* **block** [ **fail-times** *fail-times-value* **interval** *interval-value* ]
     
     
     
     The local user is blocked.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.