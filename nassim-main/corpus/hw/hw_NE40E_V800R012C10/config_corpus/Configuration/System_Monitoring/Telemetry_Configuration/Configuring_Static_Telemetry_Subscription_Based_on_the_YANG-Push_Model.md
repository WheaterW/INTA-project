Configuring Static Telemetry Subscription Based on the YANG-Push Model
======================================================================

In static telemetry subscription based on the YANG-Push model defined by the IETF, a device functioning as a client initiates a connection to a collector functioning as a server in order to send the collected data.

#### Context

The controller uses commands to configure telemetry-capable devices, subscribe to data sources, and collect data. Only UDP can be used as the protocol for data reporting.

In static telemetry subscription mode, a device initiates a connection to a collector to send the collected data.

* If the connection is interrupted, the device connects to the collector and sends data again. However, the data sampled when the connection is being established again is lost.
* After an active/standby main control board switchover is performed or the device saves telemetry service configurations and restarts, the device reloads telemetry service configurations so that the service can run properly. However, the data sampled during the restart or switchover is lost.

If the device restarts or an active/standby main control board switchover occurs, the system is busy, and the CPU usage is high. In this case, you can configure static telemetry subscription for coarse-grained data collection to relieve device loads.


#### Pre-configuration Tasks

Before configuring static telemetry subscription, configure a static or dynamic routing protocol so that devices can communicate at the network layer.


[Configuring a Destination Collector](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_telemetry_cfg_00196.html)

When configuring a static telemetry subscription to the sampled data based on the YANG-Push model, you need to create a receiver for the sampled data.

[Configuring a Sampling Path](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_telemetry_cfg_00197.html)

When configuring a static telemetry subscription to the sampled data based on the YANG-Push model, you need to create a sampling filter and specify a sampling path.

[Creating a Subscription](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_telemetry_cfg_00198.html)

When configuring a static telemetry subscription to the sampled data based on the YANG-Push model, you need to create a subscription to associate the configured receiver with the configured sampling filter so that data can be sent to the sampling filter.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_telemetry_cfg_00199.html)

After configuring static telemetry subscription to the sampled data, you can check the sampling path information of a sensor.