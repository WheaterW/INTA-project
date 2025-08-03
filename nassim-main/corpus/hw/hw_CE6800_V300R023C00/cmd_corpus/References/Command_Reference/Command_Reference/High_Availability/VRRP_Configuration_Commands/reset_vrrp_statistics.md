reset vrrp statistics
=====================

reset vrrp statistics

Function
--------



The **reset vrrp statistics** command clears statistics about the VRRP Advertisement packets sent and received by a VRRP group.




Format
------

**reset vrrp** [ **interface** { *interface-name* | *interface-type* *interface-number* } ] [ **vrid** *virtual-router-id* ] **statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-name* *interface-type* *interface-number* | Specifies the name, type, and ID of an interface. | - |
| **vrid** *virtual-router-id* | Specifies the ID of a VRRP group. | The value is an integer ranging from 1 to 255. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To clear statistics about packets sent and received by a VRRP group for fault locating, run the **reset vrrp statistics** command.

* If interface-type, interface-name, and interface-number are specified but virtual-router-id is not, this command clears statistics about packets sent and received by all VRRP groups on a specified interface.
* If virtual-router-id is specified but interface-type, interface-name, and interface-number are not, this command clears statistics about packets sent and received by a specified VRRP group on all interfaces.
* If neither interface-type, interface-name, interface-number, or virtual-router-id is specified, this command clears statistics about packets sent and received by all VRRP groups.

**Configuration Impact**

After the **reset vrrp statistics** command is run, statistics about the received and sent VRRP Advertisement packets are cleared.

**Precautions**

Statistics about VRRP Advertisement packets cannot be restored after being cleared. Therefore, exercise caution when running this command.


Example
-------

# Clear statistics about the packets of all VRRP groups.
```
<HUAWEI> reset vrrp statistics

```

# Clear statistics about the packets of VRRP group 1 on 100GE 1/0/1.
```
<HUAWEI> reset vrrp interface 100GE 1/0/1 vrid 1 statistics

```