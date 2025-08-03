bridge-domain (Layer 2 sub interface view)
==========================================

bridge-domain (Layer 2 sub interface view)

Function
--------



The **bridge-domain** command adds an EVC Layer 2 sub-interface to a bridge domain.

The **undo bridge-domain** command removes an EVC Layer 2 sub-interface from a bridge domain.



By default, no EVC Layer 2 sub-interface is added to a bridge domain.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**bridge-domain** *bd-id*

**undo bridge-domain**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **bridge-domain** *bd-id* | Specifies a BD ID. | The bd-id value is an integer ranging from 1 to 16777215. |



Views
-----

100GE Layer 2 sub-interface view,200GE Layer 2 sub-interface view,400GE Layer 2 sub-interface view,50GE Layer 2 sub-interface view,Eth-Trunk Layer 2 sub-interface view,Layer 2 sub-interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After a BD is created, run the **bridge-domain** command in the Layer 2 Ethernet interface view to add an EVC Layer 2 sub-interface to the BD so that service packets can be forwarded in the BD.

**Prerequisites**

To run the **bridge-domain** command in the EVC Layer 2 sub-interface view, perform the following steps:

1. A BD has been created using the bridge-domain <bd-id> command in the system view.
2. An EVC Layer 2 sub-interface has been created using the interface <interface-type interface-number.subnum> mode l2 command in the system view.

Example
-------

# Add an EVC Layer 2 sub-interface to BD 10.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain 10
[*HUAWEI-bd10] quit
[*HUAWEI] interface 100GE1/0/1.1 mode l2
[*HUAWEI-100GE1/0/1.1] bridge-domain 10

```