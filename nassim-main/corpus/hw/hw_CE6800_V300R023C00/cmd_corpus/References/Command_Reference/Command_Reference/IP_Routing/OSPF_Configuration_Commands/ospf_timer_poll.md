ospf timer poll
===============

ospf timer poll

Function
--------



The **ospf timer poll** command sets the poll interval at which Hello packets are sent on an NBMA network.

The **undo ospf timer poll** command restores the default value.



The default interval is 120 seconds.


Format
------

**ospf timer poll** *interval*

**undo ospf timer poll**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies a poll interval. | The value is an integer ranging from 1 to 3600, in seconds. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On an NBMA network, if a neighbor is invalid, the device sends Hello packets to the neighbor at the poll interval set using the ospf timer poll command. The poll interval must be at least 4 times the Hello interval.

**Precautions**

The command cannot be run on a null interface.


Example
-------

# Set the poll interval at which Hello packets are sent on an interface to 130 seconds.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/7
[~HUAWEI-100GE1/0/7] undo portswitch
[*HUAWEI-100GE1/0/7] ospf timer poll 130

```