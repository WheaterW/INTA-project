stp vlan timer hello
====================

stp vlan timer hello

Function
--------



The **stp vlan timer hello** command sets the interval of the switching device to send BPDUs, that is, the value of the Hello Time.

The **undo stp vlan timer hello** command restores the default setting.



By default, the interval of the switch to send BPDUs is 200 centiseconds (2 seconds).


Format
------

**stp vlan** *vlan-id* [ **to** *vlan-id* ] [ *vlan-id* [ **to** *vlan-id* ] ] &<1-9> **timer** **hello** *time-value*

**undo stp vlan** *vlan-id* [ **to** *vlan-id* ] [ *vlan-id* [ **to** *vlan-id* ] ] &<1-9> **timer** **hello** [ *time-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **to** *vlan-id* | Specifies one or more VLANs in which the Hello timer value is set. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| *time-value* | Specifies the interval at which the device sends BPDUs, in centiseconds. The step is 100. | The value is an integer that ranges from 100 to 1000, in centiseconds, and the step is 100. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a network where a spanning tree protocol is enabled, a switching device periodically sends BPDUs to other devices in the same spanning tree at the interval of the Hello Time. Sending BPDUs periodically ensures that the spanning tree is stable. The stp vlan timer hello command can be used to set the BPDU sending interval, that is, the Hello Time.If no BPDUs are received by the switching device within the timeout period (timeout period = Hello Time x 3 x Timer Factor), the spanning tree is calculated again.

**Configuration Impact**

The value of the Forward Delay timer set on the root bridge is advertised to other devices of the same spanning tree using BPDUs. Then it becomes the value of the Forward Delay timer of all devices in the spanning tree.

**Precautions**

The relationships between the Hello Time, Forward Delay, and Max Age are as follows. The spanning tree works properly only if the relationships are correctly established. Otherwise, frequent network flapping occurs.

* 2 x (Forward Delay - 1.0 second) >= Max Age
* Max Age >= 2 x (Hello Time + 1.0 second)Running the **stp vlan bridge-diameter** command to set the network diameter is recommended. After the stp bridge-diameter command is run, the switching device sets optimum values for the three parameters, Hello Time, Forward Delay, and Max Age.

Example
-------

# Set the Hello time to 400 centiseconds (4 seconds) for VLAN 10 when VBST is running.
```
<HUAWEI> system-view
[~HUAWEI] stp vlan 10 timer hello 400

```