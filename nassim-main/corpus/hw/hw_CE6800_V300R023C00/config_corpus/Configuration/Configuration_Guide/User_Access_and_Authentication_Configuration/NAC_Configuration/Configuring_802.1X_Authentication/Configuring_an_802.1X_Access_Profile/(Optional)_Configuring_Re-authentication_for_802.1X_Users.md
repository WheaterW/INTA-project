(Optional) Configuring Re-authentication for 802.1X Users
=========================================================

(Optional) Configuring Re-authentication for 802.1X Users

#### Context

If the administrator modifies parameters such as access rights and authorization attributes of an online user on the authentication server, the user needs to be re-authenticated to ensure user validity.

If re-authentication is configured for online 802.1X users, the device sends online users' authentication parameters that it has saved upon users' going online to the authentication server for re-authentication. If the authentication information of a user on the authentication server remains unchanged, the user remains online. If the information has been modified, the user is disconnected and needs to be re-authenticated.

Two methods are available to enable the device to re-authenticate 802.1X users:

* Configure the device to periodically re-authenticate 802.1X users using a specified 802.1X access profile.
  
  ![](public_sys-resources/note_3.0-en-us.png) 
  + After this function is configured, many 802.1X authentication logs will be generated.
  + If the device is connected to a server for re-authentication and the server replies with a re-authentication deny message that makes an online user go offline, it is recommended that you locate the cause of the re-authentication failure on the server or disable the re-authentication function on the device.


#### Procedure

* Configure periodic automatic re-authentication.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the 802.1X access profile view.
     
     
     ```
     [dot1x-access-profile](cmdqueryname=dot1x-access-profile) name access-profile-name
     ```
  3. Configure the device to re-authenticate online 802.1X users.
     
     
     ```
     [dot1x reauthenticate](cmdqueryname=dot1x+reauthenticate)
     ```
     
     By default, the device does not re-authenticate online 802.1X users.
  4. (Optional) Configure the re-authentication period for online 802.1X users.
     
     
     ```
     [dot1x timer](cmdqueryname=dot1x+timer) reauthenticate-period reauthenticate-period-value
     ```
     
     By default, the re-authentication period is 3600 seconds for online 802.1X users.
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     + In most cases, the default re-authentication period is recommended.
     + When remote authentication and authorization are used, a short re-authentication period may cause a high CPU usage.
     + When many users need to be re-authenticated, to reduce the impact of re-authentication on device performance, the actual re-authentication period may be longer than the configured re-authentication period.
  5. Commit the configuration.
     
     
     ```
     commit
     ```