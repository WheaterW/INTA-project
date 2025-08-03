(Optional) Configuring the NE40E to Log Out an Online User and Deny Access of a New User After Detecting an IPv4 Address Conflict
=================================================================================================================================

You can configure the NE40E to log out an online user and deny access of a new user if it detects that the IP address assigned to the new user from a remote address pool or by the RADIUS server is the same as the IP address of the online user.

#### Context

To implement authentication, authorization, and accounting for users separately, users must use different IP addresses to go online. This requires the NE40E to detect whether the IP address assigned to a new user conflicts with that of an online user. By default, if the NE40E detects that the IP address assigned to a new user is the same as the IP address of an online user, it sends a DHCP Decline message to the DHCP server. Then the new user cannot go online, but the online user is not affected.

In scenarios in which IP addresses are assigned based on the Option 82 field that carries physical location information of users and ARP probe is not configured, the online user is required to go offline to allow the new user to go online. For example, if a CPE is replaced, users attached to the old CPE will switch to the new CPE to go online. As their physical location information remains the same, they will be assigned the same IP addresses as before. However, if the previous IP address lease has not expired, the user information is retained. Therefore, the NE40E considers that the users are already online and discards the user packets sent from the new CPE. Subsequently, the users fail to go online through the new CPE. To allow the users to go online through the new CPE, configure the NE40E to delete the previous user information and deny new user access so that the users can be triggered to go online again.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dhcp conflict-ip-address offline user**](cmdqueryname=dhcp+conflict-ip-address+offline+user) [ **include framed-ip** ]
   
   
   
   The NE40E is configured to log out an online user and deny access of a new user if it detects that the IP address assigned to the new user from a remote address pool or by the RADIUS server is the same as the IP address of the online user.
   
   When both the [**dhcp conflict-ip-address offline**](cmdqueryname=dhcp+conflict-ip-address+offline) and [**dhcp conflict-ip-address offline user**](cmdqueryname=dhcp+conflict-ip-address+offline+user) commands are run, a new user is assigned the IP address of an online user from a remote address pool, and the two users are both IPv4/IPv6 dual-stack users, the [**dhcp conflict-ip-address offline**](cmdqueryname=dhcp+conflict-ip-address+offline) command configuration takes effect. Specifically, the NE40E will log out the online user only from the IPv4 address after detecting the IPv4 address conflict.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.