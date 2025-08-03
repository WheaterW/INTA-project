reset ipv6 neighbors
====================

reset ipv6 neighbors

Function
--------



The **reset ipv6 neighbors** command clears dynamic IPv6 ND entries.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset ipv6 neighbors** { **dynamic** | { *interface-name* | *interface-type* *interface-number* } }

**reset ipv6 neighbors vlan** *vlan-id* [ *interface-name* | *interface-type* *interface-number* ]

**reset ipv6 neighbors dynamic** { *interface-name* | *interface-type* *interface-number* } *ipv6-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **dynamic** | Clears dynamic ND entries on all interfaces. | - |
| *interface-name* | Clears all dynamic ND entries on a specified interface. | - |
| *interface-type* *interface-number* | Clears dynamic ND entries on a specified interface. | - |
| **vlan** *vlan-id* | Clears dynamic ND entries of a specified VLAN ID. | The value is an integer ranging from 1 to 4094. |
| *ipv6-address* | Clears dynamic ND entries with a specified IPv6 address on a specified interface. | The address is a 32-bit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the number of dynamic ND entries exceeds the upper threshold, run the **reset ipv6 neighbors** command to delete unwanted dynamic ND entries.

**Configuration Impact**



Running the **reset ipv6 neighbors** command clears specified dynamic ND entries. Exercise caution when running this command.




Example
-------

# Clear all ND entries on 100GE 1/0/1.
```
<HUAWEI> reset ipv6 neighbors 100GE 1/0/1

```

# Clear dynamic ND entries on all interfaces.
```
<HUAWEI> reset ipv6 neighbors dynamic

```

# Clear all ND entries on VLANIF1.
```
<HUAWEI> reset ipv6 neighbors vlanif 1

```

# Clear ND entries with IPv6 address 2001:db8:1::1 on 100GE 1/0/1.
```
<HUAWEI> reset ipv6 neighbors dynamic 100GE 1/0/1 2001:db8:1::1

```