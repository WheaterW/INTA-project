iqcn enable (Interface View)
============================

iqcn enable (Interface View)

Function
--------



The **iqcn enable** command enables the iQCN function in the interface view.

The **undo iqcn enable** command disables the iQCN function in the interface view.



By default, the iQCN function is disabled on an interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**iqcn enable**

**undo iqcn enable**


Parameters
----------

None

Views
-----

100GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After the iQCN function is enabled globally, you need to enable the iQCN function in the interface view to implement the iQCN function.

**Precautions**

* You are advised to configure the iQCN function on downlink interfaces of an access device.
* The iQCN function cannot be configured on interfaces in a PFC uplink interface group or on a peer-link interface.
* If an Eth-Trunk interface is used to set up an M-LAG, iQCN can be enabled on only one member interface of the Eth-Trunk interface.
* iQCN can be enabled on a maximum of two member interfaces of an Eth-Trunk interface.

Example
-------

# Enable the iQCN function on interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] iqcn enable

```