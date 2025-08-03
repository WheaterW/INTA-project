display traffic-policy applied-record
=====================================

display traffic-policy applied-record

Function
--------



The **display traffic-policy applied-record** command displays traffic policy application records.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display traffic-policy applied-record** [ *policy-name* ] [ **global** [ **slot** *slot-id* ] | **interface** { *interface-type* *interface-number* | *interface-name* } | **vlan** *vlan-id* | **qos** **group** *group-name* | **vpn-instance** *vpn-instance-name* | **bridge-domain** *bd-id* ] [ **inbound** | **outbound** ]

For CE6820H, CE6820H-K, CE6820S:

**display traffic-policy applied-record** [ *policy-name* ] [ **global** [ **slot** *slot-id* ] | **interface** { *interface-type* *interface-number* | *interface-name* } | **vlan** *vlan-id* | **qos** **group** *group-name* | **vpn-instance** *vpn-instance-name* ] [ **inbound** | **outbound** ]

For CE6885-LL (low latency mode):

**display traffic-policy applied-record** [ *policy-name* ] [ **global** [ **slot** *slot-id* ] | **interface** { *interface-type* *interface-number* | *interface-name* } | **vlan** *vlan-id* | **qos** **group** *group-name* | **vpn-instance** *vpn-instance-name* ] [ **inbound** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *policy-name* | Specifies a traffic policy name. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. |
| **global** | Displays the record of a traffic policy that has been applied globally. | - |
| **slot** *slot-id* | Specifies a slot ID. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |
| **interface** *interface-type* *interface-number* | Displays the record of a traffic policy that has been applied to an interface.   * interface-type specifies the interface type. * interface-number specifies the interface number. | -  - |
| *interface-name* | Displays the application record of a traffic policy on a specified interface. | - |
| **vlan** *vlan-id* | Displays the record of a traffic policy that has been applied in a VLAN. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer that ranges from 1 to 1023. |
| **vpn-instance** *vpn-instance-name* | Displays the record of a traffic policy that has been applied in a VPN. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. The character string can contain spaces if it is enclosed with double quotation marks (""). |
| **inbound** | Displays the record of a traffic policy that has been applied in the inbound direction. | - |
| **outbound** | Displays the record of a traffic policy that has been applied in the outbound direction.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **group** *group-name* | Displays the record of a traffic policy that has been applied in a QoS group. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |
| **bridge-domain** *bd-id* | Displays the record of a traffic policy that has been applied in a BD.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer ranging from 1 to 16777215. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

This command displays the records of a specified traffic policy or all traffic policies, including the view, interface number, and direction in which a traffic policy is applied. The command output helps you check whether a traffic policy is properly applied and locate faults.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the record of the traffic policy.
```
<HUAWEI> display traffic-policy applied-record
Total records : 3 
--------------------------------------------------------------------------------     
Policy Type/Name                     Apply Parameter             Slot State          
--------------------------------------------------------------------------------     
dsc                                          Global(IN)                      1 success 
--------------------------------------------------------------------------------              
n4                                           100GE1/0/1(IN)               1 fail(3)   
--------------------------------------------------------------------------------     
p1                                           100GE1/0/2(IN)               1 fail(4)        
--------------------------------------------------------------------------------      
Fail reason:  
   3 -- The numbers of matched conditions and actions in the traffic policy exceed the limit. 
   4 -- Insufficient ACL resources.

```

**Table 1** Description of the **display traffic-policy applied-record** command output
| Item | Description |
| --- | --- |
| Total records | Total number of traffic policy records. |
| Policy Type/Name | Traffic policy type or name. |
| Apply Parameter | View and direction to which the traffic policy is applied. |
| Slot | Slot to which the traffic policy is applied. |
| State | Application status of a traffic policy.  Status of the traffic policy applied to the specified slot in the corresponding view and direction:   * success: indicates that the traffic policy is successfully applied. For details about service configurations, see the traffic classifier and traffic behavior configurations. * fail (n): indicates that the application fails. n indicates the code of the traffic policy application failure cause. For details about the failure cause corresponding to the code, see the value of Fail reason. * offline: indicates that no card is installed in the slot, or the card fails to be registered. * waiting: indicates that the application is not delivered. * processing: indicates that the application is being updated or delivered. * â: indicates that the query times out. |
| Fail reason | Reason why a traffic policy fails to be applied in the corresponding view and direction of a specified device.  You are advised to check the configuration as follows:   * If the system displays a message indicating that duplicate rules exist, check whether the matching rules in the traffic classifier are correct. For example, if the relationship between matching rules is AND, the matching fields of the same type are not unique in the traffic classifier. * If the system displays a message indicating that the traffic policy matches too many fields, delete some matching rules. * If the system displays a message indicating that resources are insufficient, delete the configured traffic policy application or disable other features (such as protocol association) using ACL resources. If the fault persists, contact technical support personnel. * If the system displays a message indicating that queue resources fail to be allocated, delete the configured traffic policy application to ensure that queue resources are sufficient. |