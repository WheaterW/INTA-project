Configuring a Serial Interface
==============================

Before you configure a serial interface, familiarize yourself
with the usage scenario and complete the pre-configuration tasks for the configuration.

#### Usage Scenario

If you want a serial interface
to carry upper-layer services, configure the link-layer attributes
of the serial interface and ensure that the status of the link-layer
protocol for the serial interface is Up.


#### Pre-configuration Tasks

Before configuring
link-layer attributes, create a serial interface.


[Configuring a Link Layer Protocol for a Serial Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_serial_cfg_0006.html)

This section describes how to configure a link-layer protocol for a serial interface. The link-layer protocol used by a serial interface determines the format of frames passing through this interface.

[Configuring the MTU for a Serial Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_serial_cfg_0007.html)

During MTU configuration for a serial interface, ensure that the MTUs of interfaces on directly connected devices are the same. Otherwise, services may be interrupted.

[Enabling the Payload Scramble Function on a Serial Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cfg_atm_0003_5.html)

To prevent communication failures caused by consecutive 0s or 1s on a link, enable the payload scramble function on a serial interface.

[Configuring the Length of the CRC Code for a Serial Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_serial_cfg_0001.html)

Serial interfaces support a 16- or 32-bit CRC code.

[Verifying the Serial Interface Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_serial_cfg_0008.html)

After you configure a serial interface, you can check the protocol type, link-layer protocol hold-timer, maximum transmission unit (MTU) the interface.