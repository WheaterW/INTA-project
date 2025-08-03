Configuring Static Telemetry Subscription Based on the OpenConfig-Telemetry Model
=================================================================================

In static telemetry subscription based on the OpenConfig-Telemetry model defined by OpenConfig, a device functioning as a client initiates a connection to a collector functioning as a server in order to send the collected data.

#### Context

The controller uses commands to configure telemetry-capable devices, subscribe to data sources, and collect data. The protocol used to send data can be gRPC or UDP.

In static telemetry subscription mode, a device initiates a connection to a collector to send the collected data.

* If the connection is interrupted, the device connects to the collector and sends data again. However, the data sampled when the connection is being established again is lost.
* After an active/standby main control board switchover is performed or the device saves telemetry service configurations and restarts, the device reloads telemetry service configurations so that the service can run properly. However, the data sampled during the restart or switchover is lost.

If the device restarts or an active/standby main control board switchover occurs, the system is busy, and the CPU usage is high. In this case, you can configure static telemetry subscription for coarse-grained data collection to relieve device loads.


#### Pre-configuration Tasks

Before configuring static telemetry subscription, configure a static or dynamic routing protocol so that devices can communicate at the network layer.


[Configuring gRPC-based Static Telemetry Subscription](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_telemetry_cfg_00186.html)

Telemetry supports static subscription in gRPC dial-out mode.

[Configuring UDP-based Static Telemetry Subscription](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_telemetry_cfg_00190.html)

Telemetry supports static subscription in UDP mode.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_telemetry_cfg_00194.html)

After configuring static telemetry subscription to the sampled data or a customized event, check information about the sampling sensor group, destination group, and subscription.