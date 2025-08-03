rewrite (Layer 2 sub-interface view)
====================================

rewrite (Layer 2 sub-interface view)

Function
--------



The **rewrite** command configures a traffic behavior on an EVC Layer 2 sub-interface.

The **undo rewrite** command restores the default configuration.



By default, a Layer 2 sub-interface with the encapsulation type being QinQ is enabled to transparently transmit received packets.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**rewrite pop double**

**undo rewrite** [ **pop** **double** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **double** | Enables an EVC Layer 2 sub-interface to remove double tags from packets after receiving them. | - |
| **pop** | Remove one or more specified VLAN tags. | - |



Views
-----

100GE Layer 2 sub-interface view,200GE Layer 2 sub-interface view,400GE Layer 2 sub-interface view,50GE Layer 2 sub-interface view,Eth-Trunk Layer 2 sub-interface view,Layer 2 sub-interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



In the EVC model, if a Layer 2 sub-interface with QinQ encapsulation is configured as a service access point, the Layer 2 sub-interface needs to remove double VLAN tags from data packets. To enable a Layer 2 sub-interface in QinQ encapsulation mode to remove double VLAN tags from received packets, run the **rewrite pop double** command.



**Prerequisites**

The following conditions have been met:The Layer 2 sub-interface is not added to a bridge domain

**Configuration Impact**

After the **rewrite pop double** command is run successfully, the VLAN tag operation on packets is as follows:

* For incoming packets, the tags are removed and forwarded at Layer 2.
* For outgoing packets, the corresponding VLAN information is added to the packets before they are forwarded.

**Precautions**

A maximum of one traffic behavior can be specified on each EVC Layer 2 sub-interface. If a traffic behavior has been configured on an EVC Layer 2 sub-interface, perform the following operations:

* Run the **undo rewrite** command to delete the existing traffic behavior.
* Run the **undo bridge-domain** command to remove the EVC Layer 2 sub-interface from the existing bridge domain.


Example
-------

# Enable 100GE 1/0/1.1 to remove double tags from received packets.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1.1 mode l2
[*HUAWEI-100GE1/0/1.1] rewrite pop double

```