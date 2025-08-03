Understanding Dynamic Subscription
==================================

Understanding Dynamic Subscription

#### Definition

In dynamic telemetry subscription, a collector functioning as a client initiates a connection to a device functioning as a server to collect data.


#### Fundamentals

To implement dynamic subscription, you must enable the gRPC service (the protocol used to report data) and configure the source IP address and port number to be listened.

If the connection between the device and collector is interrupted, the device automatically cancels the subscription and stops data sampling and reporting. The configuration cannot be restored unless the collector resends a connection establishment request. For example, if you want to monitor an interface for a period of time, configure dynamic telemetry subscription. To stop monitoring, tear down the connection. The subscription is then automatically canceled and cannot be restored. This mitigates loads on devices and simplifies the interaction between you and devices.