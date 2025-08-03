subinterface trap updown disable
================================

subinterface trap updown disable

Function
--------



The **subinterface trap updown disable** command disables LinkDown alarm generation on a Layer 2 or Layer 3 sub-interface.

The **undo subinterface trap updown disable** command enables LinkDown alarm generation on a Layer 2 or Layer 3 sub-interface.



By default, LinkDown alarm generation is enabled on a Layer 2 or Layer 3 sub-interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**subinterface trap updown disable**

**undo subinterface trap updown disable**


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

By default, the LinkDown alarm (Trap OID: 1.3.6.1.6.1.1.5.3) is generated when the status of a Layer 2 or Layer 3 sub-interface changes. If a large number of Layer 2 or Layer 3 sub-interfaces exist on a device, the LinkDown alarm is reported on the sub-interfaces at the interval of several minutes. In this case, an NMS has to process a large number of interface status change alarms, which overloads the NMS. To resolve this problem, run the **subinterface trap updown disable** command to disable LinkDown alarm generation on the Layer 2 or Layer 3 sub-interfaces as needed.

**Configuration Impact**

After this command is run, the LinkDown alarm is no longer generated on any of the device's Layer 2 or Layer 3 sub-interfaces in case of a status change. Therefore, exercise caution when running this command.


Example
-------

# Disable LinkDown alarm generation on sub-interfaces.
```
<HUAWEI> system-view
[~HUAWEI] subinterface trap updown disable

```