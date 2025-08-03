stp vlan timer forward-delay
============================

stp vlan timer forward-delay

Function
--------



The **stp vlan timer forward-delay** command sets the value of the Forward Delay of a device.

The **undo stp vlan timer forward-delay** command restores the default value of the Forward Delay.



By default, the value of the Forward Delay of a device is 1500 centiseconds (15 seconds).


Format
------

**stp vlan** *vlan-id* [ **to** *vlan-id* ] [ *vlan-id* [ **to** *vlan-id* ] ] &<1-9> **timer** **forward-delay** *time-value*

**undo stp vlan** *vlan-id* [ **to** *vlan-id* ] [ *vlan-id* [ **to** *vlan-id* ] ] &<1-9> **timer** **forward-delay** [ *time-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **to** *vlan-id* | Specifies one or more VLANs in which the Forward Delay value is set. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| *time-value* | Specifies the value of the Forward Delay. | The value is an integer that ranges from 400 to 3000, in centiseconds, and the step is 100. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a network running a spanning tree algorithm, if the network topology is changed, it takes time to advertise new BPDU configuration messages on the network. During this period, interfaces to be blocked may not be blocked in time and interface ever blocked may not be blocked. As a result, a temporary loop may be formed. To prevent this problem, you can use the Forward Delay timer to set a delay time. During the delay time, all interfaces are blocked temporarily.The stp timer forward-delay command is used to set the Forward Delay timer.

**Configuration Impact**

The value of the Forward Delay timer set on the root bridge is advertised to other devices of the same spanning tree using BPDUs. Then it becomes the value of the Forward Delay timer of all devices in the spanning tree.

**Precautions**

The relationships between the Hello Time, Forward Delay, and MaxAge are as follows. The spanning tree functions properly only if the correct relationships are established. Otherwise, frequent network flapping occurs.

* 2 x (Forward Delay - 1.0 second) >= Max Age
* Max Age >= 2 x (Hello Time + 1.0 second)Running the **stp vlan bridge-diameter** command to set the network diameter is recommended. After the stp bridge-diameter command is run, the switching device sets optimum values for the three parameters, Hello Time, Forward Delay, and Max Age.

Example
-------

# Set the Forward Delay value to 2000 centiseconds (20 seconds) for VLAN 10 when VBST is running.
```
<HUAWEI> system-view
[~HUAWEI] stp vlan 10 timer forward-delay 2000

```