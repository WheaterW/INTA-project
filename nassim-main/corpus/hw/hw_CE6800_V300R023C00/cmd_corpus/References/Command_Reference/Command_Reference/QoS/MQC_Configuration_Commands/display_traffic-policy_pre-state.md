display traffic-policy pre-state
================================

display traffic-policy pre-state

Function
--------



The **display traffic-policy pre-state** command displays information about resources occupied by the traffic policy to be applied, based on which you can determine whether the traffic policy can be successfully applied after the configuration is committed.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display traffic-policy pre-state** { **global** [ **slot** *slot-id* ] | **interface** { *interface-type* *interface-number* | *interface-name* } | **vlan** *vlan-id* | **qos** **group** *qos-group-name* | **vpn-instance** *vpn-instance-name* } *traffic-policy-name* { **inbound** | **outbound** }

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display traffic-policy pre-state bridge-domain** *bd-id* *traffic-policy-name* { **inbound** | **outbound** }

For CE6885-LL (low latency mode):

**display traffic-policy pre-state** { **global** [ **slot** *slot-id* ] | **interface** { *interface-type* *interface-number* | *interface-name* } | **vlan** *vlan-id* | **qos** **group** *qos-group-name* | **vpn-instance** *vpn-instance-name* } *traffic-policy-name* { **inbound** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **global** | Displays information about resources occupied by a traffic policy to be applied in the system view. | - |
| **slot** *slot-id* | Displays information about resources occupied by a traffic policy to be applied in a specified slot. | The value is an integer or a character string. You can enter a question mark (?) and select a value from the displayed value range. |
| **interface** *interface-type* *interface-number* | Displays information about resources occupied by a traffic policy to be applied on a specific interface.   * interface-type specifies the interface type. * interface-number specifies the interface number. | - |
| *interface-name* | Displays information about resources occupied by a traffic policy to be applied on a specified interface. | - |
| **vlan** *vlan-id* | Displays information about resources occupied by a traffic policy to be applied in a specific VLAN. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer that ranges from 1 to 1023. |
| **vpn-instance** *vpn-instance-name* | The traffic policy is applied under the specified vpn-instance. | The value is a string of 1 to 31 case-sensitive characters without spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| *traffic-policy-name* | Specifies the name of a traffic policy to be applied. | The value is a string of 1 to 31 case-sensitive characters, starting with a letter or digit. It cannot contain spaces or question marks (?). |
| **inbound** | Displays information about resources occupied by a traffic policy to be applied in the inbound direction. | - |
| **outbound** | Displays information about resources occupied by a traffic policy to be applied in the outbound direction.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **bridge-domain** *bd-id* | Displays information about resources occupied by a traffic policy to be applied in a specific broadcast domain.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer ranging from 1 to 16777215. |
| **qos** **group** *qos-group-name* | The traffic policy is applied under the specified qos group. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

Before applying a traffic policy, you can run the **display traffic-policy pre-state** command to check information about resources occupied by the traffic policy to be applied. Then you can determine whether the traffic policy can be successfully applied after the configuration is committed.

**Precautions**

* The **display traffic-policy pre-state** command displays information about resources occupied by the traffic policy to be applied, based on which you can determine whether the traffic policy can be successfully applied after the configuration is committed.
* You can run this command to view information about resources occupied by only one traffic policy to be applied at a time. If multiple traffic policies are configured, whether these traffic policies can be applied successfully cannot be determined based on the resource information displayed using this command.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about resources occupied by traffic policy test to be applied in the inbound direction of 100GE1/0/1.
```
<HUAWEI> display traffic-policy pre-state interface 100GE1/0/1 test inbound
Slot: 1    Chip: 0                                                              
---------------------------------------------------------------------------
Direction    ServiceName              Group       NeedEntrys     Pre-State 
---------------------------------------------------------------------------
Ingress       Traffic Policy Port       30             1                     OK         
---------------------------------------------------------------------------

```

**Table 1** Description of the **display traffic-policy pre-state** command output
| Item | Description |
| --- | --- |
| Direction | Direction in which a packet is forwarded. |
| ServiceName | Name of the application. |
| Group | Service delivery group. |
| NeedEntrys | Number of entry resources required by a group. |
| Pre-State | Whether a traffic policy can be successfully applied in the current state:   * OK: The traffic policy can be successfully applied in the current state. * NO: The traffic policy cannot be applied in the current state. |
| Slot | Slot ID. |
| Chip | Chip ID. |