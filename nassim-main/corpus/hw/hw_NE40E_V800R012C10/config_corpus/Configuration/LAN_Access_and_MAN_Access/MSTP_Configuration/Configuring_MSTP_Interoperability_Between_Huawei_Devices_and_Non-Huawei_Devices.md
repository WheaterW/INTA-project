Configuring MSTP Interoperability Between Huawei Devices and Non-Huawei Devices
===============================================================================

To enable Huawei devices to interwork with non-Huawei devices, configure proper parameters and functions, including the Bridge Protocol Data Unit (BPDU) format, Multiple Spanning Tree Protocol (MSTP) protocol packet format, and digest snooping function, on the Huawei devices running MSTP.

#### Applicable Environment

On a Multiple Spanning Tree Protocol (MSTP) network, inconsistent protocol packet formats and BPDU keys may lead to a communication failure. Configuring proper MSTP parameters on Huawei devices ensures interoperability between Huawei devices and non-Huawei devices.


#### Pre-configuration Tasks

Before configuring MSTP interoperability between Huawei devices and non-Huawei devices, complete the following task:

* Configuring basic MSTP functions


[Configuring a Proposal/Agreement Mechanism](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mstp_cfg_0037.html)

To enable Huawei Datacom devices to communicate with non-Huawei devices, configure a proper rapid transition mechanism on Huawei devices according to the Proposal/Agreement mechanism on non-Huawei devices.

[Configuring the MSTP Protocol Packet Format on an Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mstp_cfg_0038.html)

MSTP protocol packets can be transmitted in auto, dot1s, or legacy mode.

[Enabling the Digest Snooping Function](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mstp_cfg_0040.html)

When a Huawei device is connected to a non-Huawei device, if the region names, revision numbers, and VLAN-to-instance mappings configured on the two devices are consistent but the Bridge Protocol Data Unit (BPDU) keys are different, the two devices cannot communicate. To address this problem, enable the digest snooping function on the Huawei device.

[(Optional) Configuring an Interface to Transparently Transmit HVRP Packets](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_mstp_cfg_0001_a.html)



[Verifying the MSTP Interoperability Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mstp_cfg_0041.html)

After Multiple Spanning Tree Protocol (MSTP) parameters are configured for the interoperability between Huawei devices and non-Huawei devices, verify the configuration.