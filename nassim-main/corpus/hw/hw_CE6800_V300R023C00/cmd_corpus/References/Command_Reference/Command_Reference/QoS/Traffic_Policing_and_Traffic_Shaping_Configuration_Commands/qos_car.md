qos car
=======

qos car

Function
--------



The **qos car** command creates a QoS CAR profile and sets parameters in the QoS CAR profile.

The **undo qos car** command deletes a QoS CAR profile.



By default, no QoS CAR profile is created.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**qos car** *car-name* { **percent** *percent-value* | **cir** *cir-value* [ **kbps** | **mbps** | **gbps** ] [ **cbs** *cbs-value* [ **bytes** | **kbytes** | **mbytes** ] [ **pbs** *pbs-value* [ **bytes** | **kbytes** | **mbytes** ] ] | **pir** *pir-value* [ **kbps** | **mbps** | **gbps** ] [ **cbs** *cbs-value* [ **bytes** | **kbytes** | **mbytes** ] **pbs** *pbs-value* [ **bytes** | **kbytes** | **mbytes** ] ] ] }

**undo qos car** *car-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *car-name* | Specifies the name of a QoS CAR profile. | The value is a string of 1 to 31 case-sensitive characters without spaces or question marks (?). It cannot be i, if, ifg, s, st, sta, stat, stati, statis, statist, statisti, statistic, or statistics. |
| **percent** *percent-value* | Specifies the percentage of the CIR to the interface bandwidth. | The value is an integer in the range from 1 to 100. |
| **cir** *cir-value* | Specifies the committed information rate (CIR), which is the average rate of traffic that can pass through an interface. | The value is an integer in the range of 24 to 400000000. The default unit is kbit/s. |
| **kbps** | Indicates that the rate unit is kbit/s. | - |
| **mbps** | Indicates that the rate unit is Mbit/s. | - |
| **gbps** | Indicates that the rate unit is Gbit/s. | - |
| **cbs** *cbs-value* | Specifies the committed burst size (CBS), which is the average volume of burst traffic that can pass through an interface. | The value is an integer. The value range differs depending on the CBS unit. The default unit is byte. Where:   * If the CBS is expressed in bytes, the value ranges from 10000 to 33554432. By default, the value of cbs-value is eight times the value of cir-value (kbit/s). * If the CBS is expressed in kbytes, the value ranges from 10 to 32768. By default, the value of cbs-value is eight times the value of cir-value (mbit/s). * If the CBS is expressed in mbytes, the value ranges from 1 to 32. By default, the value of cbs-value is eight times the value of cir-value (gbit/s). |
| **bytes** | Indicates that the CBS is expressed in bytes. | - |
| **kbytes** | Indicates that the CBS is expressed in Kbytes. | - |
| **mbytes** | Indicates that the CBS is expressed in Mbytes. | - |
| **pbs** *pbs-value* | Specifies the peak burst size (PBS), which is the maximum volume of burst traffic that can pass through an interface. | The value is an integer. The value range differs depending on the CBS unit. The default unit is byte. Where:   * If the CBS is expressed in bytes, the value ranges from 10000 to 33554432. If the PIR is not specified, the default PBS value is the CBS value. If the PIR is specified, the default PBS value is eight times the PIR value (kbit/s). * If the CBS is expressed in kbytes, the value ranges from 10 to 32768. If the PIR is not specified, the default PBS value is the CBS value. If the PIR is specified, the default PBS value is eight times the PIR value (mbit/s). * If the CBS is expressed in mbytes, the value ranges from 1 to 32. If the PIR is not specified, the default PBS value is the CBS value. If the PIR is specified, the default PBS value is eight times the PIR value (gbit/s). |
| **pir** *pir-value* | Specifies the peak information rate (PIR), which is the maximum rate of traffic that can pass through an interface. | The value is an integer in the range of 24 to 400000000. The default unit is kbit/s. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Traffic policing controls traffic. It monitors the traffic rate on the network and punishes the excess traffic to limit the incoming or outgoing traffic within a proper range and protect network resources.When data is transmitted from a high-speed link to a low-speed link, a bandwidth bottleneck occurs on the low-speed link interface, causing severe data loss. In this case, the rate of data traffic needs to be limited. Traffic policing can be performed in the outbound direction of a high-speed link interface to discard the packets whose rate exceeds the limit so that the rate of sent traffic is limited within the specified range. You can also configure traffic policing in the inbound direction of a low-speed link interface. When the rate of received packets is higher than the traffic policing rate, the device discards the packets.The packet color is determined by the cbs cbs-value and pbs pbs-value parameters in the **qos car** command.

* When the burst size of a packet is smaller than the CBS, the packet is colored green.
* When the burst size of a packet is greater than or equal to the CBS and less than the PBS, the packet is colored yellow.
* When the burst size of a packet is greater than or equal to the PBS, the packet is colored red.The QoS CAR profile created using this command can be applied to the following scenarios:
* The **car share** command is run in the traffic behavior view to perform traffic policing for a specified type of service traffic.
* The **qos car inbound** command is run in the interface view to perform traffic policing for all incoming packets on the interface.

**Precautions**

* If you specify percent percent-value when running the **qos car** command to create a QoS CAR profile, the QoS CAR profile can be applied only to physical interfaces.
* A maximum of 512 QoS CAR profiles can be created on the device.
* It is recommended that the CIR be greater than 2 Mbit/s.
* When the traffic policing rate exceeds the maximum rate of an interface, traffic policing is not performed on the interface. Set cir-value and pir-value to values smaller than the interface rate based on the actual interface rate.
* When the CBS is smaller than the number of bytes in a packet, packets of this type are discarded.
* To prevent packet color identification problems, you are advised to set the PBS to be greater than the CBS.


Example
-------

# Create a QoS CAR profile named qoscar1, and set the CIR to 10000 kbit/s and the CBS to 10240 bytes.
```
<HUAWEI> system-view
[~HUAWEI] qos car qoscar1 cir 10000 kbps cbs 10240 bytes

```