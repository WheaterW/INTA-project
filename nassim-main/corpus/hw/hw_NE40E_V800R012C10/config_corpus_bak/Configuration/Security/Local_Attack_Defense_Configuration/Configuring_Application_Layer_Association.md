Configuring Application Layer Association
=========================================

This section describes how to configure association between
the application layer and lower layers.

#### Usage Scenario

There are various application
protocols on the Router, but not all of them are used in actual networking. To save CPU
resources and defend against attacks, unnecessary application protocol
packets are not sent to the CPU for processing.

To save Router resources, you can configure application layer association to have
only packets of the enabled protocol be sent to the CPU for processing.
The packets of the disabled protocol are sent to the CPU at a minimum
bandwidth by default.

When application layer association and
protocols are enabled, packets are sent to the CPU at the default
bandwidth; when application layer association is enabled but protocols
are disabled, packets are sent to the CPU at a minimum bandwidth or
simply dropped. When application layer association is disabled, protocols
are not associated. In this case, packets are sent to the CPU at the
default bandwidth regardless of whether the protocols are enabled.

In VS mode, this feature is supported only by the
admin VS.


#### Pre-configuration Tasks

Before configuring
application layer association, configure parameters of the link layer
protocol and IP addresses for interfaces and ensure that the link
layer protocol on the interfaces is Up.


[Creating an Attack Defense Policy](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_sysattack_cfg_0005c.html)

All local attack defense features must be added to an attack defense policy. These features take effect after the attack defense policy is applied to the interface board.

[Setting the Mode of Processing the Packets Sent to the CPU](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_sysattack_cfg_0030.html)

This section describes the default mode of handling protocol packets when association between the application layer and lower layers is enabled whereas no upper layer protocol is enabled.

[Applying the Attack Defense Policy](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_sysattack_cfg_0009c.html)

The configured attack defense policy takes effect only after being applied to the interface board.

[Verifying the Application Layer Association Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_sysattack_cfg_0032.html)