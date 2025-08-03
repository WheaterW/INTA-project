reset port forwarding-path statistics
=====================================

reset port forwarding-path statistics

Function
--------



The **reset port forwarding-path statistics** command clears statistics on packets that contain specified 5-tuple information.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset port forwarding-path path-id** *pathnum* **statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **path-id** *pathnum* | Specifies the path ID. | The value is an integer that ranges from 1 to 128. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

The 5-tuple information includes the source and destination IP addresses, source/destination port numbers in TCP or UDP packets, and protocol type. You can use the display port forwarding-path statistics command to check statistics on packets containing specified 5-tuple information. To facilitate fault locating, you can run the **reset port forwarding-path** command to clear existing statistics.


Example
-------

# Clear statistics on packets matching a specified path ID.
```
<HUAWEI> reset port forwarding-path path-id 2 statistics

```