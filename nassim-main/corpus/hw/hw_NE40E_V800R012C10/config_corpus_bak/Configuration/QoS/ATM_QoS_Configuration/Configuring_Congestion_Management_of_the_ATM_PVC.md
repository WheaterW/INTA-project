Configuring Congestion Management of the ATM PVC
================================================

By configuring queues on ATM PVCs, you can schedule packets
into different queues based on a certain algorithm and discard excess
packets to implement congestion management.

#### Usage Scenario

On an ATM network, when the
traffic rate exceeds the threshold, the exceeding packets are buffered
instead of being discarded. When the network is not busy, the buffered
packets are forwarded. After the congestion management of ATM PVC
is configured, the packets are organized into queues according to
a specified algorithm. The packets then are forwarded according to
the queue scheduling mechanism.

The configuration of ATM PVC
queues involves the PQ configuration and the WFQ configuration.


#### Pre-configuration Tasks

Before configuring
the traffic shaping of the ATM PVC, complete the following task:

* Configuring the physical parameters of ATM interfaces to ensure
  normal operation of the interfaces
* Configuring IP addresses for the ATM interfaces
* Configuring a PVC
* Configuring the traffic shaping of the ATM PVC

#### Configuration Procedures

**Figure 1** Flowchart for Configuring Congestion Management of the ATM
PVC
  
![](images/fig_dc_ne_qos_cfg_01240001.png)


[Configuring the Queue Scheduling of an ATM PVC](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_012602.html)

When the network is congested, you can buffer the packets that exceed the PVC bandwidth and then send the packets out when the network becomes idle.

[Verifying the Configuration of Congestion Management of the ATM PVC](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_012603.html)

After congestion management is configured for ATM PVCs, you can view information about queues and packet statistics on ATM interfaces.