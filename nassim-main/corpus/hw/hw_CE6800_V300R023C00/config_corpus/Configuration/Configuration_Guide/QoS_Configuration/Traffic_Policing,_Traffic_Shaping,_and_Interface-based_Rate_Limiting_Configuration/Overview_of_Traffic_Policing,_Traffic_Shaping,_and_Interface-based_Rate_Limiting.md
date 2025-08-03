Overview of Traffic Policing, Traffic Shaping, and Interface-based Rate Limiting
================================================================================

Overview of Traffic Policing, Traffic Shaping, and Interface-based Rate Limiting

#### Definition

Traffic policing, traffic shaping, and interface-based rate limiting monitor and control traffic rates and resource usage.

* Traffic policing: monitors the rate of traffic entering a network and discards excess traffic to ensure the incoming traffic rate remains within a specified range, conserving network resources.
* Traffic shaping: adjusts the rate at which traffic is sent to reduce traffic bursts, thereby ensuring a stable transmission rate and preventing congestion on the downstream device.
* Interface-based rate limiting: controls the rate at which packets are sent or received on an interface. This mechanism is useful for limiting the rate of all traffic on an interface, regardless of packet types.

#### Purpose

Network congestion may occur when the transmit rate on an upstream device is higher than the receive rate on a downstream device or when the interface rate on a downstream device is lower than the interface rate on an upstream device. If users are allowed to send traffic at an unlimited rate, continuous traffic bursts from many users may result in a congested network. Therefore, user traffic must be rate-limited to ensure services remain stable even in scenarios where network resources are limited. As such, traffic policing, traffic shaping, and interface-based rate limiting can be used to control the traffic rate to improve network resource utilization and service stability.