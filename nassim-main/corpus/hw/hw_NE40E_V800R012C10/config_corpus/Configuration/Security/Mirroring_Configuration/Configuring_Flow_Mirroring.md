Configuring Flow Mirroring
==========================

You can configure flow mirroring to copy the traffic of a specified type on the mirrored port to the observing port for analysis, thereby learning about the status of such traffic on the mirrored port.

#### Usage Scenario

If refined control is required for the packets sent to a packet analyzer, you can configure flow mirroring. In this manner, only the packets that meet specific conditions are copied and the other packets are filtered out, improving the efficiency of the analyzer.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Although you can configure an observing port, specify the observing port for board-based mirroring, and apply a traffic policy to a mirrored port in any sequence, you need to perform all these operations. Otherwise, flow mirroring cannot take effect. When the mirroring function is not required, you are advised to disable it so that it does not adversely affect other services.



#### Pre-configuration Tasks

Before configuring flow mirroring, complete the following task:

* Connect interfaces and configure physical parameters for them to ensure that their physical status is up.


[Configuring an Observing Port](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_portmirror_cfg_0005a.html)

An observing port is used to copy the traffic on a mirrored port to a packet analyzer. To prevent running services from being adversely affected, do not use the observing port as a service port.

[Specifying an Observing Port for Mirroring](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_portmirror_cfg_0030.html)

This section describes how to specify an observing port for mirroring. You can then associate this port with the corresponding mirrored port.

[Defining a Traffic Policy for Mirrored Traffic](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_portmirror_cfg_0021.html)

This section describes how to define a traffic policy for mirrored traffic. It covers configuring a traffic classifier to define the traffic to be mirrored, specifying a traffic behavior, enabling flow mirroring, and defining a traffic policy to associate the traffic classifier with the traffic behavior.

[Applying a Traffic Policy to a Mirrored Port](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_portmirror_cfg_0016.html)

A traffic policy must be applied to an interface for the configured traffic behavior to take effect when the traffic passing through the interface matches the specified traffic classification rule.

[(Optional) Configuring the Mirroring Statistics Function](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_portmirror_cfg_0033a.html)

You can enable mirroring statistics collection to check information about mirrored packets.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_portmirror_cfg_0017.html)

After configuring flow mirroring, you can check the traffic behavior, traffic classifier, traffic policy, and port mirroring configurations.

[Disabling Flow Mirroring](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_portmirror_cfg_0023.html)

When the flow mirroring function is not required, disable it so that it does not adversely affect user services.