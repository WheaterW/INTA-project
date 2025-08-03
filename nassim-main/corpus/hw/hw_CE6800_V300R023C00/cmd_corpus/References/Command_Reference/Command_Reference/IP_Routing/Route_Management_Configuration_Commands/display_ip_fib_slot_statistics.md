display ip fib slot statistics
==============================

display ip fib slot statistics

Function
--------



The **display ip fib slot statistics** command displays the total number of IPv4 FIB entries.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K:

**display ip fib slot** *slot-id* [ **vpn-instance** *vpn-instance-name* ] **statistics**

For CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**display ip fib slot** *slot-id* **cpuid** *cpuid* [ **vpn-instance** *vpn-instance-name* ] **statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *slot-id* | Specifies the slot ID. | The value is a string of 0 to 4 case-sensitive characters, spaces not supported. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |
| **cpuid** *cpuid* | Specifies the CPU ID.  NOTE:  This parameter is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a string of 1 to 23 case-sensitive characters, spaces not supported. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

This command is used to detect route module faults. If the routing module is working properly, the number of routes displayed in the command output is the same as the number of routes in the Summary Prefixes field in the **display ip routing-table statistics** command output.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the total number of IPv4 public network FIB entries on the board in slot 1.
```
<HUAWEI> display ip fib slot 1 statistics
Route Entry Count : 6

```

# Display the total number of IPv4 FIB entries in the VPN instance named vpna on the board in a specified slot.
```
<HUAWEI> display ip fib slot 1 cpuid 0 vpn-instance vpna statistics
Route Entry Count : 2

```

**Table 1** Description of the **display ip fib slot statistics** command output
| Item | Description |
| --- | --- |
| Route Entry Count | Number of IPv4 FIB entries. |