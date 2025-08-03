(Optional) Configuring Re-authentication for Users
==================================================

(Optional) Configuring Re-authentication for Users

#### Context

When users are in pre-connection state or fail authentication, you can configure bypass rights for the users on the device and enable the device to record the corresponding entry information. To ensure that users are successfully authenticated in a timely manner and obtain normal network access rights, the device can re-authenticate those who fail authentication based on user entries.

If a user is successfully re-authenticated before the aging time of the user entry expires, the device adds the user to the list of successfully authenticated users and grants network access rights to the user. If the user fails the re-authentication when the aging time expires, the device deletes the corresponding user entry and reclaims the bypass rights granted to the user.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the authentication profile view.
   
   
   ```
   [authentication-profile](cmdqueryname=authentication-profile) name authentication-string
   ```
3. Configure the re-authentication period for pre-connection users or users who fail authentication.
   
   
   ```
   [authentication timer re-authen](cmdqueryname=authentication+timer+re-authen) { pre-authen pre-authen-time | authen-fail authen-fail-time }
   ```
   
   
   
   By default, the interval for re-authenticating pre-connection users or users who fail authentication is 60s.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   When many users need to be re-authenticated, to reduce the impact of re-authentication on device performance, the actual re-authentication period may be longer than the configured re-authentication period.
4. Enable the device to re-authenticate users in authentication bypass state when the authentication server changes from down to up.
   
   
   ```
   [authentication event authen-server-up action re-authen](cmdqueryname=authentication+event+authen-server-up+action+re-authen)
   ```
   
   By default, the device does not re-authenticate users in authentication bypass state when the authentication server changes from down to up.
5. (Optional) Disable the function of re-authenticating users when the authentication server is down.
   
   
   ```
   [authentication event authen-server-down action close re-authen](cmdqueryname=authentication+event+authen-server-down+action+close+re-authen)
   ```
   
   By default, the function of re-authenticating users when the authentication server is down is enabled.
   
   If re-authentication is performed on users when the authentication server is down and users fail authentication multiple times over a short period, the users may enter the quiet state. As a result, the configured bypass rights cannot be used. To prevent this problem, you are advised to disable the function of re-authenticating users when the authentication server is down.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```