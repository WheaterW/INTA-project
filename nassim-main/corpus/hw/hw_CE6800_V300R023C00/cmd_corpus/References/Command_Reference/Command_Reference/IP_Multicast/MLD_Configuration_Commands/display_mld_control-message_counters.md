display mld control-message counters
====================================

display mld control-message counters

Function
--------



The **display mld control-message counters** command displays the statistics of Multicast Listener Discovery (MLD) messages received by the interface.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display mld control-message counters** [ **interface** { *interface-type* *interface-number* | *interface-name* } ] **message-type** { **query** | **report** }

**display mld control-message counters** [ **interface** { *interface-type* *interface-number* | *interface-name* } ]

**display mld** { **vpn-instance** *instance-name* | **all-instance** } **control-message** **counters** [ **interface** { *interface-type* *interface-number* | *interface-name* } ] **message-type** { **query** | **report** }

**display mld** { **vpn-instance** *instance-name* | **all-instance** } **control-message** **counters** [ **interface** { *interface-type* *interface-number* | *interface-name* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* | Specifies the type and number of an interface type. | - |
| *interface-number* | Specifies an interface number. | - |
| *interface-name* | Specifies the name of an interface. | - |
| **message-type** | Indicates the MLD message type. | - |
| **query** | Indicates the statistics of Query messages received by an interface. | - |
| **report** | Indicates the statistics of Report messages received by an interface. | - |
| **vpn-instance** *instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **all-instance** | Specifies all VPN instance. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

When running the **display mld control-message counters** command, note the following:

* If interface port-type port-number is specified, only the statistics of MLD messages received by the specified interface are displayed.
* If message-type and interface are specified, only the statistics of a specified type of MLD messages received by the interface are displayed.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about MLD messages received by 100GE1/0/1 in the public network instance.
```
<HUAWEI> display mld control-message counters interface 100GE 1/0/1
Interface control-message counters information of VPN-Instance: public net
 100GE1/0/1(FE80::D57E:0:3075:2):
 Message Type                Sent        Valid       Invalid     Ignore
 ------------------------------------------------------------------
 General Query               23          0           0           0
 Group Query                 0           0           0           0
 Source Group Query          0           0           0           0
 ------------------------------------------------------------------
 MLDV1
 Report ASM                  0           0           0           0
 Report SSM                  0           0           0           0
 ------------------------------------------------------------------
 DONE  ASM                   0           0           0           0
 DONE  SSM                   0           0           0           0
 ------------------------------------------------------------------
 MLDV2
 ISIN Report                 0           0           0           0
 ISEX Report                 0           0           0           0
 TOIN Report                 0           0           0           0
 TOEX Report                 0           0           0           0
 ALLOW Report                0           0           0           0
 BLOCK Report                0           0           0           0
 Source Records Total        0           0           0           0
 ------------------------------------------------------------------
 Others                      -           -           0           0
 ------------------------------------------------------------------

```

**Table 1** Description of the **display mld control-message counters** command output
| Item | Description |
| --- | --- |
| Interface control-message counters information of VPN-Instance | Indicates the VPN instance of the interface control message statistics information. |
| General Query | Number of general query messages. |
| Group Query | Number of group query messages. |
| Source Group Query | Number of source/group query messages. |
| Source Records Total | Number of source-Records-total messages. |
| Report ASM | Number of mld-v1 asm-report messages. |
| Report SSM | Number of MLDv1 SSM-Report messages. |
| DONE ASM | Number of asm-done messages. |
| DONE SSM | Number of SSM-Done messages. |
| ISIN Report | Number of mld-v2 isin-report messages. |
| ISEX Report | Number of MLD-v2 isex-report messages. |
| TOIN Report | Number of MLD-v2 toin-report messages. |
| TOEX Report | Number of MLD-v2 toex-report messages. |
| ALLOW Report | Number of MLD-v2 allow-report messages. |
| BLOCK Report | Number of MLD-v2 block-report messages. |
| Others | Number of messages of unknown types. |