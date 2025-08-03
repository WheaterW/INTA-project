multicast-nat inbound enable
============================

multicast-nat inbound enable

Function
--------



The **multicast-nat inbound enable** command enables multicast NAT on an inbound interface of multicast streams.

The **undo multicast-nat inbound enable** command disables multicast NAT on an inbound interface of multicast streams.



By default, multicast NAT is disabled on interfaces.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**multicast-nat inbound enable**

**undo multicast-nat inbound enable**


Parameters
----------

None

Views
-----

100GE interface view,25GE interface view,400GE interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Before translating an input multicast stream into output multicast streams with different characteristics (source IP address, destination IP address, and destination port number), you must run the **multicast-nat enable** command to enable multicast NAT globally. Additionally, you must run the multicast-nat inbound enable command to enable multicast NAT on an inbound interface of multicast streams.

**Prerequisites**

Multicast NAT has been globally enabled using the **multicast-nat enable** command.

**Precautions**

* The interface must work in Layer 3 mode.
* The interface cannot be an Eth-Trunk member interface.

Example
-------

# Enable multicast NAT on the inbound interface 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] multicast-nat enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] multicast-nat inbound enable

```