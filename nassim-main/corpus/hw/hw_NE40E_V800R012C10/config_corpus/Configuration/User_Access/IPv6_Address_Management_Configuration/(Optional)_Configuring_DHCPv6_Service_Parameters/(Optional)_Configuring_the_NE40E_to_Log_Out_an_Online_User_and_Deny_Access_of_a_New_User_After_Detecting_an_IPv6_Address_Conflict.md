(Optional) Configuring the NE40E to Log Out an Online User and Deny Access of a New User After Detecting an IPv6 Address Conflict
=================================================================================================================================

You can configure the NE40E to log out an online user and deny access of a new user
if it detects that the IPv6 address assigned to the new user from
a remote address pool or by the RADIUS server is the same as the IPv6
address of the online user.

#### Context

To implement authentication, authorization, and accounting
for users separately, users must use different IPv6 addresses to go
online. This requires the NE40E to detect whether the IPv6 address assigned to a new user
conflicts with that of an online user. By default, if the NE40E detects that the IPv6 address assigned to a new user is
the same as the IPv6 address of an online user, it sends a DHCPv6
Decline message to the DHCPv6 server. Then the new user cannot go
online, but the online user is not affected.

In scenarios in
which IPv6 addresses are assigned based on the Option 82 field that
carries physical location information of users and ARP probe is not
configured, the online user is required to go offline to allow the
new user to go online. For example, if a CPE is replaced, users attached
to the old CPE will switch to the new CPE to go online. As their physical
location information remains the same, they will be assigned the same
IPv6 addresses as before. However, if the previous IPv6 address lease
has not expired, the user information is retained. Therefore, the NE40E considers that the users are already online and discards
the user packets sent from the new CPE. Subsequently, the users fail
to go online through the new CPE. To allow the users to go online
through the new CPE, configure the NE40E to delete the previous user information and deny new user
access so that the users can be triggered to go online again.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dhcpv6 conflict-ip-address offline user**](cmdqueryname=dhcpv6+conflict-ip-address+offline+user) [ **include framed-ipv6** ]
   
   
   
   The NE40E is configured to log out an online user and deny access
   of a new user if it detects that the IPv6 address assigned to the
   new user from a remote address pool or by the RADIUS server is the
   same as the IPv6 address of the online user.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.