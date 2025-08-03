ptp enable
==========

ptp enable

Function
--------

The **ptp enable** command enables 1588v2 on an interface.

The **undo ptp enable** command disables 1588v2 on an interface.

By default, 1588v2 is disabled on an interface.

![](../public_sys-resources/note_3.0-en-us.png)
 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H-48S6CQ, CE6881H-48S6CQ-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.





Format
------

**ptp enable**

**undo ptp enable**



Parameters
----------

None


Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

1588v2 can be enabled in the system and interface views:

* Run the ptp enable (system view) command in the system view to enable 1588v2 on a device. 1588v2 functions then can be configured in the system view.
* Run the ptp enable (interface view) command in the interface view of the device. 1588v2 functions then can be configured in the interface view.

**Precautions**

1588v2 can be enabled on only one interface of an OC device.



Example
-------

# Enable 1588v2 on
100GE
1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] ptp enable

```