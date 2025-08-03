Applying a Basic ACL6
=====================

Basic ACL6s can be used in device management, QoS services, multicast packet filtering, and routing policies.

#### Context

[Table 1](#EN-US_TASK_0172365063__tab_dc_vrp_acl6_cfg_005201) describes the typical applications of basic ACL6s.

**Table 1** Typical applications of basic ACL6s
| Typical Application | Usage Scenario | Operation |
| --- | --- | --- |
| Device management | When a device functions as a TFTP server, configure a basic ACL6 to allow only the clients that match specific ACL6 rules to access the server. | For details on how to configure rights to access a TFTP server, see [Configuring TFTP Access Authority](dc_vrp_basic_cfg_0090.html). |
| Multicast packet filtering | To filter multicast packets, you can configure a basic ACL6 to receive or forward only the multicast packets that match the ACL6 rules. | For details on how to filter multicast packets, see  * [Setting a Multicast Source Address Range](dc_vrp_multicast_cfg_2011.html) * [Setting the Range of Valid C-RP Addresses](dc_vrp_multicast_cfg_2018.html) * [Setting a Valid BSR Address Range](dc_vrp_multicast_cfg_2020.html) * [Setting an SSM Group Address Range](dc_vrp_multicast_cfg_2024.html) |
| Routing policies | To control the reception and advertisement of routing information on a device, configure a basic ACL6 on the device to allow the device to receive or advertise only the routes that match the ACL6 rules. | For details on how to control the reception and advertisement of routing information on a device, see  * [Configuring OSPFv3 to Filter Received Routes](dc_vrp_ospfv3_cfg_2028.html) * [Configuring OSPFv3 to Filter the Routes to Be Advertised](dc_vrp_ospfv3_cfg_2029.html) * [Filtering IPv6 IS-IS Routes](dc_vrp_isis_cfg_1032.html) * [Configuring IPv6 IS-IS to Import External Routes](dc_vrp_isis_cfg_1038.html) * [Configuring a Policy for Receiving BGP4+ Routes](dc_vrp_bgp6_cfg_0031.html) * [Configuring a Policy for Advertising BGP4+ Routes](dc_vrp_bgp6_cfg_0030.html) |
| QoS services | To process different types of traffic, configure a basic ACL6 to perform traffic policing, traffic shaping, or traffic classification on traffic that matches the ACL6 rules. | For details on how to process different types of traffic, see Configuring the Traffic Policing Policy, Configuring Traffic Shaping, and Configuring Traffic Behaviors. |