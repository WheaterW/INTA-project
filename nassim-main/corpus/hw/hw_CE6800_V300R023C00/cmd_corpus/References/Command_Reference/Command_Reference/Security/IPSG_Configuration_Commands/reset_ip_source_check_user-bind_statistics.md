reset ip source check user-bind statistics
==========================================

reset ip source check user-bind statistics

Function
--------



The **reset ip source check user-bind statistics** command clears statistics about discarded IPSG packets.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset ip source check user-bind statistics** [ **vlan** [ *vlan-id* ] | **interface** [ *interface-name* | *interface-type* *interface-number* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vlan** *vlan-id* | Clears statistics about discarded IPSG packets with a specified VLAN ID. | The value is an integer ranging from 1 to 4094. |
| **interface** *interface-name* | Specifies an interface name. | - |
| **interface** *interface-type* *interface-number* | Clears statistics about discarded IPSG packets on a specified interface:  interface-type: specifies the interface type.  interface-number: specifies the interface number. | The value is a string of 1 to 64 case-sensitive characters without spaces. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To view statistics about IPSG discarded packets within a certain period, run this command to clear the existing statistics and then run the **display ip source check user-bind statistics** command to view the new statistics.


Example
-------

# Clear statistics on discarded IPSG packets on the local device.
```
<HUAWEI> reset ip source check user-bind statistics

```