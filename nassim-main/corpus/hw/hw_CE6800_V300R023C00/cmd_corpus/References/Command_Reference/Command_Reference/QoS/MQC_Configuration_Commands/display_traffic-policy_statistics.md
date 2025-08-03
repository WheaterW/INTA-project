display traffic-policy statistics
=================================

display traffic-policy statistics

Function
--------



The **display traffic-policy statistics** command displays statistics on packets matching a traffic policy.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display traffic-policy statistics** { **global** [ **slot** *slot-id* ] | **interface** { *interface-type* *interface-number* | *interface-name* } | **vlan** *vlan-id* | **vpn-instance** *vpn-instance-name* | **qos** **group** *group-name* | **bridge-domain** *bd-id* } [ *policy-name* ] [ **inbound** | **outbound** ] [ { **classifier-base** | **rule-base** } [ **class** *classifier-name* ] ]

**display traffic-policy statistics** { **global** [ **slot** *slot-id* ] | **interface** { *interface-type* *interface-number* | *interface-name* } | **vlan** *vlan-id* | **vpn-instance** *vpn-instance-name* | **qos** **group** *group-name* | **bridge-domain** *bd-id* } [ *policy-name* ] [ **inbound** | **outbound** ] **rule-base** [ **class** *classifier-name* ] **history**

For CE6820H, CE6820H-K, CE6820S:

**display traffic-policy statistics** { **global** [ **slot** *slot-id* ] | **interface** { *interface-type* *interface-number* | *interface-name* } | **vlan** *vlan-id* | **vpn-instance** *vpn-instance-name* | **qos** **group** *group-name* } [ *policy-name* ] [ **inbound** | **outbound** ] **rule-base** [ **class** *classifier-name* ] **history**

**display traffic-policy statistics** { **global** [ **slot** *slot-id* ] | **interface** { *interface-type* *interface-number* | *interface-name* } | **vlan** *vlan-id* | **vpn-instance** *vpn-instance-name* | **qos** **group** *group-name* } [ *policy-name* ] [ **inbound** | **outbound** ] [ { **classifier-base** | **rule-base** } [ **class** *classifier-name* ] ]

For CE6885-LL (low latency mode):

**display traffic-policy statistics** { **global** [ **slot** *slot-id* ] | **interface** { *interface-name* | *interface-type* *interface-number* } | **vlan** *vlan-id* | **vpn-instance** *vpn-instance-name* | **qos** **group** *group-name* } [ *policy-name* ] [ **inbound** ] **rule-base** [ **class** *classifier-name* ] **history**

