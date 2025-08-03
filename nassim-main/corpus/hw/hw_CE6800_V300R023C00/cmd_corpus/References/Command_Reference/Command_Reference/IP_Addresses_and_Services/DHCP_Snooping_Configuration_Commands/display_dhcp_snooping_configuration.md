display dhcp snooping configuration
===================================

display dhcp snooping configuration

Function
--------



The **display dhcp snooping configuration** command displays the DHCP snooping configuration.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display dhcp snooping configuration** [ **interface** { *interface-type* *interface-number* | *interface-name* } | **vlan** *vlan-id* | **bridge-domain** *bd-id* ]

For CE6820H, CE6820H-K, CE6820S, CE6885-LL (low latency mode):

**display dhcp snooping configuration** [ **interface** { *interface-type* *interface-number* | *interface-name* } | **vlan** *vlan-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* | Interface type. | - |
| *interface-number* | Specifies an interface number. | - |
| *interface-name* | interface-name specifies the name of an interface. | The value is a string of 1 to 128 case-sensitive characters. It cannot contain spaces. |
| **vlan** *vlan-id* | Displays DHCP snooping running information in a specified VLAN. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **bridge-domain** *bd-id* | Displays DHCP snooping running information in a specified BD.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer that ranges from 1 to 16777215. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After DHCP snooping is configured, you can run this command to view the DHCPv4 and DHCPv6 snooping configurations. If no VLAN or interface is specified, all DHCP snooping configurations are displayed. If a VLAN or an interface is specified, only the DHCP snooping configuration in the VLAN or on the interface is displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display all the DHCP snooping configurations.
```
<HUAWEI> display dhcp snooping configuration
#
dhcp snooping enable
#
vlan 3
 dhcp snooping enable
 dhcp snooping check dhcp-giaddr enable
#
interface 10GE1/0/1
 dhcp snooping enable
#

```

**Table 1** Description of the **display dhcp snooping configuration** command output
| Item | Description |
| --- | --- |
| dhcp snooping enable | Enables the DHCP snooping function. |
| dhcp snooping check dhcp-giaddr enable | Enables the function of checking whether the GIADDR field in DHCP messages is 0. |
| vlan | DHCP snooping configuration in a VLAN. |
| interface | DHCP snooping configuration on an interface. |