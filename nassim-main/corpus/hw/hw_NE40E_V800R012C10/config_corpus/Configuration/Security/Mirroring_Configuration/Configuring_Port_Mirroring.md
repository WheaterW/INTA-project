Configuring Port Mirroring
==========================

Port mirroring enables a device to copy the traffic on a specified port (mirrored port) to an observing port for analysis, so that you can determine the traffic status of the mirrored port.

#### Usage Scenario

Port mirroring applies to scenarios where you want to observe and analyze the traffic status of a port on the network device directly connected to a Router. In such scenarios, you can configure port mirroring for the Router to mirror the traffic of that port to a dedicated packet analyzer for analysis, thereby avoiding complicated analysis on the port.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

You can configure port mirroring in either of the following ways:

* [Configure port mirroring in integrated mode](dc_ne_portmirror_cfg_0035.html).
* Configure [an observing port](dc_ne_portmirror_cfg_0005.html) and [a mirrored port](dc_ne_portmirror_cfg_0025.html), and [specify the observing port for mirroring](dc_ne_portmirror_cfg_0026.html).
  
  Although you can configure an observing port, configure a mirrored port, and specify the observing port for mirroring in any sequence, you need to perform all these operations. Otherwise, port mirroring cannot take effect. When the mirroring function is not required, you are advised to disable it so that it does not adversely affect other services.


#### Pre-configuration Tasks

Before configuring port mirroring, complete the following task:

* Connect interfaces and configure physical parameters for them to ensure that their physical status is up.


[Configuring an Observing Port](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_portmirror_cfg_0005.html)

An observing port is used to copy the traffic on a mirrored port to a packet analyzer. To prevent running services from being adversely affected, do not use the observing port as a service port.

[Configuring a Mirrored Port](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_portmirror_cfg_0025.html)

To analyze the traffic sent or received by an interface, you can configure this interface as a mirrored port.

[Specifying an Observing Port for Mirroring](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_portmirror_cfg_0026.html)

This section describes how to specify an observing port for mirroring. You can then associate this port with the corresponding mirrored port.

[Configuring Port Mirroring in Integrated Mode](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_portmirror_cfg_0035.html)



[(Optional) Configuring the CAR Function for Mirrored Traffic](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_portmirror_cfg_0024.html)

This section describes how to configure the committed access rate (CAR) function for mirrored traffic. This function helps prevent a large volume of mirrored traffic from affecting packet processing.

[(Optional) Configuring the Function to Mirror Packet Content of a Specified Length](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_portmirror_cfg_0038.html)

You can specify the length of packet content to be mirrored. This configuration reduces the bandwidth consumed by the observing port and improves service performance.

[(Optional) Enabling Mirroring Statistics Collection](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_portmirror_cfg_0033.html)

You can enable mirroring statistics collection to check information about mirrored packets.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_portmirror_cfg_0008.html)

After configuring port mirroring, you can view the configuration of the mirrored port and observing port.

[Disabling Port Mirroring](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_portmirror_cfg_0022.html)

When the port mirroring function is not required, disable it so that it does not adversely affect user services.