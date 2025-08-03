Configuring PRBS Testing
========================

This section describes how to configure user-side and network-side
PRBS testing.

#### Usage Scenario

PRBS testing is used to test
service connectivity between two devices. A PRBS testing-enabled NE40E sends a PRBS bit stream to a remote device that has remote
loopback enabled to perform a user-side test or to a remote device
that has local loopback enabled to perform a network-side test. After
the bit stream is looped back to NE40E, NE40E compares the bit stream with the one it previously sent
and calculates a bit error rate to determine the service connectivity.


#### Pre-configuration Tasks

* Before configuring user-side PRBS, ensure that remote loopback
  has been enabled on the remote device.
* Before configuring network-side PRBS, ensure that local loopback
  has been enabled on the remote device.

#### Configuration Procedures


[(Optional) Configuring UNI-Side PRBS Testing](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cfg_prbs_0005.html)

After configuring UNI-side PRBS testing, you can check the service connectivity on the UNI side in one-click mode, thereby determining whether the services between a PE and a CE are running properly.

[(Optional) Configuring Network-Side PRBS Testing](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cfg_prbs_0006.html)

After PRBS testing is enabled, you can perform a one-click test to check the service connectivity on the NNI side, that is, whether the PW between PEs is functioning properly.

[Verifying the PRBS Testing Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cfg_prbs_0007.html)

After configuring PRBS testing, verify the configuration.

[Example for Configuring a PRBS Test](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_prbs_cfg_0007.html)

This section provides an example on how to configure a PRBS test to check device connectivity when two devices are connected to each other through E1 interfaces.