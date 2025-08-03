Configuring a DHCPv4 Server Group
=================================

A DHCPv4 server group is required only when a remote address pool is used to assign IP addresses to users that use a BAS interface for access.

#### Usage Scenario

The NE40E can be used as a DHCPv4 server to assign IP addresses to users. A remote DHCPv4 server can also be used with the NE40E functioning as a DHCPv4 relay agent to assign IP addresses to users.

When IP addresses are allocated by a remote DHCPv4 server, you need to configure the IP address
of the remote DHCPv4 server on the NE40E. This allows the NE40E to communicate with
the DHCPv4 server. The NE40E manages DHCPv4 servers by using DHCPv4 server groups.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

A DHCPv4 server group is required only when the remote address
pool is used to assign IP addresses to BAS-side users.



#### Pre-configuration Tasks

None.


[Creating a DHCPv4 Server Group](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv4_address_cfg_0035.html)

DHCPv4 servers in a DHCPv4 server group can work in load balancing, polling, or master/backup mode.

[Associating an IP Address Pool with a DHCPv4 Server Group](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv4_address_cfg_0056.html)

Only remote IP address pools need to be associated with DHCPv4 server groups.

[Verifying the DHCPv4 Server Group Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv4_address_cfg_0040.html)

After configuring DHCPv4 server groups, verify the configurations of these DHCPv4 server groups.