multicast-nat instance
======================

multicast-nat instance

Function
--------



The **multicast-nat instance** command creates a multicast NAT instance and displays the multicast NAT instance view.

The **undo multicast-nat instance** command deletes a multicast NAT instance.



By default, no multicast NAT instance is created.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**multicast-nat instance id** *instance-id* [ **name** *instance-name* ]

**undo multicast-nat instance id** *instance-id* [ **name** *instance-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **name** *instance-name* | Specifies the name of a multicast NAT instance. | The value is a string of 1 to 127 case-sensitive characters, spaces not supported. |
| **id** *instance-id* | Specifies the ID of a multicast NAT instance. | The value is an integer that ranges from 1 to 2048. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In multicast NAT, to translate an input multicast flow into an output multicast flow, you must create a multicast NAT instance. To simplify the multicast NAT configuration, run the multicast-nat instance command to create a multicast NAT instance so that input multicast flows can be associated with the multicast NAT instance.

**Prerequisites**

Multicast NAT has been enabled globally using the **multicast-nat enable** command.

**Follow-up Procedure**

Run the **multicast-nat bind** command in the traffic behavior view to bind the traffic behavior to a multicast NAT instance.After a traffic policy is applied to the inbound interface of multicast traffic, input multicast flows are associated with the multicast NAT instance.


Example
-------

# Create a multicast NAT instance.
```
<HUAWEI> system-view
[~HUAWEI] multicast-nat enable
[*HUAWEI] multicast-nat instance id 1 name stream1

```