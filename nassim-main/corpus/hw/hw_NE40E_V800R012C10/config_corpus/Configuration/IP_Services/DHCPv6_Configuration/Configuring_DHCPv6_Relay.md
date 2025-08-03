Configuring DHCPv6 Relay
========================

When a DHCPv6 client and a DHCPv6 server reside on different links, configure a DHCPv6 relay agent to relay DHCPv6 messages between the client and server.

#### Usage Scenario

On the network shown in [Figure 1](#EN-US_TASK_0139427859__fig_dc_vrp_dhcpv6_relay_cfg_000301), DHCPv6 clients reside on Network A, and the DHCPv6 server resides on Network B. A DHCPv6 relay agent must be configured to relay DHCPv6 messages between the clients and server so that the clients can apply for IPv6 addresses from the server.

**Figure 1** Configuring DHCPv6 relay  
![](images/fig_dc_vrp_dhcpv6_relay_cfg_000301.png)  
#### Pre-configuration Tasks

Before configuring DHCPv6 relay, complete the following tasks:

* Configure a DHCPv6 server.
* Configure a DHCPv6 relay interface.
* Configure a route from the DHCPv6 server to the DHCPv6 relay interface.


[Enabling DHCPv6](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcpv6_relay_cfg_0013.html)

DHCPv6 provides client, relay, and server functions.

[Configuring DHCPv6 Relay Forwarding](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcpv6_relay_cfg_0004.html)

DHCPv6 relay forwarding functions are configured on the user-side inbound interface of DHCPv6 messages. You can specify the outbound interface, destination DHCPv6 server address, or next-hop DHCPv6 relay agent address.

[(Optional) Configuring DHCPv6 PD Relay Functions](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcpv6_relay_cfg_0014.html)

A DHCPv6 relay agent can be configured to advertise DHCPv6 PD routes, limit the maximum number of access DHCPv6 clients, and check the physical information of DHCPv6 messages.

[(Optional) Configuring DHCPv6 Relay Dual-Device Hot Standby in a VRRP/VRRP6 Master/Backup Backup Scenario](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcpv6_relay_cfg_0018.html)

DHCPv6 relay dual-device hot standby can be enabled to back up user entries between devices. If a network node or link fails, a rapid user service switchover is triggered, improving service reliability.

[(Optional) Configuring DHCPv6 Relay Options](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcpv6_relay_cfg_0005.html)

DHCPv6 relay options include the Interface-ID option, Subscriber-ID option, and Remote-ID option. These options carry detailed user information for address assignment and parameter configuration.

[(Optional) Configuring IPsec on a DHCPv6 Relay Agent](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcpv6_relay_cfg_0012.html)

To defend against DoS attacks, configure IPsec on a DHCPv6 relay agent so that IPsec can be implemented on packets exchanged between DHCPv6 relay agents or between the DHCPv6 relay agent and DHCPv6 server.

[(Optional) Configuring CAR for Whitelisted DHCPv6 Sessions](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcpv6_relay_cfg_0020.html)

You can configure an aging time and bandwidth parameters for CAR for whitelisted DHCPv6 sessions to flexibly isolate the sessions.

[Verifying the Configuration of DHCPv6 Relay](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcpv6_relay_cfg_0006.html)

After configuring DHCPv6 relay on a host or router, verify the configuration.