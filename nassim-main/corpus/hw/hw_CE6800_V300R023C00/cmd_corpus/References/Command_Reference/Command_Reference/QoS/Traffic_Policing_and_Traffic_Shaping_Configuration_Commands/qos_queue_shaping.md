qos queue shaping
=================

qos queue shaping

Function
--------



The **qos queue shaping** command enables traffic shaping for a queue on a specified interface and sets traffic shaping parameters.

The **undo qos queue shaping** command restores the default scheduling parameters of each queue on an interface.



The following table describes the default scheduling parameters on an interface.


Format
------

**qos queue** *queue-index* **shaping** { **percent** **cir** *cir-percent-value* [ **pir** *pir-percent-value* ] | **cir** *cir-value* [ **kbps** | **mbps** | **gbps** ] [ **cbs** *cbs-value* [ **bytes** | **kbytes** | **mbytes** ] | **pir** *pir-value* [ **kbps** | **mbps** | **gbps** ] [ **cbs** *cbs-value* [ **bytes** | **kbytes** | **mbytes** ] **pbs** *pbs-value* [ **bytes** | **kbytes** | **mbytes** ] ] ] }

**undo qos queue** *queue-index* **shaping**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *queue-index* | Specifies the queue index. | The value is an integer ranging from 0 to 7. |
| **percent** | Specify the QoS queue shaping percent. | - |
| **cir** *cir-value* | Specifies the absolute value of the committed information rate (CIR). | The value is an integer that ranges from 1 to 400000000. |
| **cir** *cir-percent-value* | Specifies the percentage value of the CIR. | The value is an integer that ranges from 1 to 100. The default value is 100.  The CBS is calculated as follows: CBS = cir-percent-value x Maximum bandwidth of an interface x 8 |
| **pir** *pir-percent-value* | Specifies the percentage value of the PIR. | The value is an integer that ranges from 1 to 100. The default value is 100, which is the same as cir-percent-value.  The PBS is calculated as follows: PBS = pir-percent-value x Maximum bandwidth of an interface x 8 |
| **pir** *pir-value* | Specifies the absolute value of the peak information rate (PIR). | The value is an integer that ranges from 1 to 400000000. |
| **kbps** | Indicates that the rate unit is kbit/s. | - |
| **mbps** | Indicates that the rate unit is Mbit/s. | - |
| **gbps** | Indicates that the rate unit is Gbit/s. | - |
| **cbs** *cbs-value* | Specifies the absolute value of the committed burst size (CBS), which is the volume of committed burst traffic that can pass through an interface. | For the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer that ranges from 1 to 8388608.  For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S:The value is an integer that ranges from 1 to 33554432. |
| **bytes** | Indicates that the CBS is expressed in bytes. | - |
| **kbytes** | Indicates that the CBS is expressed in Kbytes. | - |
| **pbs** *pbs-value* | Specifies the absolute value of the peak burst size (PBS), which is the maximum volume of burst traffic that can pass through an interface. | For the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer that ranges from 1 to 8388608.  For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S:The value is an integer that ranges from 1 to 33554432. |
| **mbytes** | Indicates that the CBS is expressed in Mbytes. | - |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When the traffic rate of an interface on a downstream device is lower than that of the connected interface on the upstream device, traffic congestion may occur on the interface of the downstream device. You can configure traffic shaping for queues on the outbound interface of the upstream device and adjust the transmit rate of the interface.The **qos queue shaping** command configures traffic shaping on packets of a specific service on an interface.

**Prerequisites**

Priority mapping based on simple traffic classification has been configured to map packet priorities to PHBs and colors, or internal priority re-marking based on complex traffic classification has been configured so that packets of different services enter different queues.

**Precautions**

If traffic shaping is configured both on an interface queue and an interface (using the **qos lr** command), the CIR of the interface cannot be lower than the sum of CIR values of all the queues on the interface; otherwise, traffic shaping result may be incorrect. For example, the queue with a lower priority may occupy the bandwidth of the queue with a higher priority.If you run the **qos queue shaping** command multiple times on the same interface, only the latest configuration takes effect.


Example
-------

# Set absolute values of the CIR and PIR for queue 4 on the 100GE1/0/1 to 10000 kbit/s and 20000 kbit/s, respectively.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] qos queue 4 shaping cir 10000 kbps pir 20000 kbps

```

# Set percentage values of the CIR and PIR for queue 4 on the 100GE1/0/1 to 50% and 80%, respectively.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] qos queue 4 shaping percent cir 50 pir 80

```