**display traffic-policy statistics** { **global** [ **slot** *slot-id* ] | **interface** { *interface-name* | *interface-type* *interface-number* } | **vlan** *vlan-id* | **vpn-instance** *vpn-instance-name* | **qos** **group** *group-name* } [ *policy-name* ] [ **inbound** ] [ { **classifier-base** | **rule-base** } [ **class** *classifier-name* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **global** | Displays packet statistics in the system to which a traffic policy has been applied. | - |
| **slot** *slot-id* | Specifies a slot ID. | The value is an integer. You can enter the question mark (?) and select the value as prompted. |
| **interface** *interface-type* *interface-number* | Displays packet statistics on an interface to which a traffic policy has been applied.   * interface-type specifies the interface type. * interface-number specifies the interface number. | -  -  -  -  - |
| *interface-name* | Displays packet statistics on a specified interface to which a traffic policy has been applied. | - |
| **vlan** *vlan-id* | Displays packet statistics in a specified VLAN to which a traffic policy has been applied. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer that ranges from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer that ranges from 1 to 1023. |
| **vpn-instance** *vpn-instance-name* | Displays packet statistics in a specified VPN instance to which a traffic policy has been applied. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. "\_public\_" is reserved and cannot be used as a VPN instance name. |
| *policy-name* | Displays statistics on packets matching a specified traffic policy. | The value is a string of 1 to 31 case-sensitive characters, starting with a letter or digit. It cannot contain spaces. |
| **inbound** | Displays packet statistics in the inbound direction to which a traffic policy has been applied. | - |
| **outbound** | Displays packet statistics in the outbound direction to which a traffic policy has been applied.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **classifier-base** | Displays statistics on packets matching a specified traffic classifier. If this parameter is specified, statistics on packets matching a traffic classifier in the traffic policy are displayed. | - |
| **rule-base** | Displays statistics on packets matching a rule. If this parameter is specified, statistics on packets matching all rules are displayed. | - |
| **class** *classifier-name* | Specifies the name of a traffic classifier. If this parameter is specified, statistics on packets matching the specified traffic classifier or rules in the specified traffic classifier are displayed. If this parameter is not specified, statistics on packets matching all traffic classifiers are displayed. | The value is a string of 1 to 31 case-sensitive characters, starting with a letter or digit. It cannot contain spaces. |
| **history** | Display packet history statistics to which a traffic policy has been applied. | - |
| **bridge-domain** *bd-id* | Displays the record of a traffic policy that has been applied in a BD.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer that ranges from 1 to 16777215. |
| **group** *group-name* | Displays packet statistics in a specified QoS group to which a traffic policy has been applied. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

The **display traffic-policy statistics** command displays packet statistics. The command output helps you check statistics on forwarded and discarded packets after a traffic policy is applied and locate faults.

**Prerequisites**

Run the **display traffic-policy statistics** command to collect traffic statistics and run the **statistics enable** command in the traffic behavior view.

**Precautions**

* If a traffic policy contains many rules, after the **reset traffic-policy statistics** command has been used, wait for a period and run the **display traffic-policy statistics** command. If you run the **display traffic-policy statistics** command immediately, information may be not displayed.
* When a traffic policy containing many rules and the traffic statistics action is configured and the statistics are being queried based on instances or traffic classifiers, command line execution is interrupted and MIB-based query expires. By default, the timeout of MIB-based query is 5s and only statistics on packets matching the traffic policy within 1024 rules can be queried. When a traffic policy defines more than 1024 rules, the system reads cached data. When a traffic policy defines more than 1024 rules, the timeout of MIB-based query needs to be changed based on the data volume and the cached data is counted.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display traffic statistics in the inbound direction to which a traffic policy has been applied.
```
<HUAWEI> display traffic-policy statistics interface 100ge 1/0/1 inbound
Traffic policy: p1, inbound                                                                                                         
--------------------------------------------------------------------------------
 Slot: 1                                                                        
 Item                  Packets                Bytes           pps           bps 
 -------------------------------------------------------------------------------
 Matched                     0                    0             0             0 
  Passed                     0                    0             0             0 
  Dropped                    0                    0             0             0 
   Filter                    0                    0             0             0 
   CAR                       0                    0             0             0 
 -------------------------------------------------------------------------------

```

# Display statistics on incoming packets matching a rule after the traffic policy is applied to the system.
```
<HUAWEI> display traffic-policy statistics global inbound rule-base
Traffic policy: p1, inbound                                                     
--------------------------------------------------------------------------------
  Classifier: c1, Behavior: b1                                                  
    Slot: 1                                                                     
    ----------------------------------------------------------------------------
    if-match any                                                                
    Passed Packets                       0, Passed Bytes                       0
    Passed pps                           0, Passed bps                         0
    Dropped Packets                      0, Dropped Bytes                      0
    Dropped pps                          0, Dropped bps                        0
    ----------------------------------------------------------------------------

```

# Display traffic history statistics in inbound direction to which a traffic policy has been applied.
```
<HUAWEI> display traffic-policy statistics interface 100ge 1/0/1 inbound rule-base  history
Traffic policy: yc1, inbound                                                                                                        
--------------------------------------------------------------------------------                                                    
    Slot: 1                                                                                                                         
    ----------------------------------------------------------------------------                                                    
    if-match vlan 10                                                                               
        Time Period                          Matched Packets       Matched Bytes                                                    
        ------------------------------------------------------------------------                                                    
        2020-11-08 20:27~2020-11-08 20:28               1209              154752                                                    
        ------------------------------------------------------------------------                                                    
    ----------------------------------------------------------------------------

```

**Table 1** Description of the **display traffic-policy statistics** command output
| Item | Description |
| --- | --- |
| Traffic policy | Traffic policy that has been applied and direction in which the traffic policy has been applied. |
| Packets | Number of packets. |
| Bytes | Number of bytes. |
| Matched | Numbers of packets and bytes that match traffic classification rules. The data is originated from the packet statistics that have been collected since the original statistics were cleared last time. |
| Matched Packets | Numbers of packets in interval time that match traffic classification rules. |
| Matched Bytes | Numbers of bytes in interval time that match traffic classification rules. |
| Passed | Numbers of forwarded packets and bytes that match traffic classification rules. The data is originated from the packet statistics that have been collected since the original statistics were cleared last time. |
| Dropped | Numbers of discarded packets and bytes that match traffic classification rules. The data is originated from the packet statistics that have been collected since the original statistics were cleared last time. The dropped packets include the filtered packets and packets dropped by CAR. |
| Filter | Number of discarded packets and bytes by the filtering action among the packets matching the traffic classifier. Packet statistics have been collected after the previous statistics were cleared last time. |
| CAR | Numbers of packets and bytes that match the traffic classification rule and are discarded by CAR. The data is originated from the packet statistics that have been collected since the original statistics were cleared last time. To configure CAR, run the car (traffic behavior view) command. |
| Car | Numbers of packets and bytes that match the traffic classifier. The traffic classifier is bound to the traffic behavior that containing the CAR action. The data is originated from the packet statistics that have been collected since the original statistics were cleared last time. |
| Green | Number and bytes of green packets to which CAR is applied. The data is originated from the packet statistics that have been collected since the original statistics were cleared last time. |
| Yellow | Number and bytes of yellow packets to which CAR is applied. The data is originated from the packet statistics that have been collected since the original statistics were cleared last time. |
| Red | Number and bytes of red packets to which CAR is applied. The data is originated from the packet statistics that have been collected since the original statistics were cleared last time. |
| Time Period | Time range in which packet statistics are collected. |
| Classifier | Relationship between rules in the traffic classifier. To create a traffic classifier, run the traffic classifier command. |
| Behavior | Traffic behavior name. To create a traffic behavior, run the traffic behavior command. |
| slot | Slot ID. |