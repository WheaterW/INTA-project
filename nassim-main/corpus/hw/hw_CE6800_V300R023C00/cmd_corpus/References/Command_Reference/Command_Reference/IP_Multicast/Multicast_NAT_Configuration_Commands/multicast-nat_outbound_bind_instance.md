multicast-nat outbound bind instance
====================================

multicast-nat outbound bind instance

Function
--------



The **multicast-nat outbound bind instance** command binds a multicast output flow to a multicast instance.

The **undo multicast-nat outbound bind instance** command unbinds a multicast output flow from a multicast instance.



By default, no output multicast flow is bound to a multicast instance.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**multicast-nat outbound id** *outbound-id* [ **name** *outbound-name* ] **bind** **instance** **id** *instance-id* [ **name** *instance-name* ]

**undo multicast-nat outbound id** *outbound-id* [ **name** *outbound-name* ] **bind** **instance** **id** *instance-id* [ **name** *instance-name* ]

**undo multicast-nat outbound id** *outbound-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **name** *instance-name* | Specifies the name of a multicast NAT instance. | The value is a string of 1 to 127 case-sensitive characters, spaces not supported. |
| **name** *outbound-name* | Specifies the name of an output multicast stream. | The value is a string of 1 to 127 case-sensitive characters, spaces not supported. |
| **id** *outbound-id* | Specifies the ID of an output multicast flow. | The value is an integer ranging from 1 to 16000. |
| **id** *instance-id* | Specifies the ID of a multicast NAT instance. | The value is an integer that ranges from 1 to 2048. |



Views
-----

multicast-nat-bind-list


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In multicast NAT, to translate an input multicast flow into an output multicast stream, you must create a multicast NAT instance. To bind an output multicast flow to a multicast NAT instance, run the multicast nat outbound bind instance command.

**Prerequisites**

Before using this command, run the following commands:

* Run the **multicast-nat enable** command to enable multicast NAT globally.
* Run the **multicast-nat instance** command to configure a multicast NAT instance.
* Run the **multicast-nat outbound** command in the interface view to configure an outbound interface instance.

Example
-------

# Bind a multicast output flow to a multicast instance in the multicast NAT binding view.
```
<HUAWEI> system-view
[~HUAWEI] multicast-nat enable
[*HUAWEI] multicast-nat instance id 1 name stream1
[*HUAWEI-multicast-nat-instance-1] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] multicast-nat outbound id 1 name out1 src-ip 10.0.0.1 dst-ip 225.0.0.1 dst-udp-port 100
[*HUAWEI-100GE1/0/1] quit
[*HUAWEI] multicast-nat bind-list
[*HUAWEI-multicast-nat-bind-list] multicast-nat outbound id 1 name out1 bind instance id 1 name stream1

```