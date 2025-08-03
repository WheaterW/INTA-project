encapsulation untag
===================

encapsulation untag

Function
--------



The **encapsulation untag** command enables a Layer 2 sub-interface to receive untagged packets.

The **undo encapsulation untag** command disables a Layer 2 sub-interface from receiving untagged packets.



By default, no encapsulation type is configured on a Layer 2 sub-interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**encapsulation untag**

**undo encapsulation untag**


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

To add packets that do not carry VLAN TAG, run the encapsulation untag command on the sub-interface. Each Layer 2 sub-interface can be configured with only one encapsulation type. If flow encapsulation has been configured on a Layer 2 sub-interface, you must run the **undo encapsulation** command to delete the original encapsulation type before changing the encapsulation type.

**Configuration Impact**

After the encapsulation untag command is run, the main interface cannot forward packets without VLAN tags.After the encapsulation untag configuration is deleted, if VLAN-related configurations exist on the main interface, you need to re-perform the VLAN-related configurations on the main interface to make the configurations take effect.


Example
-------

# Set the encapsulation type of the EVC Layer 2 sub-interface to untagged.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1.1 mode l2
[*HUAWEI-100GE1/0/1.1] encapsulation untag

```