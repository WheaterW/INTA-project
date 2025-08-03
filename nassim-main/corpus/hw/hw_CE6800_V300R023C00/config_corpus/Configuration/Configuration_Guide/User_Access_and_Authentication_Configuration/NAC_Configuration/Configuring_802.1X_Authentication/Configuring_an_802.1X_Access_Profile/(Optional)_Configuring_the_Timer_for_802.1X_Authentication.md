(Optional) Configuring the Timer for 802.1X Authentication
==========================================================

(Optional) Configuring the Timer for 802.1X Authentication

#### Context

In 802.1X authentication, a timer is used to control the retransmission of EAP-Request/Identity packets and EAP-Request/MD5 Challenge packets.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure the interval for sending 802.1X authentication requests.
   
   
   ```
   [dot1x timer](cmdqueryname=dot1x+timer) tx-period tx-period-value
   ```
   
   By default, the device sends 802.1X authentication requests at an interval of 30 seconds.
3. Enter the 802.1X access profile view.
   
   
   ```
   [dot1x-access-profile](cmdqueryname=dot1x-access-profile) name access-profile-name
   ```
4. Configure the authentication timeout timer for 802.1X clients.
   
   
   ```
   [dot1x timer](cmdqueryname=dot1x+timer) client-timeout client-timeout-value
   ```
   
   By default, the authentication timeout timer for 802.1X clients is enabled and its value is 5 seconds.
5. Configure the maximum number of times the device retransmits an authentication request to an 802.1X user.
   
   
   ```
   [dot1x retry](cmdqueryname=dot1x+retry) max-retry-value
   ```
   
   By default, the device retransmits an authentication request to an 802.1X user twice.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```