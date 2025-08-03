Understanding Static Subscription
=================================

Understanding Static Subscription

#### Definition

In static telemetry subscription, a device functioning as a client initiates a connection to a collector functioning as a server in order to report sampled data.


#### Fundamentals

You can use commands to configure telemetry-capable devices by subscribing to data sources in order to collect data. gRPC and UDP can be used to send data to the collector.

If the connection between a device and the collector is interrupted, the device reconnects to the collector and resends the data. However, any data sampled while the connection is being re-established is lost.

After an active/standby switchover is performed, or when the system restarts after saving the telemetry service configuration, the device reloads the telemetry service configuration so that the service can run properly. However, the data sampled during the restart or active/standby switchover is lost. As this poses high pressure requirements on devices, telemetry static subscription is often used for coarse-grained data collection.