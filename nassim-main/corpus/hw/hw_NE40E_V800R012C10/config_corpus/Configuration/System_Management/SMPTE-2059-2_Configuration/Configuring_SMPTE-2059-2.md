Configuring SMPTE-2059-2
========================

This section describes how to configure SMPTE-2059-2. An SMPTE-2059-2 network typically uses the best master clock algorithm (BMCA) to dynamically establish the master-slave hierarchy. For different types of devices on an SMPTE-2059-2, the corresponding functions need to be configured.

#### Usage Scenario

The first step of establishing an SMPTE-2059-2 network is to import time signals from an external BITS clock source. The BMCA can be used to select the grandmaster clock and master clock from SMPTE-2059-2 devices. Alternatively, the grandmaster clock and master clock can be manually configured. On a dynamic SMPTE-2059-2 network, clock source selection is implemented by comparing priorities to ensure the precision of clock signals to the maximum extent.


#### Pre-configuration Tasks

* Set physical parameters of interfaces so that the interfaces are physically Up.


[Importing Time Signals from an External BITS Source](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_smpte-2059-2_cfg_005.html)

On an SMPTE-2059-2 network, time signals are typically imported from an external building integrated timing supply system (BITS) source. Multiple Routers can be configured to import time signals from an external BITS source before the grandmaster clock is determined.

[Configuring Clock Source Attributes for Dynamic BMCA Selection](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_smpte-2059-2_cfg_006.html)

After multiple SMPTE-2059-2 devices are configured with time signal input, clock source attributes can be configured on these devices to allow them to participate in BMCA selection. The local clock of an SMPTE-2059-2 device can also participate in BMCA selection. The BMCA helps SMPTE-2059-2 devices dynamically determine the grandmaster clock which provides time signals for the entire SMPTE-2059-2 network. SMPTE-2059-2 devices can obtain time synchronization information from the grandmaster clock through the SMPTE-2059-2 protocol.

[Enabling SMPTE-2059-2 Globally](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_smpte-2059-2_cfg_0013.html)

This section describes how to enable SMPTE-2059-2 globally. SMPTE-2059-2 needs to be enabled in both the system view and interface view. After SMPTE-2059-2 is enabled in the system view, you need to configure basic device information, such as the domain value, required for setup of an SMPTE-2059-2 network.

[Enabling SMPTE-2059-2 on an Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_smpte-2059-2_cfg_008_a.html)

This section describes how to enable SMPTE-2059-2 on an interface. SMPTE-2059-2 needs to be enabled in both the system view and interface view. After being globally enabled in the system view, SMPTE-2059-2 also needs to be enabled on an interface.

[(Optional) Configuring Time Attributes for SMPTE-2059-2 Packets](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_smpte-2059-2_cfg_009.html)

This section describes how to configure time attributes for SMPTE-2059-2 packets. SMPTE-2059-2 nodes exchange Announce, Sync, and Delay or Pdelay packets to send time information and maintain SMPTE-2059-2 connections. You can set the interval at which an SMPTE-2059-2 interface sends Announce, Sync, and Delay or Pdelay packets and the maximum number of Announce packet timeouts. Using the default time attribute values is recommended.

[(Optional) Configuring an SMPTE-2059-2 Packet Encapsulation Mode](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_smpte-2059-2_cfg_010.html)

This section describes how to configure an SMPTE-2059-2 packet encapsulation mode. SMPTE-2059-2 packets can be encapsulated into Layer 3 packets for transmission. Select the encapsulation type based on networking environments and configure the source and destination IP addresses and transmission priority.

[Verifying the SMPTE-2059-2 Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_smpte-2059-2_cfg_012.html)

After configuring SMPTE-2059-2 functions, verify the configuration.