Adjusting DHCPv4 Service Parameters
===================================

You can adjust DHCPv4 service parameters to enhance the
security of the DHCPv4 service.

#### Usage Scenario

After configuring a DHCPv4
server, you need to configure the security function of the DHCPv4
service. This enhances security of the DHCPv4 service and prevents
other unauthorized DHCPv4 servers from assigning invalid IP addresses
to clients. By viewing logs, the administrator determines whether
there are unauthorized DHCPv4 servers assigning invalid IP addresses
to clients.


#### Pre-configuration Tasks

Before adjusting
DHCPv4 parameters, configure a DHCPv4 server.


[(Optional) Configuring Global DHCPv4 Parameters](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv4_address_cfg_0037.html)

Global DHCPv4 parameters include the maximum number of DHCPv4 access users allowed for a specified board and the limit on the packet transmission rate of a DHCPv4 server group.

[Configuring a DHCP Option](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv4_address_cfg_0141.html)

DHCP provides a framework for parameter transmission over the TCP/IP network. The DHCP client and server can transmit the negotiated parameters and control information to each other through options.

[(Optional) Configuring the Format for Encapsulating the Option82 Attribute into DHCP Messages](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv4_address_cfg_0253.html)

This section describes how to enable a device to insert Sub-option 2 (remote ID) into the Option 82 attribute or replace Sub-option 2 carried in the Option 82 attribute of a message to be sent to the DHCP server based on a fixed format when addresses are assigned to Layer 2 users from a remote address pool.

[(Optional) Shortening the User Address Lease Before a DHCPv4 Server Restarts](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv4_address_cfg_0238.html)

The user address lease can be shortened before a DHCPv4 server restarts. This change allows DHCP users to get online within a short period of time after the DHCPv4 server restarts due to an upgrade without restarting the terminal.

[Configuring Transparent Transmission of DHCPv4 Packets](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv4_address_cfg_0039.html)

You need to configure transparent transmission of DHCPv4 packets when STB users send only one DHCPv4 Discover packet after they restart.

[(Optional) Enabling the BRAS to Transparently Transmit NAK Messages to DHCP Clients](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv4_address_cfg_0252.html)

In scenarios where IP addresses are assigned from a DHCPv4 remote address pool, if a DHCP client sends a Discover message to the DHCP server through a BRAS and the BRAS receives a NAK message from the DHCP server, the BRAS discards the NAK message by default. After the BRAS is enabled to transparently transmit NAK messages to clients, the clients can be informed of login failures if parsing of NAK messages is supported on the client terminals.

[Enabling a DHCPv4 Server to Detect Unauthorized DHCPv4 Servers](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv4_address_cfg_0043.html)

Enabling a DHCPv4 server to detect unauthorized DHCPv4 servers help prevent unauthorized DHCPv4 servers from allocating invalid IP addresses to clients.

[Configuring IP Address Conflict Detection](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv4_address_cfg_0044.html)

The DHCPv4 server sends ping packets to detect the usage of an IP address to prevent an IP address conflict.

[Saving DHCPv4 Data](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv4_address_cfg_0045.html)

After the DHCPv4 data of the NE40E that functions as a DHCPv4 server is saved to a storage device, the data can be restored from the storage device when the NE40E fails.

[Restoring DHCPv4 Data](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv4_address_cfg_0046.html)

DHCPv4 data restoration allows the NE40E that functions as a DHCPv4 server capable of saving DHCPv4 data to a storage device to restore saved information about address leases and address conflicts.

[(Optional) Configuring the NE40E to Log Out an Online User and Deny Access of a New User After Detecting an IPv4 Address Conflict](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv4_address_cfg_0002.html)

You can configure the NE40E to log out an online user and deny access of a new user if it detects that the IP address assigned to the new user from a remote address pool or by the RADIUS server is the same as the IP address of the online user.

[(Optional) Configuring the Device to Log Out a Dual-Stack User from Both IPv4 and IPv6 Stacks When a Zero Lease Is Delivered in a CoA Message for the User's IPv4 Address](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv4_address_cfg_0073.html)

This section describes how to configure the device to log out a dual-stack user from both IPv4 and IPv6 stacks and sends a DHCPv4 NAK message to the user when the RADIUS server delivers a zero lease for the user's IPv4 address in a CoA message and the user sends a Request message to renew the lease.

[Verifying the DHCPv4 Parameter Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ipv4_address_cfg_0047.html)

After adjusting DHCPv4 parameters, verify DHCPv4 server information and the storage path of the DHCPv4 data.