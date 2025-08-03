Configuring Flow Mirroring Based on the Option 82 Information of User Packets
=============================================================================

This section describes how to configure flow mirroring based on the Option 82 information of user packets. This configuration enables a device to copy user packets carrying specified Option 82 information to the specified observing port for analysis. You can then determine the traffic status.

#### Usage Scenario

To analyze user traffic more precisely, you can configure the device to mirror user traffic based on Option 82 information and traffic classifier configuration. In this way, only the traffic that meets specified conditions is copied to the observing port for analysis. This helps filter out irrelevant user traffic, improving efficiency.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Although you can configure an observing port, specify the observing port for mirroring, and define a traffic policy for mirrored traffic as well as apply the policy globally in any sequence, you need to perform all these operations. Otherwise, flow mirroring cannot take effect. When the mirroring function is not required, you are advised to disable it so that it does not adversely affect other services.



#### Pre-configuration Tasks

Before configuring flow mirroring, complete the following task:

* Connect interfaces and configure physical parameters for them to ensure that their physical status is up.


[Configuring an Observing Port](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_portmirror_cfg_0005b.html)

An observing port is used to copy the traffic on a mirrored port to a packet analyzer. To prevent running services from being adversely affected, do not use the observing port as a service port.

[Specifying an Observing Port](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_portmirror_cfg_0030a.html)

This section describes how to specify an observing port for mirroring. You can then associate this port with the corresponding mirrored port.

[Defining a Traffic Policy for Mirrored Traffic and Applying It Globally](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_portmirror_cfg_0031.html)

This section describes how to define a traffic policy for mirrored traffic and apply the policy globally. It covers configuring a traffic classifier to define the traffic to be mirrored, specifying a traffic behavior, enabling flow mirroring, defining a traffic policy to associate the traffic classifier with the traffic behavior, and applying the traffic policy globally.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_portmirror_cfg_0032.html)

After configuring flow mirroring, you can check the traffic behavior, traffic classifier, traffic policy, and port mirroring configurations.

[Disabling Flow Mirroring](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_portmirror_cfg_0023a.html)

When the flow mirroring function is not required, disable it so that it does not adversely affect user services.