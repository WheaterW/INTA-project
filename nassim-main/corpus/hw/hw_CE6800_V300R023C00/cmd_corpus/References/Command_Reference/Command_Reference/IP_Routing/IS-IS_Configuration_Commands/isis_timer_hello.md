isis timer hello
================

isis timer hello

Function
--------



The **isis timer hello** command sets an interval for a broadcast interface to send Hello packets of a corresponding level.

The **undo isis timer hello** command restores the default value.



By default, the interval at which Hello packets are sent is 10 seconds.


Format
------

**isis timer hello** *hello-interval* [ **conservative** ]

**undo isis timer hello** [ *hello-interval* ]

**undo isis timer hello** *hello-interval* **conservative**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *hello-interval* | Specifies the interval at which Hello packets are sent on an interface. | The value is an integer ranging from 1 to 255, in seconds. |
| **conservative** | Enables the conservative mode for the IS-IS neighbor hold time.   * If this parameter is specified and the holdtime of an IS-IS neighbor relationship is less than 20, the IS-IS neighbor relationship is disconnected without a delay after the holdtime expires. * If this parameter is not specified and the holdtime of an IS-IS neighbor relationship is less than 20, the holdtime is delayed to 20 seconds after the holdtime expires. After the holdtime expires, the neighbor relationship is disconnected. | - |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a broadcast link, Level-1 and Level-2 Hello packets are sent separately, and the intervals at which they are sent need to be set respectively. On a P2P link, neither level-1 nor level-2 is required because there is only one type of Hello packets. The shorter the interval, the more system resources used to send Hello packets. The interval should therefore be set as required.

**Precautions**

You are not advised to set a short interval for sending IS-IS packets. Otherwise, protocol flapping may occur when the system is busy. The default interval is recommended.


Example
-------

# Set the interval at which Level-2 Hello packets are sent to 20 seconds on a specified interface.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] isis enable 1
[*HUAWEI-100GE1/0/1] isis timer hello 20 level-2

```