Configuring a POS Interface
===========================

You can configure the link layer protocol, clock mode,
overhead byte, frame format, and CRC for a POS interface.

#### Usage Scenario

Before using a POS interface
to carry packets, configure parameters for the POS interface.


#### Pre-configuration Tasks

* Before configuring a POS interface, power on the Router and ensure that it is working properly.

#### Configuration Procedure

By
default, parameters in POS interface configuration commands use default
values. Perform one or more of the following configurations as required.


[Configuring the Link Layer Protocol for a POS Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_pos_cfg_2004.html)



[Configuring the Clock Mode for a POS Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_pos_cfg_2005.html)

A POS interface works in either master or slave clock mode. You can configure different clock modes for POS interfaces that function as a DTE or DCE.

[Configuring Overhead Bytes for a POS Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_pos_cfg_2006.html)

SONET/SDH provides a variety of overhead bytes to implement monitoring at different levels.

[Configuring the Frame Format for a POS Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_pos_cfg_2007.html)

The frame format of a POS interface determines the application mode of the interface. POS interfaces support two frame formats: SDH and SONET.

[Configuring the Scrambling Function for a POS Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_pos_cfg_2008.html)

POS interfaces support the scrambling function for the payload data to avoid excessive consecutive 1s or 0s, which helps the receiver extract line clock signals.

[Configuring the Length of the CRC Code for a POS Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_pos_cfg_2009.html)

POS interfaces support a 16- or 32-bit CRC code.

[Configuring the MTU for a POS Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_pos_cfg_2010.html)

The MTU is used to reassemble or fragment packets on a POS interface when packets are received or sent on the interface through the IP network protocol.

[Configuring the Loopback Function for a POS Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_pos_cfg_2015.html)

Loopback is enabled on an interface only when some special function tests need to be carried out.

[Verifying the POS Interface Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_pos_cfg_2011.html)

After configuring a POS interface, verify the configuration.