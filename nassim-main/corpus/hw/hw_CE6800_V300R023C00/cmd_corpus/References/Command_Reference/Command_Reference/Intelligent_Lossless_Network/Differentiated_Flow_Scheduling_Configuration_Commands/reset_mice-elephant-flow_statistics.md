reset mice-elephant-flow statistics
===================================

reset mice-elephant-flow statistics

Function
--------



The **reset mice-elephant-flow statistics** command clears statistics about discarded packets in mice flows.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset mice-elephant-flow statistics** [ **interface** { *interface-name* | *interface-type* *interface-number* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Clears statistics about mice flows on a specified interface where differentiated flow scheduling is enabled.   * interface-type specifies the interface type. * interface-number specifies the interface number. | - |
| **interface** *interface-name* | Clears statistics about mice flows on a specified interface where differentiated flow scheduling is enabled.  interface-name specifies the name of an interface. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

You can run this command to clear statistics about mice flows on an interface where differentiated flow scheduling is enabled, including the number of forwarded packets, packet forwarding rate, number of discarded packets, and packet discarding rate.


Example
-------

# Clear statistics about mice flows on an interface where differentiated flow scheduling is enabled.
```
<HUAWEI> reset mice-elephant-flow statistics

```