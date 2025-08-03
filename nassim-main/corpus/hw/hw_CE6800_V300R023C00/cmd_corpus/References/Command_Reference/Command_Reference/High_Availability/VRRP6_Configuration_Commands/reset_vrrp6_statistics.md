reset vrrp6 statistics
======================

reset vrrp6 statistics

Function
--------



The **reset vrrp6 statistics** command clears statistics about packets sent and received by a Virtual Router Redundancy Protocol for IPv6 (VRRP6) backup group.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset vrrp6** [ **interface** { *interface-name* | *interface-type* *interface-number* } ] [ **vrid** *virtual-router-id* ] **statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-name* *interface-type* *interface-number* | Specifies the name, type, and ID of an interface. | - |
| **vrid** *virtual-router-id* | Specifies the ID of a VRRP6 backup group. | The value is an integer ranging from 1 to 255. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To clear statistics about packets sent and received by a VRRP6 group for fault locating, run the **reset vrrp6 statistics** command.

* If interface-type, interface-name, and interface-number are specified but virtual-router-id is not, this command clears statistics about packets sent and received by all VRRP6 groups on a specified interface.
* If virtual-router-id is specified but interface-type, interface-name, and interface-number are not, this command clears statistics about packets sent and received by a specified VRRP6 group on all interfaces.
* If neither interface-type, interface-name, interface-number, or virtual-router-id is specified, this command clears statistics about packets sent and received by all VRRP6 groups.

**Precautions**

Statistics about packets sent and received by a VRRP6 backup group cannot be restored after being cleared. Exercise caution when running this command.


Example
-------

# Clear statistics about packets sent and received by VRRP6 backup group 1 on 100GE 1/0/2.
```
<HUAWEI> reset vrrp6 interface 100GE 1/0/2 vrid 1 statistics

```

# Clear statistics about packets sent and received by all VRRP6 backup groups.
```
<HUAWEI> reset vrrp6 statistics

```