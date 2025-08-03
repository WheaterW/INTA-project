reset mld control-message counters
==================================

reset mld control-message counters

Function
--------



The **reset mld control-message counters** command deletes statistics of Multicast Listener Discovery (MLD) messages.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**reset mld control-message counters** [ **interface** { *interface-type* *interface-number* | *interface-name* } ] [ **message-type** { **query** | **report** } ]

**reset mld** { **vpn-instance** *instance-name* | **all-instance** } **control-message** **counters** [ **interface** { *interface-type* *interface-number* | *interface-name* } ] [ **message-type** { **query** | **report** } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* | Specifies the type of an interface. | - |
| *interface-number* | Specifies the number of an interface. | - |
| *interface-name* | Specifies the name of an interface. | - |
| **message-type** | Indicates the type of an MLD message. | The types of MLD message are the Query and the Report messages. |
| **query** | Indicates the Query message received by an interface. | - |
| **report** | Indicates the Report message received by an interface. | - |
| **vpn-instance** *instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **all-instance** | Specifies all VPN instance. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

When running the **reset mld control-message counters** command, note the following points:

* If interface port-type port-number is specified, statistics of received MLD messages are deleted from the specified interface.
* If message-type and interface are specified, statistics of a specified type of received MLD messages are deleted from the specified interface.After statistics of MLD messages are deleted, MLD still operates normally.

Example
-------

# Delete statistics of MLD messages from all interfaces in a public network instance.
```
<HUAWEI> reset mld control-message counters

```

# Clear statistics about MLD messages on 100GE1/0/1 in the public network instance.
```
<HUAWEI> reset mld control-message counters interface 100GE 1/0/1

```