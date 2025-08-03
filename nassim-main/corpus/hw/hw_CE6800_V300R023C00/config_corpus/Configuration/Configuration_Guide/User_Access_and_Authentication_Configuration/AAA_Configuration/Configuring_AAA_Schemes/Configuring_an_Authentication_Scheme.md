Configuring an Authentication Scheme
====================================

Configuring an Authentication Scheme

#### Context

An authentication scheme defines the authentication methods used for user authentication and the order in which authentication methods take effect. To prevent authentication failures caused by a single authentication method failing to respond, you can configure local authentication as the backup authentication method in the authentication scheme.

![](public_sys-resources/note_3.0-en-us.png) 

* If the authentication method is set to non-authentication using the [**authentication-mode**](cmdqueryname=authentication-mode) [**none**](cmdqueryname=none) command, an access user will be authenticated successfully after entering any user name and password for login. Therefore, for security purposes, you are advised to set an authentication method other than non-authentication to ensure that only authenticated users can access the device or network.
* If the authentication method is set to non-authentication using the [**authentication-mode**](cmdqueryname=authentication-mode) [**none**](cmdqueryname=none) command, administrators are not allowed to go online. If the authentication method of administrators is set to AAA authentication using the **authentication-mode** command in the user interface view, the device does not allow administrators to log in from the user interface view.
* Third-party authentication may lack security mechanisms such as password complexity check and brute force attack defense. Check whether third-party authentication is used.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the AAA view.
   
   
   ```
   [aaa](cmdqueryname=aaa)
   ```
3. Create an authentication scheme and enter the authentication scheme view.
   
   
   ```
   [authentication-scheme](cmdqueryname=authentication-scheme) authentication-scheme-name
   ```
4. Configure an authentication method.
   
   
   ```
   [authentication-mode](cmdqueryname=authentication-mode) { hwtacacs | { local | local-case } | radius | ldap | } * [ none ]
   ```
   
   If **local** is specified, user names are case-insensitive. If **local-case** is specified, user names are case-sensitive.
   
   If you run the [**authentication-mode**](cmdqueryname=authentication-mode) [**none**](cmdqueryname=none) command to set the authentication mode to non-authentication and AAA authentication is configured for administrators in the user interface view, the device does not allow administrators in the user interface view to log in to the device.
5. (Optional) Configure administrators to replace PAP authentication with CHAP authentication during RADIUS authentication.
   
   
   ```
   [authentication-type radius chap access-type admin](cmdqueryname=authentication-type+radius+chap+access-type+admin) [ ftp | ssh | telnet | terminal | http | snmp | md-cli ] *
   ```
   
   
   
   By default, administrators use PAP authentication during RADIUS authentication.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   After the Federal Information Processing Standards (FIPS) mode is enabled, CHAP authentication is used by default during RADIUS authentication.
6. (Optional) Configure the device not to send accounting packets when local authentication is triggered because the server does not respond to users' authentication requests.
   
   
   ```
   [undo server no-response accounting](cmdqueryname=undo+server+no-response+accounting)
   ```
   
   By default, if server accounting is configured, the device does not send accounting packets when local authentication is triggered because the server does not respond to users' authentication requests.
7. (Optional) Configure the device to perform local authorization without sending authorization packets when local authentication is triggered because the server does not respond to users' authentication requests.
   
   
   ```
   undo server no-response authorization
   ```
   
   By default, if both server authentication and local authentication are configured, the device directly requests local authorization when local authentication is triggered because the server does not respond to users' authentication requests.
8. (Optional) Configure local authentication for administrators if RADIUS authentication is rejected.
   
   
   ```
   [radius-reject local](cmdqueryname=radius-reject+local)
   ```
   
   By default, local authentication is not configured for administrators if RADIUS authentication is rejected. After the RADIUS server responds with an Access-Reject packet, the authentication process ends and the user fails authentication.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * This function takes effect only for administrators.
   * The authentication method must be RADIUS authentication+local authentication.
