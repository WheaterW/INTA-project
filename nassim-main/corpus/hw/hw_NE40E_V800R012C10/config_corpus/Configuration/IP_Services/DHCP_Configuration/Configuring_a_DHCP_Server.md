Configuring a DHCP Server
=========================

A DHCP server selects available IP addresses from the global address pool and assigns these IP addresses to DHCP clients.

#### Usage Scenario

A DHCP server that uses a global address pool is configured to dynamically assign IP addresses to computers that are indirectly connected to the DHCP server, as shown in [Figure 1](#EN-US_TASK_0172364694__fig_dc_vrp_dhcp_server_cfg_001101).

**Figure 1** IP address assignment based on an address pool  
![](images/fig_dc_vrp_dhcp_server_cfg_001101.png)
#### Pre-configuration Tasks

Before configuring the DHCP server, complete the following tasks:

* Implement the connectivity between the DHCP client and server.
* (Optional) Configure a DNS server.
* (Optional) Configure a network basic input/output system (NetBIOS) server.
* (Optional) Configure routes between the DNS server and NetBIOS server.
* (Optional) Configure the DHCP global address pool option.


[Configuring IP Address Assignment](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcp_server_cfg_0012.html)

IP address assignment includes specifying such basic information as a gateway address and address segments, as well as configuring static binding.

[(Optional) Configuring IP Address Management](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcp_server_cfg_0013.html)

IP address management includes backing up and restoring data in an address pool, configuring alarm thresholds, and reclaiming IP addresses.

[(Optional) Configuring Address Pool Attributes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcp_server_cfg_0014.html)

Configuring address pool attributes includes specifying an IP address lease, configuring the application server address and customized items. The address pool attributes are contained in option information that is sent by the DHCP server to clients.

[(Optional) Configuring DHCP Server Dual-Device Hot Backup](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcp_server_cfg_0021.html)

DHCP server dual-device hot backup can be enabled to achieve backup of user session information between devices. When a network node or link experiences an abnormality, fast user service switching is triggered, which enhances service reliability.

[(Optional) Configuring Parameters for DHCP User Access Restriction](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcp_server_cfg_0024.html)



[(Optional) Configuring a Server to Force a Client to Renew the IP Address](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcp_server_cfg_0025.html)



[(Optional) Configuring IPsec on a DHCP Server](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcp_server_cfg_0026.html)

To defend against certain network attacks, configure IPsec to authenticate messages between a DHCP relay agent and server.

[Verifying the Configuration of a DHCP Server](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcp_server_cfg_0015.html)

After configuring the DHCP server, verify the configuration.