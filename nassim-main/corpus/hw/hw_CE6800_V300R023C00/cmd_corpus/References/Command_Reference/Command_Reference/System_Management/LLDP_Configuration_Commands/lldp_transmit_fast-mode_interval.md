lldp transmit fast-mode interval
================================

lldp transmit fast-mode interval

Function
--------



The **lldp transmit fast-mode interval** command configures an interval for a device interface to send Link Layer Discovery Protocol (LLDP) packets.

The **undo lldp transmit fast-mode interval** command restores the default interval.



By default, the interval for a device interface to send LLDP packets is the same as the global interval for the device to send LLDP packets.


Format
------

**lldp transmit fast-mode interval** *packet-interval*

**undo lldp transmit fast-mode interval** [ *packet-interval* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *packet-interval* | Indicates packet Interval. | The value is an integer that ranges from 1 to 32768 . |



Views
-----

Layer 2 100GE interface view,100GE interface view,Layer 2 10GE interface view,10GE interface view,Layer 2 200GE interface view,200GE interface view,25GE-L2 view,25GE interface view,400GE-L2 view,400GE interface view,Layer 2 50GE interface view,50GE interface view,Layer 2 GE interface view,Interface group view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



When the LLDP status of a device remains unchanged or no new neighbor is discovered, the interface module periodically sends LLDP packets to its neighbors at a specified interval. By periodically exchanging LLDP packets with neighbors, a device can notify neighbors of its own status to ensure the accuracy and timely discovery of network topology and communication stability.To adjust the global frequency of network topology discovery, run the **lldp transmit interval** command to set a global interval for the device to send LLDP packets. Device interfaces may send LLDP packets at different intervals. If the network topology connected to an interface needs to be promptly discovered, run the lldp transmit fast-mode interval command to increase the LLDP packet exchange frequency.



**Prerequisites**



LLDP has been enabled globally using the lldp enable command in the system view.



**Configuration Impact**

Setpacket-interval to a proper value and adjust it based on the network load.

* The longer the interval, the lower the frequency of LLDP packets being exchanged. This saves system resources. However, if the interval for sending LLDP packets is too long, the device cannot notify neighbors of its status in a timely manner, reducing network topology discovery efficiency.
* The shorter the interval, the higher the frequency of LLDP packets being exchanged. This ensures prompt network topology discovery. However, if the interval is too short, LLDP packets are exchanged too frequently, increasing the system load and wasting resources.It is recommended that you use the default interval for sending LLDP packets.

**Precautions**

* The BY14packet-interval value is independent of the delay value.
* If the global interval and interface-specific interval are both configured, the interface-specific interval is preferred.


Example
-------

# Set the interval for sending LLDP packets to 2s.
```
<HUAWEI> system-view
[~HUAWEI] lldp enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] lldp transmit fast-mode interval 2

```