multicast-nat bind-list
=======================

multicast-nat bind-list

Function
--------



The **multicast-nat bind-list** command creates and displays the multicast NAT binding view.

The **undo multicast-nat bind-list** command deletes the multicast NAT binding view and the configurations in the view.



By default, no multicast NAT binding view is created.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**multicast-nat bind-list**

**undo multicast-nat bind-list**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In multicast NAT, to translate an input multicast stream into output multicast streams, you must create a multicast NAT instance. Before binding output multicast streams to a multicast NAT instance, you must run the multicast-nat bind-list command to create and enter the multicast NAT binding view.

**Prerequisites**

Multicast NAT has been globally enabled using the **multicast-nat enable** command.

**Follow-up Procedure**

Run the **multicast-nat outbound** command to bind output multicast streams to the multicast NAT instance.


Example
-------

# Create and display the multicast NAT binding view.
```
<HUAWEI> system-view
[~HUAWEI] multicast-nat enable
[*HUAWEI] multicast-nat bind-list

```