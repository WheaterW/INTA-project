igmp snooping static-router-port
================================

igmp snooping static-router-port

Function
--------



The **igmp snooping static-router-port** command configures current sub-interface as a static router port.

The **undo igmp snooping static-router-port** command restores the default configuration.



By default, a dynamic router port is used.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**igmp snooping static-router-port**

**igmp snooping static-router-port dot1q vid** *vidValue*

**igmp snooping static-router-port qinq pe-vid** *pe-vidValue* **ce-vid** *ce-vidValue*

**undo igmp snooping static-router-port** [ **dot1q** **vid** *vidValue* | **qinq** **pe-vid** *pe-vidValue* **ce-vid** *ce-vidValue* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **dot1q** | Enables dot1q encapsulation to allow a Layer 2 sub-interface to receive packets each with one or more tags. | - |
| **vid** *vidValue* | Specifies a range of VLAN IDs for single-tagged packets to be received by a Layer 2 sub-interface. | The value is an integer ranging from 1 to 4094. |
| **qinq** | Enables QinQ encapsulation to allow a Layer 2 sub-interface to receive packets with two or more tags. | - |
| **pe-vid** *pe-vidValue* | Specifies an outer VLAN ID for double-tagged packets to be received by a Layer 2 sub-interface. | The value is an integer ranging from 1 to 4094. |
| **ce-vid** *ce-vidValue* | Specifies a range of inner VLAN IDs for double-tagged packets to be received by a Layer 2 sub-interface. | The value is an integer ranging from 1 to 4094. |



Views
-----

100GE Layer 2 sub-interface view,200GE Layer 2 sub-interface view,400GE Layer 2 sub-interface view,50GE Layer 2 sub-interface view,Eth-Trunk Layer 2 sub-interface view,Layer 2 sub-interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If user hosts need to receive multicast data packets from a port for a long period of time, the igmp snooping static-router-port command can be used to configure the port as a static router port.

**Prerequisites**

Before running this command on a layer 2 sub-interface, check the following conditions have been met:

* IGMP snooping has been configured globally and in a BD.
* The layer 2 sub-interface is bound to only one BD, and this command is run once on the layer 2 sub-interface.
* After the layer 2 sub-interface is configured as a router port in a BD, the layer 2 sub-interface is not configured as a router port in any other BD.

**Configuration Impact**

A static router port does not age. To delete a static router port, you must run the **undo igmp snooping static-router-port** command.If the igmp snooping static-router-port command is run more than once, all configurations take effect.


Example
-------

# Configure 100GE 1/0/1.1 as a static router port in a BD.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] bridge-domain 100
[*HUAWEI-bd100] igmp snooping enable
[*HUAWEI-bd100] quit
[*HUAWEI] interface 100GE1/0/1.1 mode l2
[*HUAWEI-100GE1/0/1.1] portswitch
[*HUAWEI-100GE1/0/1.1] encapsulation untag
[*HUAWEI-100GE1/0/1.1] bridge-domain 100
[*HUAWEI-100GE1/0/1.1] igmp snooping static-router-port

```