Configuring Microburst Detection
================================

Configuring Microburst Detection

#### Context

Microbursts are short spikes in network traffic, typically lasting several milliseconds. During a microburst, the instantaneous data rate is tens or hundreds times higher than the average rate, and in some cases even exceeds the interface bandwidth. When a microburst exceeds the forwarding capability of a device, the device buffers the burst data for later transmission. If the device does not have sufficient available buffer, the excess data is discarded. This is known as packet loss due to congestion. Such issues cannot be effectively handled using traditional fault locating methods, which are complex and difficult. With such traditional methods, after packets are lost due to congestion in the outbound direction of an interface, outgoing packets are obtained to analyze the traffic trend and identify the characteristics of burst traffic. Microburst detection can be used to detect instantaneous (millisecond-level) burst traffic in the outbound direction of an interface, helping maintenance personnel determine whether packet loss is caused by microbursts. Microburst detection helps to identify potential congestion risks before congestion occurs and, if congestion does occur, quickly locate abnormal traffic.

The following microburst detection modes are supported:

* Default mode: Packets are sampled at an interval of 5 ms. In this mode, microburst detection can be enabled on multiple interfaces.
* Enhanced mode: Packets are sampled at an interval of 1 ms. In this mode, microburst detection can be enabled on only one interface.

The measurement period of microburst detection is 5 minutes. That is, the key performance indicators of interfaces are collected every 5 minutes and related entries are generated accordingly. The device can store statistics collected up to 300 minutes after microburst detection is enabled.

The key performance indicators of microburst detection are as follows:

* Average rate of burst traffic forwarded to an interface from any other interface on the same device
* Peak rate of burst traffic forwarded to an interface from any other interface on the same device
* Number of discarded packets on an interface
* Average buffer usage of an interface
* Peak buffer usage of an interface
* Buffer usage of interface queues when the interface buffer usage reaches the peak value in a measurement period

#### Procedure

* Configuring microburst detection on the device
  1. Enter the system view.
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure the microburst detection mode.
     ```
     [qos micro-burst detection](cmdqueryname=qos+micro-burst+detection+enable) [ enhanced ] enable
     ```
  3. Commit the configuration.
     ```
     [commit](cmdqueryname=commit)
     ```
* Configuring microburst detection on an interface
  1. Enter the system view.
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the interface view.
     ```
     [interface](cmdqueryname=interface) { interface-type interface-number | interface-name }
     ```
  3. Enable the microburst detection function on the interface.
     ```
     [qos micro-burst detection enable](cmdqueryname=qos+micro-burst+detection+enable)
     ```
  4. Commit the configuration.
     ```
     [commit](cmdqueryname=commit)
     ```