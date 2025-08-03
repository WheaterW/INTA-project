Configuring an Ethernet Interface on an Interface Board
=======================================================

You can configure parameters for Ethernet interfaces on interface boards to ensure that physical connections work properly between devices.

#### Usage Scenario

You need to configure parameters for an Ethernet interface before using the interface to transmit packets on an Ethernet.

All parameters for an Ethernet interface have default values, except the IP address. Any change to an Ethernet interface on a local device must be the same as that on the peer device.


#### Pre-configuration Tasks

None


#### Ethernet Interface Attributes

Ethernet interfaces on the HUAWEI NE40E-M2 series-M2 support different configurations, as listed in [Table 1](#EN-US_TASK_0172362802__tab_dc_vrp_ethernet_cfg_000202). Configure supported features according to interfaces.

**Table 1** Ethernet interface attributes
| Ethernet Interface Attribute | Ethernet Electrical Interface | Ethernet Optical Interface | 10GE WAN Interface | 10GE LAN/WAN Interface | 25GE Interface | 400GE Interface | 40GE Interface | 50GE Interface | 50|100GE Interface |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MTU configuration for an Ethernet interface:  [**mtu**](cmdqueryname=mtu) *mtu* or [**ipv6 mtu**](cmdqueryname=ipv6+mtu) *mtu* | Supported | Supported | Supported | Supported | Supported | Supported | Supported | Not supported | Not supported |
| Duplex mode configuration for an Ethernet interface:  [**duplex**](cmdqueryname=duplex+full+half+auto) { **full** | **half** | **auto** } | Supported | Not supported (the default full-duplex mode is supported) | Not supported | Not supported | Not supported | Not supported | Not supported | Not supported | Not supported |
| Rate configuration for an Ethernet electrical interface:  [**speed**](cmdqueryname=speed+10+100+1000+auto) { **10** | **100** | **1000** | **auto** } | Supported | Supported | Not supported | Not supported | Not supported | Not supported | Not supported | Not supported | Not supported |
| Negotiation mode configuration for an Ethernet interface:  [**negotiation auto**](cmdqueryname=negotiation+auto) | Supported | Supported | Supported only when the interfaces at both ends support the GE rate. The configuration takes effect only in the GE interface view. | Supported only when the interfaces at both ends support the GE rate. The configuration takes effect only in the GE interface view. | Supported | Not supported | Not supported | Not supported | Not supported |
| Flow control configuration for a GE interface:  [**flow control**](cmdqueryname=flow+control+receive+send) [ **receive** | **send** ] | Supported | Supported | Supported | Supported | Supported | Supported | Supported | Supported | Supported |
| Overhead byte configuration for a 10GE WAN interface:  [**flag**](cmdqueryname=flag) | Not supported | Not supported | Supported | Supported by WAN interfaces instead of LAN interfaces | Not supported | Not supported | Not supported | Not supported | Not supported |



[Setting the Maximum Frame Length Allowed by an Ethernet Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ethernet_cfg_2010.html)

Jumbo frames are designed for gigabit Ethernet networks. They are giant frames and their lengths vary according to vendors. To enable devices that transmit different lengths of jumbo frames to communicate successfully, adjust the maximum frame length allowed by either the local or peer Ethernet interface.

[Configuring the MTU for an Ethernet Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ethernet_cfg_2002.html)

MTU is the largest packet of data that can be transmitted on a network, expressed in bytes. MTU is determined by data link layer protocols, and MTU values vary with networks. A proper MTU is a prerequisite for normal communication between network devices.

[Configuring a Working Mode for an Ethernet Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ethernet_cfg_2003.html)

An Ethernet interface works in either half-duplex or full-duplex mode at the physical layer of an Ethernet network. To ensure communication between devices, configure a proper duplex mode for an Ethernet interface.

[Configuring the Working Rate for an Ethernet Electrical Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ethernet_cfg_2004.html)

The volume of traffic that can be transmitted on an Ethernet electrical interface is determined by the working rate of the interface. To ensure communication between devices, set a proper working rate for Ethernet electrical interfaces.

[Configuring the Optical or Electrical Mode for a GE Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ethernet_cfg_2005.html)

In most cases, the system recognizes the interface module and therefore automatically sets the optical or electrical mode of an interface. If the system fails to recognize the interface module, configure the optical or electrical mode for an interface.

[Configuring the LAN/WAN Transmission Mode for a 10GE Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ethernet_cfg_2015.html)

A 10G XFP multi-mode optical transceiver works in either LAN or WAN mode. You can configure a proper mode as required.

[Configuring the LAN or OTN Transmission Mode for a 10GE or 100GE Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ethernet_cfg_2020.html)

If the transmission modes of the interfaces at both ends of a link are different, the link goes down. To ensure reliable communication, set the same transmission mode (either LAN or OTN) for the interfaces at both ends of a link. If the VS mode is used, this configuration task is supported only by the admin VS.

[Configuring an Overhead Byte for a 10GE WAN Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ethernet_cfg_2006.html)

SONET/SDH provides a variety of overhead bytes to implement monitoring at different levels.

[Enabling Flow Control on a GE Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ethernet_cfg_2014.html)

To prevent traffic congestion between a local device and its peer device, configure flow control on GE interfaces of both devices to control the rates at which the GE interfaces send and receive packets.

[Configuring Self-Loop Detection on the GE Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ethernet_cfg_5001.html)

After the self-loop detection function is enabled, the self-loop on an interface can be detected and then the interface is blocked.

[Enabling the Statistics Collection Function on a Sub-interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ethernet_cfg_0019.html)

After enabling the statistics collection function on a sub-interface, you can view the statistics about the received or sent packets on the sub-interface.

[Configuring the Hold-Time Interval Before an Interface Goes Up/Down](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ethernet_cfg_2001.html)

When an interface frequently alternates between up and down, flapping may occur. To prevent the problem, you can configure the hold-time interval before an interface goes up or down. If the VS mode is used, this configuration is supported only by the admin VS.

[Configuring the IPG](../../../../software/nev8r10_vrpv8r16/user/ne/dc_pnf_ethernet_cfg_2001.html)



[Configuring an Alarm Threshold for Sudden Traffic Rate Decrease on an Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ethernet_cfg_2031.html)

To allow a device to detect real-time traffic rate changes on an interface, you can configure the device to generate an alarm when the traffic rate change (%) on the interface exceeds a specified threshold (*ratio-threshold*) while the bandwidth usage (%) is not below the set lower threshold (*bandwidth-usage-threshold*). Traffic rate change on an interface (%) = (Interface rate in the current traffic statistics collection interval â Interface rate in the previous traffic statistics collection interval)/Interface rate in the previous traffic statistics collection interval

[Disabling an Ethernet Interface or Sub-interface from Broadcasting Packets](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ethernet_cfg_0021.html)

To protect a device against attacks from broadcast packets and improve network security, disable the Ethernet interfaces or sub-interfaces on the device from broadcasting packets.

[(Optional) Setting a Bandwidth Mode for an Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ethernet_cfg_2018.html)

Whether the bandwidth can be set to 1 Gbit/s/10 Gbit/s/25 Gbit/s depends on a device's hardware conditions.

[(Optional) Configuring an Optical Module for a Port](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ethernet_cfg_2019.html)



[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ethernet_cfg_2008.html)

After an Ethernet interface is successfully configured, you can view information about the interface's IP address, MTU, working rate, working mode, type, and statistics about packets sent and received.