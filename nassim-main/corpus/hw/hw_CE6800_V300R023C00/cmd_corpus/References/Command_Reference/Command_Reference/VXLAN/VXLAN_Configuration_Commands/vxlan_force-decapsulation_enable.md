vxlan force-decapsulation enable
================================

vxlan force-decapsulation enable

Function
--------



The **vxlan force-decapsulation enable** command enables forcible VXLAN decapsulation on an interface.

The **undo vxlan force-decapsulation enable** command restores the default configuration.



By default, forcible VXLAN decapsulation is disabled on an interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**vxlan force-decapsulation enable**

**undo vxlan force-decapsulation enable**


Parameters
----------

None

Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If a device needs to send VXLAN packets to the analyzer, you can run this command to enable forcible VXLAN decapsulation on the inbound interface of VXLAN packets to reduce the load of the analyzer. This ensures that the analyzer receives only the original packets.


Example
-------

# Enable forcible VXLAN decapsulation on an interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] vxlan force-decapsulation enable

```