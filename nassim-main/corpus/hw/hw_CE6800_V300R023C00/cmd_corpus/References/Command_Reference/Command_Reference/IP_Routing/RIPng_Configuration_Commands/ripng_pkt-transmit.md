ripng pkt-transmit
==================

ripng pkt-transmit

Function
--------



The **ripng pkt-transmit** command sets the interval for sending Update packets and the number of packets sent each time on the specified interface.

The **undo ripng pkt-transmit** command restores the default setting.



By default, the interval for sending Update packets is 200 ms and the number of packets sent each time is 30 on the RIPng interface.


Format
------

**ripng pkt-transmit** { **interval** *interval* | **number** *packet-count* } \*

**undo ripng pkt-transmit**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interval** *interval* | Specifies the interval for sending packets. | The value is an integer ranging from 50 to 500 milliseconds. |
| **number** *packet-count* | Indicates the number of packets sent each time. | The value is an integer ranging from 25 to 100. |



Views
-----

100GE interface view,10GE sub-interface view,10GE interface view,1200ge sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,Tunnel interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Running the **ripng pkt-transmit** command in the interface view as required can accurately control the interval for sending packets and the number of sent packets. RIPng performance is therefore improved.NOTE:The command can take effect only after IPv6 is enabled for the interface by the **ipv6 enable** command.


Example
-------

# On 100GE 1/0/1, set the interval for sending packets to 100 milliseconds and the number of packets sent each time to 50.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ripng pkt-transmit interval 100 number 50

```