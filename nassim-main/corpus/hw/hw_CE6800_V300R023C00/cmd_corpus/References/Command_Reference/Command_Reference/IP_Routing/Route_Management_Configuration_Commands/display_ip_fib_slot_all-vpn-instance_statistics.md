display ip fib slot all-vpn-instance statistics
===============================================

display ip fib slot all-vpn-instance statistics

Function
--------



The **display ip fib slot all-vpn-instance statistics** command displays statistics about the IPv4 route FIB tables of all VPNs on a specified board.




Format
------

**display ip fib slot** *slot-id* **all-vpn-instance** **statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Specifies the slot ID. | The value is a string of 1 to 23 case-sensitive characters, spaces not supported. |



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


# Display the total number of IPv4 FIB entries of all VPNs on the board in slot 1.
```
<HUAWEI> display ip fib slot 1 all-vpn-instance statistics
Route Entry Count of VPN _public_ : 14
Route Entry Count of VPN vpn_gmc : 1

```

**Table 1** Description of the **display ip fib slot all-vpn-instance statistics** command output
| Item | Description |
| --- | --- |
| Route Entry Count | Number of IPv4 FIB entries. |