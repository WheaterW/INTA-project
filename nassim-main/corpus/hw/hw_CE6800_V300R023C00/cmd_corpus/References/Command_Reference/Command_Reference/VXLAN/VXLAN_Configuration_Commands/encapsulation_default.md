encapsulation default
=====================

encapsulation default

Function
--------



The **encapsulation default** command configures a Layer 2 sub-interface to receive packets with any encapsulation type by default.

The **undo encapsulation default** command disables a Layer 2 sub-interface from receiving packets with any encapsulation type by default.



By default, no encapsulation type is specified on an EVC Layer 2 sub-interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**encapsulation default**

**undo encapsulation default**


Parameters
----------

None

Views
-----

100GE Layer 2 sub-interface view,200GE Layer 2 sub-interface view,400GE Layer 2 sub-interface view,50GE Layer 2 sub-interface view,Eth-Trunk Layer 2 sub-interface view,Layer 2 sub-interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A Layer 2 Ethernet can transmit untagged, single-tagged, and double-tagged packets. To enable an EVC Layer 2 sub-interface to transmit different types of packets, run the flow-encapsulation command to configure an encapsulation type for the EVC Layer 2 sub-interface. The **encapsulation default** command configures a Layer 2 sub-interface to receive packets with any encapsulation type by default. When packets cannot meet the requirements of other sub-interfaces, the packets are sent to the Layer 2 sub-interface.

**Precautions**

* Each EVC Layer 2 sub-interface can be configured with only one encapsulation type. If traffic encapsulation has been configured on an EVC Layer 2 sub-interface and you want to change the encapsulation type, run the **undo encapsulation** command to delete the original encapsulation type.
* After the **encapsulation default** command is run, the VLAN configured for the main interface does not take effect. To make the VLAN configuration take effect on an EVC Layer 2 sub-interface, clear the encapsulation configuration on the EVC Layer 2 sub-interface.


Example
-------

# Enable the encapsulation type of the EVC Layer 2 sub-interface to default.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1.1 mode l2
[*HUAWEI-100GE1/0/1.1] encapsulation default

```