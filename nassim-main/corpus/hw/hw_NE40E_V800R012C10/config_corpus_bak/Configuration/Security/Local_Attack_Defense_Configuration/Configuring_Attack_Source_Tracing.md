Configuring Attack Source Tracing
=================================

After being configured with attack source tracing, the Router saves received attack packets to its memory for attack analysis and defense.

#### Usage Scenario

When being attacked, the Router enabled with attack source tracing can save attack packets to its memory for attack analysis and defense. The attack source tracing module checks whether packet loss occurs at an interval of 1 minute. If packet loss is detected, the attack source tracing module records information about the attack packets in the memory.

In VS mode, this feature is supported only by the admin VS.


#### Pre-configuration Tasks

Before configuring attack source tracing, configure the parameters of the link layer protocol and IP addresses for interfaces and ensure that the link layer protocol on the interfaces is Up.


[Creating an Attack Defense Policy](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_sysattack_cfg_0005.html)

All local attack defense features must be added to an attack defense policy. These features take effect after the attack defense policy is applied to the interface board.

[Enabling Attack Source Tracing](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_sysattack_cfg_0006.html)

If attack source tracing is manually disabled, you need do as follows to enable it.

[Configuring Sampling Parameters for Attack Source Tracing](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_sysattack_cfg_0007.html)

You can do as follows to change the value of sampling parameters.

[Applying the Attack Defense Policy](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_sysattack_cfg_0009.html)

The configured attack defense policy takes effect only after being applied to the interface board.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_sysattack_cfg_0010.html)

After configuring attack source tracing, you can check detailed information about packets discarded by each functional module, including packet receiving interfaces, associated VLANs, and packet discarding time.