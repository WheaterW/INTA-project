Configuring the Function of Triggering 802.1X Authentication Through Multicast Packets Immediately After an Interface Goes Up (802.1X Authentication)
=====================================================================================================================================================

Configuring the Function of Triggering 802.1X Authentication Through Multicast Packets Immediately After an Interface Goes Up (802.1X Authentication)

#### Context

By default, the device periodically multicasts EAP-Request/Identity packets to clients to enable the clients to send EAPoL-Start packets for 802.1X authentication. If the device interface connecting to a client changes from down to up, the client needs to send EAPoL-Start packets again for 802.1X authentication. This can take a long time. To shorten the re-authentication time, enable the function of triggering 802.1X authentication through multicast packets immediately after the device interface goes up.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the function of triggering 802.1X authentication through multicast packets.
   
   
   ```
   [dot1x mc-trigger](cmdqueryname=dot1x+mc-trigger)
   ```
   
   By default, the function of triggering 802.1X authentication through multicast packets is enabled.
3. Enable the function of triggering 802.1X authentication through multicast packets immediately after an interface goes up.
   
   
   ```
   [dot1x mc-trigger port-up-send enable](cmdqueryname=dot1x+mc-trigger+port-up-send+enable)
   ```
   
   By default, the function of triggering 802.1X authentication through multicast packets immediately after an interface goes up is disabled.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```