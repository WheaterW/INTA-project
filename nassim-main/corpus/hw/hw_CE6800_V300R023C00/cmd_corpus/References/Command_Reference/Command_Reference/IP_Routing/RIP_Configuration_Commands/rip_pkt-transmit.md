rip pkt-transmit
================

rip pkt-transmit

Function
--------



The **rip pkt-transmit** command sets the interval at which update packets are sent by a specified interface and the number of packets sent each time.

The **undo rip pkt-transmit** command restores the default setting.



By default, interval, pkt-count, and bandwidth-value are 200 milliseconds, 50, and 99, respectively.


Format
------

**rip pkt-transmit** { **interval** *interval* | **number** *pkt-count* | **bandwidth** *bandwidth-value* } \*

**undo rip pkt-transmit**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interval** *interval* | Specifies the interval for sending packets. | The value is an integer ranging from 50 to 500 milliseconds. |
| **number** *pkt-count* | Indicates the number of packets sent each time. | The value is an integer ranging from 25 to 100. |
| **bandwidth** *bandwidth-value* | Specifies the percentage of the bandwidth for sending RIP packets to the total bandwidth. | The value is an integer that ranges from 1 to 99. |



Views
-----

100GE interface view,10GE sub-interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To configure the interval at which update packets are sent and the number of packets sent each time, run the rip pkt-transmit command, which improves RIP performance.


Example
-------

# Set the interval at which packets are sent by 100GE 1/0/1 to 100 milliseconds and the number of packets sent each time to 60.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] rip pkt-transmit interval 100 number 60

```