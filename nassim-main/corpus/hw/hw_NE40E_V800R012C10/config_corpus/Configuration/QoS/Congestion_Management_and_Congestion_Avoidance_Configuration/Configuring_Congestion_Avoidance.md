Configuring Congestion Avoidance
================================

Using WRED, you can set thresholds for random packet discard. This can avoid the situation in which the rates of multiple TCP connections are lowered at the same time, thus avoiding TCP global synchronization.

#### Usage Scenario

Due to limited memory resources, when network congestion occurs, the traditional processing method is tail drop. That is, all the excess packets are discarded. When a large number of TCP packets are discarded, TCP connections will time out. As a result, TCP slow start and congestion avoidance are triggered so as to reduce the forwarding of packets by TCP. When the packets of several TCP connections are discarded at the same time, slow start and congestion avoidance of the TCP connections occur simultaneously, leading to what is called the global TCP synchronization. Thus, these TCP connections simultaneously send fewer packets to the queue so that the rate of incoming packets is lower than the rate of outgoing packets, reducing the bandwidth usage.

To avoid global TCP synchronization, you can set queues to discard packets randomly by using the WRED mechanism. Random packet discarding of WRED can prevent multiple TCP connections from reducing their transmit rates at the same time, thus avoiding global TCP synchronization. In addition, the bandwidth can be efficiently utilized.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

WRED is usually used together with WFQ.



#### Pre-configuration Tasks

Before configuring WRED, complete the following tasks:

* Configuring the physical parameters of interfaces
* Configuring the link layer attributes of interfaces to ensure their normal operation
* Configuring IP addresses for interfaces
* Enabling the routing protocol for communication between devices


[Configuring WRED Profiles](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cmca-qos_cfg_0012.html)

You can configure the lower drop threshold, upper drop threshold, and drop probability for packets of different colors in WRED profiles.

[(Optional) Configuring Share-Shaping for Port Queues](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cmca-qos_cfg_0013.html)

When the outbound interfaces of port queues with different priorities are the same main interface, you can perform share-shaping for the port queues using the same scheduling mode.

[Applying WRED](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cmca-qos_cfg_0014.html)

You can apply the configured WRED profile based on the service type.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_cmca-qos_cfg_0015.html)

After WRED is configured, verify the configuration.