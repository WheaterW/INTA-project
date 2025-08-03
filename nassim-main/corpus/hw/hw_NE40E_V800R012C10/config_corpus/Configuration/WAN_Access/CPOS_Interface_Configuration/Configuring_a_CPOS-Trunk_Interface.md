Configuring a CPOS-Trunk Interface
==================================

Configuring a CPOS-Trunk interface includes creating a
CPOS-Trunk interface, adding a CPOS interface to the CPOS-Trunk interface,
and creating a trunk serial interface on the CPOS-Trunk interface.

#### Usage Scenario

A CPOS-Trunk interface is
a logical interface that has all the functions of a CPOS interface.
It is more reliable because it has multiple CPOS interfaces bundled
using the link aggregation technology.

After a CPOS-Trunk interface
is created, APS can be configured on the interface.


#### Pre-configuration Tasks

Before configuring
a CPOS-Trunk interface, power on the device and ensure that the self-check
succeeds.


[Creating a CPOS-Trunk Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cpos-trunk_cfg_0002.html)

This section describes how to create a CPOS-Trunk interface and add a CPOS member interface to the CPOS-Trunk interface.

[Configuring the Working Mode of a CPOS-Trunk Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cpos-trunk_cfg_0006.html)



[Configuring a Working Mode for an E1 Channel of a CPOS-Trunk Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cpos-trunk_cfg_0003.html)

An E1 channel of a CPOS-Trunk interface can be configured to work in clear channel or channelized mode to form trunk serial interfaces with different bandwidths.

[Creating a Global-MP-Group and Adding a Trunk Serial Interface to It](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cpos-trunk_cfg_0005.html)

To increase transmission bandwidth and improve network reliability, add trunk serial interfaces to a global MP-group interface.

[Creating a Global-IMA-Group and Adding a Trunk Serial Interface to It](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cpos-trunk_cfg_0007.html)

To increase transmission bandwidth and improve network reliability, add trunk serial interfaces to a global IMA-group interface.

[Verifying the CPOS-Trunk Interface Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cpos-trunk_cfg_0004.html)

After configuring a CPOS-Trunk interface, check the configurations and status of the CPOS-Trunk interface.