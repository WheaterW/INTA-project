Configuring an Authentication Profile and Binding It to an 802.1X Access Profile
================================================================================

Configuring an Authentication Profile and Binding It to an 802.1X Access Profile

#### Prerequisites

An 802.1X access profile has been configured. For details, see [Configuring an 802.1X Access Profile](galaxy_nac_cfg_0048.html).


#### Context

The device uses an authentication profile to uniformly manage configurations irrelevant to the user access mode. You can bind a specified access profile to the authentication profile to determine the authentication mode used by the authentication profile.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create an authentication profile and enter the authentication profile view.
   
   
   ```
   [authentication-profile](cmdqueryname=authentication-profile) name authentication-string
   ```
   
   To delete an authentication profile, ensure that it is not bound to any interface.
3. Bind an 802.1X access profile to the authentication profile.
   
   
   ```
   [dot1x-access-profile](cmdqueryname=dot1x-access-profile) access-profile-name
   ```
4. (Optional) Configure a default or forcible domain for users.
   
   
   ```
   [access-domain](cmdqueryname=access-domain) name [ dot1x ] [ force ]
   ```
   
   By default, no default or forcible domain is configured for users in an authentication profile.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * If the **force** parameter is specified in the command, a forcible domain is configured. Otherwise, a default domain is configured. If both a default domain and a forcible domain are configured for users, the device authenticates the users in the forcible domain.
   * If you do not specify **dot1x** in the command, the configured domain takes effect for all users using the authentication profile. If you specify **dot1x** in the command, the configured domain takes effect only for specified users.
5. (Optional) Configure the device to handshake with pre-connection and authorized users.
   
   
   1. Enable the handshake function.
      
      ```
      [authentication handshake](cmdqueryname=authentication+handshake)
      ```
      
      By default, the handshake with pre-connection and authorized users is enabled.
   2. Configure the handshake period.
      
      ```
      [authentication timer handshake-period](cmdqueryname=authentication+timer+handshake-period) handshake-period-value [ handshake-times handshake-times-value ]
      ```
      
      By default, the handshake period of the device with pre-connection users and authorized users is 100 seconds and the number of handshakes is 3.
6. (Optional) Disable the device from creating an IP hash table for client IP addresses.
   
   
   ```
   [authentication no-ip-check](cmdqueryname=authentication+no-ip-check)
   ```
   
   By default, the device creates an IP hash table for client IP addresses.
7. (Optional) Enable the device to perform conflict detection on client IP addresses.
   
   
   ```
   [authentication ip-conflict-check enable](cmdqueryname=authentication+ip-conflict-check+enable)
   ```
   
   By default, the device performs conflict detection on client IP addresses.
8. (Optional) Configure the delay after which users are logged out following an interface link fault.
   
   
   ```
   [link-down offline delay](cmdqueryname=link-down+offline+delay) { delay-value | unlimited }
   ```
   
   By default, the delay after which users are logged out following an interface link fault is 10 seconds.
   
   If the delay is set to 0, users are logged out immediately following an interface link fault. If the delay is set to **unlimited**, users are not logged out.
9. (Optional) Enable the function of triggering authentication by ARP reply packets.
   
   
   ```
   [authentication arp-reply trigger](cmdqueryname=authentication+arp-reply+trigger)
   ```
   
   By default, the function of triggering authentication by ARP reply packets is enabled.
10. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```