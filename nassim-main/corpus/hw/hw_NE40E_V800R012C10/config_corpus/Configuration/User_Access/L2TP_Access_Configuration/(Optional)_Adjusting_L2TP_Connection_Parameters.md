(Optional) Adjusting L2TP Connection Parameters
===============================================

By adjusting L2TP connection parameters, you can flexibly control L2TP tunnel establishment and the interconnection between Huawei devices and non-Huawei devices.

#### Usage Scenario

Optional L2TP connection configurations include AVP hidden in transmission, hello interval, control packet retransmission, and idle-cut timer of a tunnel.

These configurations can be used when an NE40E functions as a LAC, an LNS, or an LTS. In most cases, default configurations can be used without the need of any change.


#### Pre-configuration Tasks

Before adjusting an L2TP connection, [enable L2TP](dc_ne_l2tp_cfg_013687.html).


[Configuring AVP Attributes of L2TP Packets](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_l2tp_cfg_013497.html)

The control messages used to connect tunnels contain multiple AVP attributes. You can configure the AVP attributes of packets to adjust L2TP connections.

[Configuring an Interval for Sending Hello Packets](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_l2tp_cfg_013498.html)

A LAC and an LNS exchange Hello packets to detect tunnel connectivity.

[Configuring Control Packet Retransmission](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_l2tp_cfg_013499.html)

After control packet retransmission is enabled, if a device on one end of a tunnel does not receive any response packet from its peer for a specified number of times within a certain period, the device considers that the tunnel is torn down.

[Configuring an Idle-Cut Timer for a Tunnel](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_l2tp_cfg_013500.html)

To save bandwidth resources, you can set an idle-cut timer.

[Configuring a Default Invalid VLAN ID in the Calling-Station-Id Attribute](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_l2tp_cfg_013501.html)

To ensure interconnection between a Huawei device and a non-Huawei device, you can configure a default invalid VLAN ID in the Calling-Station-Id attribute for the Huawei device.

[Verifying the L2TP Connection Parameter Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_l2tp_cfg_013502.html)

After adjusting an L2TP connection, you can verify the L2TP group configuration on the devices at both ends of an L2TP connection.