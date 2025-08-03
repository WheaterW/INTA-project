Configuring Bit-Error-Triggered IGP Route Switching
===================================================

This section describes how to configure bit-error-triggered IGP route switching.

#### Usage Scenario

After bit-error-triggered IGP route switching is configured, if bit errors are generated on an interface, the link quality level of the interface changes to Low, triggering an IGP (OSPF or IS-IS) to increase the cost of the interface's link. IGP routes then do not preferentially select the link with bit errors. You can set different values for the bit error alarm and alarm clear thresholds. For example, to prevent jitters, set the alarm clear threshold to be one order of magnitude lower than the bit error alarm threshold. Bit-error-triggered IGP route switching ensures that the link with a lower BER is used to transmit traffic, minimizing the impact of bit errors on services.


#### Pre-configuration Tasks

Before configuring bit-error-triggered IGP route switching, complete the following tasks based on a used IGP:

* Enable BFD globally.
* [Configure basic IPv4 IS-IS functions.](dc_vrp_isis_cfg_1000.html)
* [Configure basic OSPF functions.](dc_vrp_ospf_cfg_0003.html)


[Configuring an IPv4 IS-IS Interface to Automatically Adjust the Link Cost](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_error-code_000020-1.html)

Configuring an IS-IS interface to automatically adjust the link cost based on link quality facilitates route selection control and improves network reliability.

[Configuring an IPv6 IS-IS Interface to Automatically Adjust the Link Cost](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_isis_cfg_1054_copy.html)

Configuring an IPv6 IS-IS interface to automatically adjust the link cost based on link quality facilitates route selection control and improves network reliability.

[Configuring an OSPF Interface to Automatically Adjust the Link Cost](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_error-code_000020-2.html)

Configuring an OSPF interface to automatically adjust the link cost based on link quality facilitates route selection control and improves network reliability.

[Configuring an OSPFv3 Interface to Automatically Adjust the Link Cost](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_3000_copy.html)

Configuring an OSPFv3 interface to automatically adjust the link cost based on link quality facilitates route selection control and improves network reliability.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_cfg_error-code_000021.html)

After configuring bit-error-triggered IGP route switching, verify the configurations.