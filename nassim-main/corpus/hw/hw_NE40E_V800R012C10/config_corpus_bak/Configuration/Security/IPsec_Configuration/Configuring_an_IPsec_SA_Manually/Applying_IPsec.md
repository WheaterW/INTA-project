Applying IPsec
==============

After configuring IPsec, you can configure protocols to use it for protocol packet authentication.

#### Context

To defend against network attacks, configure IPsec so that IPsec can be implemented on protocol packets exchanged between Routers. [Table 1](#EN-US_TASK_0172372418__table_dc_vrp_ipsec_cfg_000901) describes IPsec applications.

**Table 1** IPsec applications
| Protocol | Usage scenario | Reference |
| --- | --- | --- |
| DHCPv6 Relay | If an attacker pretends to be a DHCPv6 server and sends bogus DHCPv6 messages to a client, the client may suffer from DoS attacks or be incorrectly configured. To defend against DoS attacks, implement IPsec on packets exchanged between DHCPv6 relay agents or between a DHCPv6 relay agent and a DHCPv6 server. | [Configuring IPsec on a DHCPv6 Relay Agent](dc_vrp_dhcpv6_relay_cfg_0012.html) |
| RIPng | If IPsec authentication is configured on a RIPng network, the sent and received RIPng packets will be authenticated, and those cannot pass authentication will be discarded. This can improve the security of the RIPng network. | [Configuring IPsec Authentication for RIPng](dc_vrp_ripng_cfg_0030.html) |
| OSPFv3 | OSPFv3 IPsec uses a set of IPsec mechanisms to authenticate sent and received OSPFv3 packets, protecting devices against invalid OSPFv3 packets. | [Configuring OSPFv3 IPsec](dc_vrp_ospfv3_cfg_2082.html) |
| IGMP | On a multicast network, forged IGMP messages may be used to attack devices, causing devices unable to forward multicast traffic. To protect a device against attacks launched using forged IGMP messages, use this feature to authenticate sent and received IGMP messages based on a specified SA. | [Configuring IGMP IPsec](dc_vrp_multicast_cfg_2247.html) |
| MLD | On a multicast network, forged MLD messages may be used to attack devices, causing devices unable to forward multicast traffic. To protect a device against attacks launched using forged MLD messages, use this feature to authenticate sent and received MLD messages based on a specified SA. | [Configuring MLD IPsec](dc_vrp_multicast_cfg_2233.html) |
| IPv4 PIM | On a multicast network, forged IPv4 PIM messages may be used to attack devices, causing devices unable to forward multicast traffic. To protect a device against attacks launched using forged IPv4 PIM messages, use this feature to authenticate sent and received IPv4 PIM messages based on a specified SA. | [Configuring IPv4 PIM IPsec](dc_vrp_multicast_cfg_2248.html) |
| IPv6 PIM | On a multicast network, forged IPv6 PIM messages may be used to attack devices, causing devices unable to forward multicast traffic. To protect a device against attacks launched using forged IPv6 PIM messages, use this feature to authenticate sent and received IPv6 PIM messages based on a specified SA. | [Configuring IPv6 PIM IPsec](dc_vrp_multicast_cfg_2234.html) |
| DHCP Relay | An attacker pretends to be a DHCPv4 relay agent and sends bogus DHCPv4 packets to the DHCPv4 server, which may cause a denial of service attack on the DHCPv4 server. The performs IPsec authentication on DHCPv4 packets between DHCPv4 relay agents or between DHCPv4 relay agents and servers to defend against network attacks. | [(Optional) Configuring IPsec on a DHCP Relay Agent](dc_vrp_dhcp_relay_cfg_0025.html) |
| DHCP Server | An attacker pretends to be a DHCPv4 server and sends bogus DHCP packets to the DHCPv4 relay agent, which may cause the DHCPv4 relay agent to suffer DoS attacks. The DHCPv4 relay agent performs IPsec authentication by sending DHCPv4 packets between the DHCPv4 server and the relay agent to defend against network attacks. | [(Optional) Configuring IPsec on a DHCP Server](dc_vrp_dhcp_server_cfg_0026.html) |