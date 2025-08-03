display system tcam service traffic-policy
==========================================

display system tcam service traffic-policy

Function
--------



The **display system tcam service traffic-policy** command displays data of a traffic policy that has been applied.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display system tcam service traffic-policy global** *traffic-policy-name* { **inbound** | **outbound** } [ **slot** *slot-id* [ **chip** *chip-id* ] ]

**display system tcam service traffic-policy interface** { *interface-type* *interface-number* | *interface-name* } *traffic-policy-name* { **inbound** | **outbound** } [ **slot** *slot-id* [ **chip** *chip-id* ] ]

**display system tcam service traffic-policy slot** *slot-id* *traffic-policy-name* { **inbound** | **outbound** } [ **chip** *chip-id* ]

**display system tcam service traffic-policy vlan** *vlan-id* *traffic-policy-name* { **inbound** | **outbound** } [ **slot** *slot-id* [ **chip** *chip-id* ] ]

**display system tcam service traffic-policy qos group** *qos-group-name* *traffic-policy-name* { **inbound** | **outbound** } [ **slot** *slot-id* [ **chip** *chip-id* ] ]

**display system tcam service traffic-policy vpn-instance** *vpn-instance-name* *traffic-policy-name* { **inbound** | **outbound** } [ **slot** *slot-id* [ **chip** *chip-id* ] ]

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display system tcam service traffic-policy bridge-domain** *bd-id* *traffic-policy-name* { **inbound** | **outbound** } [ **slot** *slot-id* [ **chip** *chip-id* ] ]

For CE6885-LL (low latency mode):

**display system tcam service traffic-policy** { **global** | **vlan** *vlan-id* | **interface** { *interface-type* *interface-number* | *interface-name* } | **vpn-instance** *vpn-instance-name* | **qos** **group** *qos-group-name* } *traffic-policy-name* { **inbound** } [ **slot** *slot-id* [ **chip** *chip-id* ] ]

**display system tcam service traffic-policy slot** *slot-id* *traffic-policy-name* { **inbound** } [ **chip** *chip-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *traffic-policy-name* | Display the application data of a specified traffic policy. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |
| **inbound** | Applies a traffic policy to the inbound direction. | - |
| **outbound** | Applies a traffic policy to the outbound direction.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **slot** *slot-id* | Specifies a slot ID. | You can enter a question mark (?) and select a value based on the prompt. |
| **chip** *chip-id* | Specifies the chip ID. | You can enter a question mark (?) and select a value based on the prompt. |
| **interface** *interface-type* *interface-number* | Specifies the interface to which the traffic policy is applied.   * interface-type specifies the interface type. * interface-number specifies the interface number. | - |
| *interface-name* | Specifies the interface to which the traffic policy is applied. | - |
| **vlan** *vlan-id* | Specifies the ID of the VLAN to which the traffic policy is applied. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer that ranges from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer that ranges from 1 to 1023. |
| **group** *qos-group-name* | Specifies the QoS group to which the traffic policy is applied. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The first character must be a letter. |
| **vpn-instance** *vpn-instance-name* | Specifies the VPN instance to which the traffic policy is applied. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. The character string can contain spaces if it is enclosed with double quotation marks (""). |
| **bridge-domain** *bd-id* | Specifies a BD to which the traffic policy is applied.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer ranging from 1 to 16777215. |
| **global** | Specifies the name of a traffic policy instance to be applied globally. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

Due to internal logic error, a traffic policy may fail to be applied or is successfully applied but cannot take effect. You can use this command to view service data of a traffic policy.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display service data of a traffic policy in chip 0.
```
<HUAWEI> display system tcam service traffic-policy interface 100GE 1/0/1 p1 inbound  slot 1 chip 0
Instance ID  : 0                                                                
Status code  : 0                                                                
Group ID     : 68                                                               
----------------------------------------------------------------------------    
Slot         : 1                                                                
----------------------------------------------------------------------------    
Chip  ClassID  ClassPri   MatchID   MatchPri   RulePri  BehaviorID   EntryID    
----------------------------------------------------------------------------    
   0        0         5         1          1         0           0       222    
----------------------------------------------------------------------------

```

**Table 1** Description of the **display system tcam service traffic-policy** command output
| Item | Description |
| --- | --- |
| slot | Slot ID. |
| chip | Chip ID. |
| Instance ID | Application instance ID. |
| Status code | Application status code. |
| Group ID | ID of the group. |
| ClassID | ID of the traffic classifier. |
| ClassPri | Priority of the traffic classifier. |
| MatchID | ID of the if-match rule. |
| MatchPri | Priority of the if-match rule. |
| RulePri | Priority of the rule. |
| BehaviorID | ID of the traffic behavior. |
| EntryID | ID of the entry. |