encapsulation (sub-interface view)
==================================

encapsulation (sub-interface view)

Function
--------

The **encapsulation dot1q-termination** command configures a sub-interface's encapsulation type as dot1q termination.

The **undo encapsulation** command deletes the dot1q termination encapsulation configured for a sub-interface.

By default, no encapsulation type is configured for a sub-interface.



Format
------

**encapsulation dot1q-termination**

**undo encapsulation**



Parameters
----------

None


Views
-----

100ge sub-interface view,10GE sub-interface view,200GE sub-interface view,25GE sub-interface view,400GE sub-interface view,50GE sub-interface view,Eth-Trunk sub-interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

To configure a sub-interface as a dot1q VLAN tag termination sub-interface using the **dot1q termination vid** command, first run the encapsulation dot1q-termination command to configure the sub-interface's encapsulation type as dot1q termination.



Example
-------

# Configure
100GE
1/0/1.1 as a dot1q VLAN tag termination sub-interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1.1
[*HUAWEI-100GE1/0/1.1] encapsulation dot1q-termination

```