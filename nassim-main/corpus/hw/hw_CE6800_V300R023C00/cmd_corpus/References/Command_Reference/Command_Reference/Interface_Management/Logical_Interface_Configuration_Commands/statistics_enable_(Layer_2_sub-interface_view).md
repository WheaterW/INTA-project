statistics enable (Layer 2 sub-interface view)
==============================================

statistics enable (Layer 2 sub-interface view)

Function
--------

The **statistics enable** command enables traffic statistics collection on a Layer 2 sub-interface.

The **undo statistics enable** command disables traffic statistics collection on a Layer 2 sub-interface.

By default, traffic statistics collection is disabled on a Layer 2 sub-interface.

![](../public_sys-resources/note_3.0-en-us.png)
 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.





Format
------

**statistics enable**

**undo statistics enable**



Parameters
----------

None


Views
-----

100GE Layer 2 sub-interface view,10GE Layer 2 sub-interface view,200GE Layer 2 sub-interface view,25GE Layer 2 sub-interface view,400GE Layer 2 sub-interface view,50GE Layer 2 sub-interface view,Eth-Trunk Layer 2 sub-interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

To check the network status or locate network faults, you can enable traffic statistics collection on a Layer 2 sub-interface to collect traffic statistics on the Layer 2 sub-interface.

You can run the
**display interface** interface-type interface-number.subnumber command in any view or run the
**display this interface** command in the Layer 2 sub-interface view to check the statistics.

**Precautions**

If a message indicating that the service fails to be delivered because of insufficient resources is displayed on the switch when this function is configured, you are advised to configure MQC-based traffic statistics collection.

Traffic statistics collection on a Layer 2 sub-interface does not differentiate packet types. Only the total number of packets can be collected.

Example
-------

# Enable traffic statistics collection on a Layer 2 sub-interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1.1 mode l2
[~HUAWEI-100GE1/0/1.1] statistics enable

```