9. Return to the AAA view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
10. (Optional) Configure the system to lock out accounts that fail remote AAA authentication.
    
    
    * Enable the system to lock out administrators that fail remote authentication, and configure the authentication retry interval, maximum number of consecutive failed password attempts, and account lockout duration.
      ```
      administrator remote authen-fail retry-interval retry-interval retry-time retry-time block-time block-time
      ```
      Alternatively, enable the system to lock out access users who fail remote authentication, and configure the authentication retry interval, maximum number of consecutive failed password attempts, and account lockout duration.
      ```
      [access-user remote authen-fail](cmdqueryname=access-user+remote+authen-fail) retry-interval retry-interval retry-time retry-time block-time block-time
      ```
      
      By default, the account locking function is enabled for administrators who fail remote authentication and is disabled for access users who fail remote authentication. When users fail remote authentication, the authentication retry interval defaults to 5 minutes, the maximum number of consecutive failed password attempts defaults to 30, and the account lockout duration defaults to 5 minutes.
    * Configure users to access the network using a specified IP address when user accounts are locked out.
      ```
      [aaa-quiet administrator except-list](cmdqueryname=aaa-quiet+administrator+except-list) { ipv4-address | ipv6-address }  &<1-32>
      ```
      
      By default, users cannot access the network when their accounts are locked out.
      
      This function takes effect only for administrators.
      
      To check information about the specified IP address, run the [**display aaa-quiet administrator except-list**](cmdqueryname=display+aaa-quiet+administrator+except-list) command.
    * Unlock the account that is locked out after remote AAA authentication fails.
      ```
      [remote-user authen-fail unblock](cmdqueryname=remote-user+authen-fail+unblock) { all | username username }
      ```
11. (Optional) Configure the system to lock out accounts that fail local authentication.
    
    
    * Enable the system to lock out accounts that fail local authentication, and configure the authentication retry interval, maximum number of consecutive failed password attempts, and account lockout duration.
      ```
      [local-aaa-user wrong-password](cmdqueryname=local-aaa-user+wrong-password) retry-interval retry-interval retry-time retry-time block-time block-time
      ```
      
      By default, the function of locking out accounts that fail local authentication is enabled, the authentication retry interval is 5 minutes, the maximum number of consecutive failed password attempts is 3, and the account lockout duration is 5 minutes.
    * Configure users to access the network using a specified IP address when user accounts are locked out.
      ```
      [aaa-quiet administrator except-list](cmdqueryname=aaa-quiet+administrator+except-list) { ipv4-address | ipv6-address }  &<1-32>
      ```
      
      By default, users cannot access the network when their accounts are locked out.
      
      This function takes effect only for administrators.
      
      To check information about the specified IP address, run the [**display aaa-quiet administrator except-list**](cmdqueryname=display+aaa-quiet+administrator+except-list) command.
    * Unlock the account that is locked out after local authentication fails.
      ```
      [local-user](cmdqueryname=local-user) user-name state active
      ```
12. (Optional) Configure a trusted host IP address. After this step is performed, only the administrator using this IP address is authenticated based on the user name and password. The administrators using other IP addresses are not allowed to log in.
    
    
    ```
    [aaa-bind administrator ip](cmdqueryname=aaa-bind+administrator+ip) { ipv4-address | ipv6-address } &<1-8>
    ```
    
    By default, no trusted host IP address is configured on the device.
    
    The CE6885-LL supports the *ipv6-address* parameter only in standard forwarding mode.
    
    This function takes effect only for administrators.
    
    To check the configured trusted host IP address, run the [**display aaa-bind administrator ip**](cmdqueryname=display+aaa-bind+administrator+ip) command.
13. (Optional) Disable the device from disconnecting or re-authenticating users when the RADIUS server delivers the Session-Timeout attribute with the value 0.
    
    
    ```
    aaa-author session-timeout invalid-value enable
    ```
    
    By default, when the RADIUS server delivers the Session-Timeout attribute with the value 0, this attribute does not take effect.
14. Return to the system view.
    
    
    ```
    [quit](cmdqueryname=quit)
    ```
15. (Optional) Enable the bypass authentication function.
    
    
    ```
    [aaa-](cmdqueryname=aaa-)authen[-bypass](cmdqueryname=-bypass) enable time time-value
    ```
    
    By default, the bypass authentication function is disabled.
16. (Optional) Enable system log suppression.
    
    
    1. Enable system log suppression.
       ```
       access-user syslog-restrain enable
       ```
       
       By default, the system log suppression function is disabled.
    2. Configure the system log suppression period.
       ```
       [access-user syslog-restrain period](cmdqueryname=access-user+syslog-restrain+period) period
       ```
       
       By default, the system log suppression period is 300s.
17. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```

#### Verifying the Configuration

Run the **display authentication-scheme** [ **name** *authentication-scheme-name* ] command to check the authentication scheme configuration.