Configuring Basic IGMP Functions
================================

To implement communication between user hosts and a multicast network, configure basic IGMP functions on interfaces that connect multicast devices to user network segments.

#### Usage Scenario

IGMP runs on the network segments that connect Routers to user hosts and must be configured on both Routers and user hosts. This section describes how to configure IGMP on a Router.

* Before configuring IGMP, enable IP multicast routing, which is the prerequisite for configuring any other multicast functions. When IP multicast routing is disabled, all multicast-related configurations will be deleted.
* Configure an IGMP version on a Router's interface that connects to user hosts before you perform other IGMP configurations on the Router. A Router interface's IGMP version is backward compatible with a user host's IGMP version. Therefore, a Router interface's IGMP version must be the same as or later than its connected user hosts' IGMP versions.
* You can adjust IGMP querier control parameters based on actual network conditions or whether hosts can quickly respond.
* To determine whether to send IGMP messages to upper-layer protocols for processing, configure the Router-Alert option. IGMP message transmit and receive ends must have the same Router-Alert option configuration on the same network segment. If the two ends do not have the same Router-Alert option configuration, change the configuration on one end.

#### Pre-configuration Tasks

Before configuring basic IGMP functions, complete the following tasks:

* Configure link layer protocol parameters and IP addresses for interfaces to ensure that the link layer protocol status of the interfaces is Up.
* Configure a unicast routing protocol to ensure that unicast routes are reachable.


[Enabling Multicast Routing](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2180a.html)

Enable multicast routing on a Router before you configure other multicast features on the Router.

[Enabling IGMP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2045.html)

To enable an interface to process user join requests, enable IGMP on the interface.

[(Optional) Setting an IGMP Version](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2046.html)

Interfaces that connect multicast devices to the same user network segment must run the same IGMP version. Otherwise, these multicast devices fail to communicate.

[(Optional) Configuring IGMP Querier Control Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2252.html)

IGMP querier control parameters include the interval at which General Query messages are sent, robustness variable, maximum response time of Query messages, keepalive time of other IGMP queriers, and interval at which IGMP last-member query messages are sent.

[(Optional) Configuring the Router-Alert Option for IGMP Messages](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2253.html)

You can configure a device to deny IGMP messages that do not contain the Router-Alert option and the device to send IGMP messages that do not contain the Router-Alert option. The two configurations are usually used together.

[Verifying the Basic IGMP Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_multicast_cfg_2049.html)

After configuring basic IGMP functions, verify the IGMP configuration, IGMP operating status, and information about IGMP group members.