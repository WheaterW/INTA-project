port-isolate l3 enable
======================

port-isolate l3 enable

Function
--------

The **port-isolate l3 enable** command enables Layer 3 port isolation.

The **undo port-isolate l3 enable** command disables Layer 3 port isolation.

By default, Layer 3 port isolation is disabled.



Format
------

**port-isolate l3 enable**

**undo port-isolate l3 enable**



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

During routing protocol convergence, the outbound and inbound interfaces of some Layer 3 traffic are the same, namely, a loop occurs temporarily. After Layer 3 port isolation is configured, Layer 3 forwarding traffic whose outbound and inbound interfaces are the same is discarded on the outbound interface to prevent the loop. After Layer 3 port isolation is enabled, only Layer 3 traffic is isolated.

**Prerequisites**

The working mode of the interface has been switched to Layer 3 using the **undo portswitch** command.



Example
-------

# Configure Layer 3 port isolation on
100GE
1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] port-isolate l3 enable

```