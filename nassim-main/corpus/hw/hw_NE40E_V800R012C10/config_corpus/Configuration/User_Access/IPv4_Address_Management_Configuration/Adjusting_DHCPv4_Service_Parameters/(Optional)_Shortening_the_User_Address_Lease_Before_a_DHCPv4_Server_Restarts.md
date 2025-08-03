(Optional) Shortening the User Address Lease Before a DHCPv4 Server Restarts
============================================================================

The user address lease can be shortened before a DHCPv4 server restarts. This change allows DHCP users to get online within a short period of time after the DHCPv4 server restarts due to an upgrade without restarting the terminal.

#### Context

When the NE40E is being upgraded, DHCP users cannot detect that the link goes Down and dial-up again like PPP users. Therefore, these users do not redial to get online. Instead, the terminal must be restarted to trigger a DHCP request so that the users can obtain IP addresses to get online again. In the current upgrade solution, the address pool lease time is shortened at the lease renewal time before the upgrade date. For example, if the address pool lease renewal time is 1.5 days, the address pool lease is changed to 30 minutes and the lease renewal time is changed to 15 minutes 1.5 days before the upgrade. This solution ensures that the terminal can send lease renewal packets in a shorter period of time after the device is upgraded to allow DHCP users to get online again.

This upgrade solution has two disadvantages:

* Changing the address pool lease takes effect only for users that obtain addresses from local address pools. The address lease delivered by a RADIUS server is not changed. The users that have obtained addresses from the RADIUS server have to wait a comparatively long period of time to get online again.
* The address pool lease is configured in the address pool view. Manually changing the lease configurations of all the address pools brings a huge workload.

Using the [**dhcp upgrade**](cmdqueryname=dhcp+upgrade) command in the system view to change the address lease for all DHCP users attached to the device solves these problems.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dhcp upgrade**](cmdqueryname=dhcp+upgrade) **lease** *days* [ *hours* [ *minutes* ] ] [ **renewal-time** *days* [ *hours* [ *minutes* ] ] ] [ **rebinding-time** *days* [ *hours* [ *minutes* ] ] ]
   
   
   
   The address lease for all DHCPv4 users attached to the device is configured.
   
   After the **dhcp upgrade** command is used, the lease configured in the system view takes effect for new users, online users that need to renew the lease, users using addresses in local address pools, and users using addresses delivered by a RADIUS server.
   
   No configuration file will be generated after the **dhcp upgrade** command is used. To view the configuration result, run the **display dhcp upgrade** command. The **dhcp upgrade** command becomes invalid after the device restarts.
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   If a short lease is configured, a large number of users will renew their lease at the same time, causing high CPU usage. Therefore, configuring a short lease is not recommended unless the device needs to be upgraded.
   
   This command is automatically deleted after the device is upgraded.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.