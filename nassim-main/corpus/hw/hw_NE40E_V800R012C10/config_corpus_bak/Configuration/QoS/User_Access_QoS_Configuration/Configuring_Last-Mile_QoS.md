Configuring Last-Mile QoS
=========================

Last-mile QoS indicates QoS applied to the link between a user and a DSLAM. The device can adjust downstream traffic based on the link layer protocol running between the user and the DSLAM. This prevents network congestion when the volume of DSLAM traffic exceeds the actual capability of the link.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In VS mode, this feature is supported only by the admin VS.



[Overview of Last-Mile QoS](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_023803.html)

This section introduces concepts and principle of last-mile QoS.

[Configuring Last-Mile QoS](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_023806.html)

When implementing traffic shaping, the device uses last-mile QoS to deduct excessive link costs, such as the ATM cell header or Ethernet frame header. This helps prevent the congestion when the downstream traffic exceeds the line capacity of the DSLAM.