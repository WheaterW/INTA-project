(Optional) Configuring the Device to Log Out a Dual-Stack User from Both IPv4 and IPv6 Stacks When a Zero Lease Is Delivered in a CoA Message for the User's IPv4 Address
=========================================================================================================================================================================

This section describes how to configure the device to log
out a dual-stack user from both IPv4 and IPv6 stacks and sends a DHCPv4
NAK message to the user when the RADIUS server delivers a zero lease
for the user's IPv4 address in a CoA message and the user sends a
Request message to renew the lease.

#### Context

By default, a device logs out a dual-stack user from only
the IPv4 stack and sends a DHCPv4 NAK message to the user when the
RADIUS server delivers a zero lease for the user's IPv4 address in
a CoA message and the user sends a Request message to renew the lease.
To enable the device to logout a dual-stack user from both IPv4 and
IPv6 stacks, run the [**dhcp coa-zero-lease dual-cut**](cmdqueryname=dhcp+coa-zero-lease+dual-cut) command.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**domain**](cmdqueryname=domain) *domain-name*
   
   
   
   The AAA domain view is displayed.
4. Run [**dhcp coa-zero-lease dual-cut**](cmdqueryname=dhcp+coa-zero-lease+dual-cut)
   
   
   
   The device is enabled to log out a dual-stack user from both
   IPv4 and IPv6 stacks and sends a DHCPv4 NAK message to the user when
   the RADIUS server delivers a zero lease for the user's IPv4 address
   in a CoA message and the user sends a Request message to renew the
   lease.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.