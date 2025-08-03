Configuring DHCP Relay
======================

This section describes how to configure DHCP relay so that DHCP messages can be relayed between DHCP clients and the DHCP server that reside on different network segments.

#### Usage Scenario

As shown in [Figure 1](#EN-US_TASK_0172364687__fig_dc_vrp_dhcp_relay_cfg_000301), DHCP clients are located on network A, and the DHCP server is located on network B. The DHCP clients request configuration parameters, such as IP addresses from the DHCP server. To allow the DHCP clients to obtain IP addresses from the DHCP server, configure DHCP relay so that the DHCP relay agent can forward DHCP messages between the DHCP clients and the DHCP server.

**Figure 1** DHCP relay networking
  
![](images/fig_dc_vrp_dhcp_relay_cfg_000301.png)  

#### Pre-configuration Tasks

Before configuring DHCP relay, complete the following tasks:

* Configure a DHCP server.
* Configure a DHCP relay interface.
* Configure a route from the DHCP relay agent to the DHCP server.

#### Configuration Procedures



[Configuring DHCP Relay](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcp_relay_cfg_0021.html)

After a DHCP relay agent is configured, it can forward DHCP Request messages from DHCP clients to the DHCP server on a different network segment.

[Configuring DHCP Relay Proxy](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcp_relay_cfg_0200.html)

To isolate a DHCP server and defend against attacks, you can enable DHCP relay proxy on the DHCP relay agent.

[(Optional) Requesting the DHCP Server to Release the Client IP Address](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcp_relay_cfg_0005.html)

The DHCP relay agent can request the DHCP server for releasing the IP address assigned to the client.

[(Optional) Configuring Option 82 Field Insertion](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcp-snooping_cfg_0016_dhcp-snooping.html)

After Option 82 field insertion is enabled on a device, the device can record the location information of a DHCP client or create binding entries with accurate interface information based on the Option 82 information.

[(Optional) Configuring IPsec on a DHCP Relay Agent](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcp_relay_cfg_0025.html)

To defend against certain network attacks, configure IPsec to authenticate messages between a DHCP relay agent and server.

[(Optional) Configuring CAR for Whitelisted DHCP Sessions](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcp_relay_cfg_0013.html)

You can configure an aging time and bandwidth parameters for CAR for whitelisted DHCP sessions to flexibly isolate the sessions.

[Verifying the Configuration of DHCP Relay](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dhcp_relay_cfg_0006.html)

After configuring a DHCP relay agent to transmit DHCP broadcast messages between DHCP clients and the DHCP server that reside on different network segments, verify the configuration.