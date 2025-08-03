Configuring a CPOS Interface
============================

Before you configure a channelized packet over SONET/SDH (CPOS) interface, familiarize yourself with the usage scenario and complete the pre-configuration tasks.

#### Usage Scenario

To use the SDH optical interface for packet data transmission and a low-speed interface for access, configure physical attributes and E1 channels for the corresponding CPOS interface.


#### Pre-configuration Tasks

Before configuring a CPOS interface, power on the device and ensure that it is working properly.


[Configuring the Working Mode of a CPOS Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cpos_cfg_0009.html)

A CPOS interface can work in either clear channel mode or channelized mode. Synchronous serial interfaces with different transmission rates can be generated in the two modes to meet different bandwidth requirements of services.

[Configuring the Clock Mode for a CPOS Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cpos_cfg_5001.html)

A CPOS interface works in either master clock mode or slave clock mode. You can configure the clock mode for a CPOS interface.

[Configuring the Working Modes for the E1 Channels of a CPOS Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cpos_cfg_0006.html)

This section describes how to configure the working modes for the E1 channels of a channelized packet over SONET/SDH (CPOS) interface. Here, SONET stands for synchronous optical network, and SDH stands for synchronous digital hierarchy.

[Configuring Overhead Bytes for a CPOS Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cpos_cfg_5003.html)

SDH provides a variety of overhead bytes. You can configure overhead bytes for CPOS interfaces to implement layered monitoring.

[Configuring the Mapping Mode for the E1 Channels of a CPOS Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cpos_cfg_5005.html)

CPOS interfaces support three E1 channel mapping modes: a-mode, h-mode, and l-mode.

[Configuring the Clock Mode for the E1 Channels of a CPOS Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cpos_cfg_5006.html)

An E1 channel works in either master clock mode or slave clock mode.

[Configuring the Frame Format for the E1 Channels of a CPOS Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cpos_cfg_5007.html)

E1 channels support the frame format with a 4-bit CRC code.

[Configuring the Loopback Function for the E1 Channels of a CPOS Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cpos_cfg_5008.html)

You can enable the loopback function on an interface to check whether the interface or the link works properly.

[Configuring the Loopback Function for a CPOS Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cpos_cfg_0007.html)

This section describes how to configure the loopback function on a channelized packet over SONET/SDH (CPOS) interface. Here, SONET stands for synchronous optical network, and SDH stands for synchronous digital hierarchy. The loopback function is used to check interface or cable status when devices are malfunctioning and must be disabled when devices are working properly.

[Verifying the CPOS Interface Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cpos_cfg_0008.html)

After you configure a channelized packet over SONET/SDH (CPOS) interface, you can check the clock mode, frame format, overhead byte, and administrative unit group (AUG) multiplexing path of the interface and the clock mode and frame format of its E1 channels. Here, SONET stands for synchronous optical network, and SDH stands for synchronous digital hierarchy.