FlexE Interface Configuration
=============================

FlexE interfaces refer to FlexE clients, which correspond to various externally observed user interfaces on networks. Each FlexE client can be flexibly allocated bandwidth from a group resource pool, and the bandwidth can be adjusted. In VS mode, this feature is supported only by the admin VS.

#### Usage Scenario

The need for higher mobile bearer bandwidth is increasing as 5G networks continue to evolve. In addition, customers want a unified network to transmit various services, such as home broadband, leased line access, and mobile bearer services. These factors place increasingly higher requirements on telecommunication network interfaces. FlexE isolates services by isolating the bandwidth resources of interfaces. FlexE interfaces are isolated from each other so that traffic is isolated at the physical layer and network slicing is performed for services on the same physical network.

FlexE applies to the access, aggregation, and core layers. As 5G services transition through the initial, development, and maturity phases, the service volume increases gradually. FlexE allows the bearer network to be smoothly upgraded.


#### Pre-configuration Tasks

Before configuring FlexE interfaces, complete the following tasks:

* Power on the device and ensure that it passes the self-check.
* Install a FlexE-capable board on the device.
* Activate the FlexE interface license on the board.


[Activating the FlexE Interface License on a Board](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ifm_cfg_8005.html)

To configure FlexE services on a board, you must activate the FlexE interface license on the board first.

[Configuring a Standard Ethernet Interface to Work in FlexE Mode](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ifm_cfg_8006.html)

The bandwidth of a standard Ethernet interface is fixed. To flexibly specify the bandwidth of an interface, you need to switch its working mode from standard Ethernet to FlexE.

[Configuring a PHY Number for a FlexE Physical Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ifm_cfg_8007.html)

To ensure normal communication between interconnected devices, you need to configure the same PHY number for the FlexE physical interfaces on both of them.

[Creating a FlexE Group and Binding a FlexE Physical Interface to It](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ifm_cfg_8008.html)

After a FlexE group is created, you can bind a group of FlexE physical interfaces to it, flexibly allocating bandwidth to FlexE clients based on the sub-timeslot granularity.

[Configuring a Number for a FlexE Group](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ifm_cfg_8009.html)

To ensure normal communication between interconnected devices, you need to configure the same group number for the FlexE groups to which the FlexE physical interfaces on both devices are added.

[(Optional) Configuring a Sub-timeslot Granularity for a FlexE Card](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ifm_cfg_8010.html)

The sub-timeslot granularity of a FlexE card restricts the bandwidth configuration of a FlexE client. By default, the sub-timeslot granularity of a FlexE card is 5 Gbit/s.

[(Optional) Configuring a Mode for a FlexE Card](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ifm_cfg_8011.html)

FlexE cards support timeslot and bandwidth modes. The bandwidth mode is recommended.

[Creating a FlexE Client and Configuring an ID and Bandwidth for It](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ifm_cfg_8012.html)

FlexE clients correspond to externally observed user interfaces. Each FlexE client can be flexibly allocated bandwidth from a group resource pool, and the bandwidth can be adjusted.

[Adding a FlexE NE in an Ethernet Service Scenario](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ifm_cfg_8013.html)

Adding a FlexE NE to a live network running Ethernet services involves the connection between a FlexE physical interface and standard Ethernet interface. If DCN auto-negotiation is enabled on the FlexE physical interface, the two interfaces can automatically communicate with each other, and the NMS can manage the FlexE NE.

[Adding a FlexE or Ethernet NE in a FlexE Service Scenario](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ifm_cfg_8014.html)

Adding an Ethernet NE to a live network running FlexE services involves the connection between a FlexE physical interface and standard Ethernet interface. If DCN auto-negotiation is enabled on the FlexE physical interface, the two interfaces can automatically communicate with each other, and the NMS can manage the FlexE NE.

[(Optional) Configuring a Time Synchronization Mode for a FlexE Physical Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ifm_cfg_8015.html)

The FlexE standards define two 1588v2 message transmission modes: Overhead (OH) and Client. By default, 1588v2 messages are transmitted in OH mode.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ifm_cfg_8016.html)

After configuring a FlexE interface, verify the configuration.