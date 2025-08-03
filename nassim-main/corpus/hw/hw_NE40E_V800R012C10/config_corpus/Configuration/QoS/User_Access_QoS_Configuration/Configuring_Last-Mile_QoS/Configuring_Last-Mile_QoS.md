Configuring Last-Mile QoS
=========================

When implementing traffic shaping, the device uses last-mile QoS to deduct excessive link costs, such as the ATM cell header or Ethernet frame header. This helps prevent the congestion when the downstream traffic exceeds the line capacity of the DSLAM.

#### Context

When the NE40E functions as a BRAS, you can configure last-mile QoS for it so that the NE40E can perform QoS shaping more accurately by deducting excessive link costs, such as the ATM cell header or Ethernet frame header. This helps prevent the congestion when the downstream traffic of the NE40E exceeds the line capacity of the DSLAM.

The NE40E allows you to configure last-mile QoS in the interface or AAA domain view. The configuration in the AAA domain view takes effect for only the L2TP service. When last-mile QoS is configured in both the AAA domain view and the interface view, only the configuration in the AAA domain view takes effect.


#### Pre-configuration Tasks

Before configuring last-mile QoS, complete the following task:

* Configure the BRAS functions on the NE40E to allow users to go online.


[Enabling Last-Mile QoS](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_013848.html)

You must enable last-mile QoS before configuring it.

[Configuring the Last-Mile QoS Mode and Setting the Adjustment Value of the Size of Remote Packets](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_023809.html)

The device can adjust the link bandwidth based on the types of links between the user and DSLAM.

[(Optional) Enabling the Upstream CAR Function and Statistics Function for Layer 3 Packets](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_023811.html)

You can implement CAR and the statistics function for Layer 3 packets to adjust the link bandwidth.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_023831.html)

After configuring last-mile QoS, verify the configuration.