reset traffic-policy statistics
===============================

reset traffic-policy statistics

Function
--------



The **reset traffic-policy statistics** command clears statistics on packets matching a traffic policy.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**reset traffic-policy statistics** { **global** [ **slot** *slot-id* ] | **interface** { *interface-type* *interface-number* | *interface-name* } | **vlan** *vlan-id* | **vpn-instance** *vpn-instance-name* | **qos** **group** *group-id* } [ *policy-name* ] [ **inbound** | **outbound** ] [ **classifier-base** *classifier-name* ] [ **history** ]

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**reset traffic-policy statistics bridge-domain** *bd-id* [ *policy-name* ] [ **inbound** | **outbound** ] [ **classifier-base** *classifier-name* ] [ **history** ]

For CE6885-LL (low latency mode):

**reset traffic-policy statistics** { **global** [ **slot** *slot-id* ] | **interface** { *interface-type* *interface-number* | *interface-name* } | **vlan** *vlan-id* | **vpn-instance** *vpn-instance-name* | **qos** **group** *group-id* } [ *policy-name* ] [ **inbound** ] [ **classifier-base** *classifier-name* ] [ **history** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **global** | Clears statistics on packets matching a traffic policy in the system. | - |
| **slot** *slot-id* | Specifies a slot ID. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. |
| **interface** *interface-type* *interface-number* | Clears statistics on packets matching a traffic policy on a specified interface. If this parameter is not specified, statistics on packets of all interfaces are cleared.   * interface-type specifies the interface type. * interface-number specifies the interface number. | -  -  -  For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:-  For the CE6885-LL (low latency mode):- |
| *interface-name* | Clears statistics on packets matching a traffic policy applied to a specified interface. If this parameter is not specified, flow-based traffic statistics on all interfaces are cleared. | - |
| **vlan** *vlan-id* | Clears statistics on packets matching a traffic policy in a specified VLAN. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer that ranges from 1 to 1023. |
| **vpn-instance** *vpn-instance-name* | Clears the record of a traffic policy that has been applied in a specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. The character string can contain spaces if it is enclosed with double quotation marks (""). |
| *policy-name* | Clears statistics on packets matching a specified traffic policy. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |
| **inbound** | Clears traffic statistics in the inbound direction. | - |
| **outbound** | Clears traffic statistics in the outbound direction.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **classifier-base** *classifier-name* | Clears statistics on packets matching a specified traffic classifier. | The value is a string of 1 to 31 case-sensitive characters, starting with a letter or digit. It cannot contain spaces. |
| **history** | Clears historical packet statistics after a traffic policy is applied. | - |
| **qos** **group** *group-id* | Clears the record of a traffic policy that has been applied in a specified QoS group. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |
| **bridge-domain** *bd-id* | Clears the record of a traffic policy that has been applied in a BD.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The bd-id value is an integer ranging from 1 to 16777215. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

After this command is run, traffic statistics are cleared and cannot be restored.To view traffic statistics, run the **display traffic-policy statistics** command.

**Precautions**

* After the **reset traffic-policy statistics** command is run, traffic statistics are cleared and cannot be restored. Exercise caution when using the command.
* Running the **reset traffic-policy statistics history** command does not affect the statistics queried using the **display traffic-policy statistics** command. Running the **reset traffic-policy statistics** command affects the historical statistics in a statistical period queried using the **display traffic-policy statistics history** command.


Example
-------

# Clear traffic statistics on VLAN 10 in the inbound direction to which a traffic policy has been applied.
```
<HUAWEI> reset traffic-policy statistics vlan 10 inbound

```

# Clear traffic statistics on an interface in the inbound direction to which a traffic policy has been applied.
```
<HUAWEI> reset traffic-policy statistics interface 100GE 1/0/1 inbound history

```