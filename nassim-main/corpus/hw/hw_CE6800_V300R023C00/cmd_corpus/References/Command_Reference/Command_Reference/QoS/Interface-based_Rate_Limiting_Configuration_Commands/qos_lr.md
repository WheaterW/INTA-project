qos lr
======

qos lr

Function
--------



The **qos lr** command sets the traffic shaping rate to limit the rate of data packets sent by an interface.

The **undo qos lr** command cancels the traffic shaping rate.



By default, the traffic shaping rate is the maximum bandwidth of an interface.


Format
------

For CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6885-LL (low latency mode):

**undo qos lr** [ **outbound** ]

For CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K:

**qos lr cir** *cir-value* [ **kbps** | **mbps** | **gbps** ] [ **cbs** *cbs-value* [ **bytes** | **kbytes** | **mbytes** ] ] [ **outbound** ]

For CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode):

**qos lr cir** *cir-value* [ **kbps** | **mbps** | **gbps** ] [ **outbound** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **kbps** | Indicates that the rate unit is kbit/s. | - |
| **mbps** | Indicates that the rate unit is Mbit/s. | - |
| **gbps** | Indicates that the rate unit is Gbit/s. | - |
| **cbs** *cbs-value* | Specifies the committed burst size (CBS).  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S: The value is an integer. The value range differs depending on the CBS unit. The default unit is byte. Where:   * If the CBS is expressed in bytes, the value ranges from 10000 to 33554432. By default, the value of cbs-value is eight times the value of cir-value (kbit/s). * If the CBS is expressed in kbytes, the value ranges from 10 to 32768. By default, the value of cbs-value is eight times the value of cir-value (mbit/s). * If the CBS is expressed in mbytes, the value ranges from 1 to 32. By default, the value of cbs-value is eight times the value of cir-value (gbit/s). |
| **bytes** | Indicates that the CBS is expressed in bytes.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S. | - |
| **kbytes** | Indicates that the CBS is expressed in Kbytes.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S. | - |
| **outbound** | Limits the rate of outgoing packets. | - |
| **cir** *cir-value* | Specifies the committed information rate (CIR). | The value is an integer that ranges from 1 to 400000000. |
| **mbytes** | Indicates that the CBS is expressed in Mbytes.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S. | - |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When a large amount of data flows are sent from the upstream device to its downstream device, to prevent congestion or packet loss, run the **qos lr** command to configure traffic shaping on the outbound interface of the device to limit the traffic and burst traffic transmitted over a connection so that packets are sent at an even rate.Similar to traffic policing, traffic shaping limits the traffic rate. When traffic policing is used, the system directly discards the packets whose rate is larger than the traffic shaping rate. Traffic shaping, however, buffers the packets whose rate is larger than the traffic shaping rate. When there are sufficient tokens in the token bucket, the device forwards buffered packets at an even rate. Traffic shaping increases the delay, whereas traffic policing does not.

**Precautions**

* This command applies only to the outbound direction on an interface.
* When the traffic rate in the outbound direction of an interface is larger than the alarm threshold for the rate limit in the outbound direction of an interface, an alarm is generated.
* If you need to set the same traffic shaping rate on multiple interfaces, you can perform the configuration on a port group to reduce the workload.
* If both traffic shaping and queue shaping (configured by using the **qos queue shaping** command) are configured on an interface, the CIR of traffic shaping cannot be lower than the sum of CIR values of all the queues on the interface; otherwise, the traffic shaping result may be incorrect. For example, the queue with a lower priority may occupy the bandwidth of the queue with a higher priority.
* Traffic shaping increases the delay because it uses the buffer mechanism.
* If you run the **qos lr** command multiple times on the same interface, only the latest configuration takes effect.

Example
-------

# Set the CIR of data traffic sent by 100GE1/0/1 to 20000 kbit/s.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] qos lr cir 20000 kbps
[*HUAWEI-100GE1/0/1] quit

```