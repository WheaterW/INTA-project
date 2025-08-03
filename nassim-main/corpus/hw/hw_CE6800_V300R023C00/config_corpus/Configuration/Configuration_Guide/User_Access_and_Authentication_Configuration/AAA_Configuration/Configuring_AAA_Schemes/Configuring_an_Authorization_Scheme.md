Configuring an Authorization Scheme
===================================

Configuring an Authorization Scheme

#### Context

An authorization scheme defines the authorization methods used for user authorization and the order in which authorization methods take effect. Multiple authorization methods can be used in an authorization scheme to prevent authorization failures caused by a single authorization method failing to respond. RADIUS combines authentication and authorization, which cannot be separated. Authorization information is carried in the Access-Accept packet returned by the server. If RADIUS authentication is used, no authorization scheme needs to be configured.

![](public_sys-resources/note_3.0-en-us.png) 

* For device or network security purposes, you are advised not to set the authorization mode to non-authorization.
* When local authorization is used, authorization succeeds only when the user access mode matches the access type configured for the local user.
* Authorization provided by the authentication server takes precedence over authorization in the authentication domain. That is, when the attributes authorized by the authentication server and authentication domain conflict, the attributes authorized by the authentication server take precedence. Otherwise, all attributes take effect.
* Based on the authentication method (local authentication, remote server authentication, or local authentication after remote server authentication), the administrator privilege level is follows:
  + If local authentication is used, the following administrator privilege levels can be configured, which are listed in descending order of priority:
    - Local user privilege level configured using the **local-user** *user-name* **privilege level** *level* command
    - Administrator privilege level configured using the **admin-user privilege level** *level* command in the service scheme view
    - User privilege level configured using the **user privilege** command in the VTY user interface view
  + If remote authentication is used, the administrator privilege level is in the following descending order of priority:
    - User privilege level sent from the server to the device after the authentication is successful
    - Administrator privilege level configured using the **admin-user privilege level** *level* command in the service scheme view
    - User privilege level configured using the **user privilege** command in the VTY user interface view
  + If both remote authentication and local authentication are configured for a user and remote authentication takes precedence over local authentication: The administrator privilege level is that used during remote authentication. If the remote server does not respond, local authentication is used. In this case, the administrator privilege level is the local user privilege level configured using the **local-user** *user-name* **privilege level** *level* command.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the AAA view.
   
   
   ```
   [aaa](cmdqueryname=aaa)
   ```
3. Create an authorization scheme and enter the authorization scheme view.
   
   
   ```
   [authorization-scheme](cmdqueryname=authorization-scheme) authorization-scheme-name
   ```
4. Configure an authorization method.
   
   
   ```
   [authorization-mode](cmdqueryname=authorization-mode) { hwtacacs | if-authenticated | { local | local-case } | ldap } * [ none ]
   ```
   
   If **local** is specified, user names are case-insensitive. If **local-case** is specified, user names are case-sensitive.
5. (Optional) Configure command authorization based on user privilege levels.
   
   
   ```
   [authorization-cmd](cmdqueryname=authorization-cmd) [ privilege-level ] { hwtacacs | local } *[ none ]
   ```
   
   By default, command authorization is not configured for users at privilege levels 0 to 3.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * Only the HWTACACS server supports command authorization.
   * After the authorization scheme containing command authorization is applied in the administrator view, executing the **undo authorization-cmd** command will cause the administrator unable to execute any command except the **quit** command. In this case, the administrator needs to log in again.
6. (Optional) Configure the policy used when command authorization fails.
   
   
   ```
   [authorization-cmd no-response-policy](cmdqueryname=authorization-cmd+no-response-policy) { online | offline [ max-times max-times-value ] }
   ```
   
   By default, users are kept online if they fail command authorization.
7. (Optional) Return to the system view and enable the bypass authorization function and bypass command authorization function.
   
   
   * Set the bypass authorization time.
     ```
     [aaa-author-bypass](cmdqueryname=aaa-author-bypass) enable time time-value
     ```
     
     By default, the bypass authorization function is disabled.
   * Set the bypass command authorization time.
     ```
     [aaa-author-cmd-bypass](cmdqueryname=aaa-author-cmd-bypass) enable time time-value
     ```
     
     By default, the bypass command authorization function is disabled.
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the **display authorization-scheme** [ **name** *authorization-scheme-name* ] command to check the authorization scheme configuration.