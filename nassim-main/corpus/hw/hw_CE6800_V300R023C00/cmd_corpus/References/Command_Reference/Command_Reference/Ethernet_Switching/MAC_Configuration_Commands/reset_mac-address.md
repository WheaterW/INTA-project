reset mac-address
=================

reset mac-address

Function
--------



The **reset mac-address** command deletes dynamically learned MAC address entries on a device.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**reset mac-address** [ *interface-type* *interface-number* | *interface-name* ]

**reset mac-address** { { *interface-type* *interface-number* | *interface-name* } **vlan** *vlan-id* | **vlan** *vlan-id* [ *interface-type* *interface-number* | *interface-name* ] }

**reset mac-address** *mac-address* [ **vlan** *vlan-id* ]

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**reset mac-address bridge-domain** *bd-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* | Specifies the type of an interface. | - |
| *interface-number* | Specifies an interface number. | - |
| *interface-name* | Specifies the interface name. | - |
| *mac-address* | Specifies a MAC address. | The value is a hexadecimal number in the format of H-H-H. H is a 4-bit hexadecimal number, such as 00e0 or fc01. If an H contains fewer than 4 digits, the left-most digits are padded with zeros. For example, e0 is displayed as 00e0. |
| **vlan** *vlan-id* | Specifies a VLAN ID. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **bridge-domain** *bd-id* | Specifies the BD ID.  Only the CE6885, CE8851-32CQ4BQ, CE8851-32CQ8DQ-P, CE8855, CE8851K, CE8850-SAN, CE8850-HAM, CE6866, CE6866K, CE6860-SAN, CE6860-HAM, CE6863H, CE6863H-K, CE6881H, and CE6881H-K support this parameters.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer that ranges from 1 to 16777215. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To delete dynamically learned MAC address entries (entries to be deserted, for example), run the **reset mac-address** command.

**Prerequisites**



Before the **reset mac-address** command is run, the BD and VLAN have been created.



**Precautions**



After the **reset mac-address** command is run, the dynamically learned MAC address entries are deleted and cannot be restored. Exercise caution when running the command. To prevent incorrect deletion of available MAC address entries, specify a BD ID, VLAN ID, or interface name for a MAC address entry to be deleted.




Example
-------

# Delete MAC address entries on a specified interface.
```
<HUAWEI> reset mac-address 100GE 1/0/1

```

# Delete a specified MAC address entry.
```
<HUAWEI> reset mac-address 00e0-fc12-3456

```