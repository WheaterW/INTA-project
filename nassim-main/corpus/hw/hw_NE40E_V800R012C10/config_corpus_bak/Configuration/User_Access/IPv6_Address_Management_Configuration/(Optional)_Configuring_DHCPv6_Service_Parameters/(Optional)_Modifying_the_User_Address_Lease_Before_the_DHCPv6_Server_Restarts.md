(Optional) Modifying the User Address Lease Before the DHCPv6 Server Restarts
=============================================================================

The user address lease can be shortened. This change allows DHCPv6 users to get online within a short period of time due to the DHCPv6 server upgrade without restarting the terminal.

#### Context

When the NE40E is being upgraded, DHCPv6 users cannot detect that the link goes Down and dial-up again like PPP users. Therefore, these users do not redial to get online. Instead, the terminal must be restarted to trigger a DHCPv6 request so that the users can obtain IP addresses to get online again. In the current upgrade solution, the address pool lease time is shortened at the lease renewal time before the upgrade date. This solution ensures that the terminal can send lease renewal packets in a shorter period of time after the device is upgraded to allow DHCPv6 users to get online again.

This upgrade solution has two disadvantages:

* Changing the address pool lease takes effect only for users that obtain addresses from local address pools. The address lease delivered by a RADIUS server is not changed. The users that have obtained addresses from the RADIUS server have to wait a comparatively long period of time to get online again.
* The address pool lease is configured in the address pool view. Manually changing the lease configurations of all the address pools brings a huge workload.

Using the [**dhcpv6 upgrade**](cmdqueryname=dhcpv6+upgrade) command in the system view to change the address lease for all DHCP users attached to the device solves these problems.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dhcpv6 upgrade**](cmdqueryname=dhcpv6+upgrade) **preferred-lifetime** *days* [ *hours* [ *minutes* ] ] **valid-lifetime** *day*s [ *hours* [ *minutes* ] ] [ **renew-time-percent** *renew-time-value* ] [ **rebind-time-percent** *rebind-time-value* ]
   
   
   
   The address lease for all DHCPv6 users attached to the device is configured.
   
   After the **dhcpv6 upgrade** command is used, the lease configured in the system view takes effect for new users, online users that need to renew the lease, users using addresses/prefixes in local and delegation address pools, and users using addresses/prefixes delivered by a RADIUS server.
   
   No configuration file will be generated after the **dhcpv6 upgrade** command is used. To view the configuration result, run the **display dhcpv6 upgrade** command. The **dhcpv6 upgrade** command becomes invalid after the device restarts.
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   If a short lease is configured, a large number of users will renew their lease at the same time, causing high CPU usage. Therefore, configuring a short lease is not recommended unless the device needs to be upgraded.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.