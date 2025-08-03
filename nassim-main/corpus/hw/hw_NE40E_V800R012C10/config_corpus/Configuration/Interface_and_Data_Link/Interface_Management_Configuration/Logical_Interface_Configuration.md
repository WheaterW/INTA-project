Logical Interface Configuration
===============================

This section describes how to configure logical interfaces. Logical interfaces are manually configured interfaces, which are used to exchange data. Logical interfaces do not exist physically.

#### Usage Scenario

For usage scenarios of logical interfaces, see "Logical Interface" in *NE40E Feature Description > Interface Management*.

**Table 1** Logical interface list
| Feature | Interface Name | Configuration Guide |
| --- | --- | --- |
| System management | DCN serial interface | This interface is automatically created by the system. |
| Interface management | Virtual Ethernet (VE) interface | [Creating an L2VE Interface](../ne/dc_ne_l2-l3_cfg_5001.html)  [Creating an L3VE Interface](../ne/dc_ne_l2-l3_cfg_5002.html) |
| Interface management | Global VE interface | [Creating a Global VE Interface](dc_vrp_ifm_cfg_70001.html) |
| Interface management | Loopback interface | [Creating a Loopback Interface and Configuring Its IP Address](dc_vrp_ifm_cfg_0015.html) |
| Interface management | Null0 interface | [Entering the NULL Interface View](dc_vrp_ifm_cfg_0016.html) |
| LAN access and MAN access | Ethernet sub-interface | [Configuring Ethernet Sub-interfaces to Support Communication Between VLANs](dc_vrp_ethernet_cfg_0007.html) |
| LAN access and MAN access | Eth-Trunk interface | [Eth-Trunk Interface Configuration](dc_vrp_ethtrunk_cfg_0000.html) |
| LAN access and MAN access | VLANIF interface | [Configuring Layer 3 Communication Between VLANIF Interfaces](dc_vrp_vlan_cfg_0010.html) |
| WAN access | ATM bundle interface | [(Optional) Configuring an AC Interface to Transparently Transmitting TDM Frames/ATM Cells](dc_vrp_vpws_cfg_6006.html) |
| WAN access | IP-Trunk interface | [Configuring an IP-Trunk Interface](dc_vrp_hdlc_ip-trunk_cfg_0008.html) |
| WAN access | POS-Trunk interface | [Configuring a POS-Trunk interface](../ne/dc_vrp_pos_cfg_0001.html) |
| WAN access | CPOS-Trunk interface | [Creating a CPOS-Trunk Interface](dc_vrp_cpos-trunk_cfg_0002.html) |
| WAN access | MP-group interface | [Configuring MP](../ne/dc_ne_mp_cfg_0001.html) |
| WAN access | Global MP-group interface | [Creating a Global-MP-Group and Adding a Trunk Serial Interface to It](dc_vrp_cpos-trunk_cfg_0005.html) |
| WAN access | IMA-group interface | [ATM IMA Configuration](dc_vrp_atm_cfg_0001.html) |
| WAN access | Global IMA-group interface | [Creating a Global-IMA-Group and Adding a Trunk Serial Interface to It](dc_vrp_cpos-trunk_cfg_0007.html) |
| MPLS | Tunnel interface | [MPLS TE Configuration](dc_vrp_te-p2p_cfg_0000.html) |

#### Pre-configuration Tasks

Before configuring logical interfaces, connect interfaces and set their physical parameters to ensure that these interfaces are physically up.



[Creating a Global-VE interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ifm_cfg_70001.html)

Global-VE interfaces are independent of boards. You can create Global-VE interfaces only if the Router is powered on.

[Configuring a Channelized Sub-interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ifm_cfg_7011_01.html)

This section describes how to configure a channelized sub-interface.

[Creating a Loopback Interface and Configuring an IP Address for It](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ifm_cfg_0015.html)

IP addresses need to be configured for loopback interfaces that are always up so that these interfaces can be used to communicate with other devices.

[Entering the NULL Interface View](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ifm_cfg_0016.html)

The system automatically creates a NULL0 interface. The NULL interface is used for preventing routing loops and filtering traffic.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ifm_cfg_0017.html)

After the configuration is completed on the Global-VE interface, FlexE interface license, FlexE interface, loopback interface, and Null interface, check the configurations.