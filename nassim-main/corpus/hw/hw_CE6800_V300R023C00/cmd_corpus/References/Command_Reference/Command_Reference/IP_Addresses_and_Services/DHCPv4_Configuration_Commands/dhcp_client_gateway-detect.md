dhcp client gateway-detect
==========================

dhcp client gateway-detect

Function
--------



The **dhcp client gateway-detect** command enables gateway detection on a DHCP client.

The **undo dhcp client gateway-detect** command disables gateway detection on a DHCP client.



By default, gateway detection is disabled on a DHCP client.


Format
------

**dhcp client gateway-detect period** *period* **retransmit** *retransmit* **timeout** *timeout*

**undo dhcp client gateway-detect**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **period** *period* | Specifies an interval for gateway detection on a DHCP client. | The value is an integer that ranges from 1 to 86400 seconds. |
| **retransmit** *retransmit* | Specifies the retransmission count of gateway detection on a DHCP client. | The value is an integer ranging from 1 to 10. |
| **timeout** *timeout* | Specifies the timeout period of gateway detection on a DHCP client. | The value is an integer that ranges from 300 to 2000,the unit is milliseconds. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The dhcp client gateway-detect command applies to DHCP clients. After a DHCP client obtains an IP address, the dhcp client gateway-detect command enables the DHCP client to detect the status of the gateway being used. If the gateway has an incorrect address or the gateway device fails, the DHCP client requests a new IP address from the DHCP server.

**Precautions**

Gateway detection applies to dual-homed scenarios.


Example
-------

# Enable gateway detection on 100GE1/0/1 of the DHCP client. Set the detection interval to 3600s, retransmission count to 3, and timeout period to 500 ms.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] dhcp client gateway-detect period 3600 retransmit 3 timeout 500

```