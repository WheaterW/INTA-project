qos micro-burst detection enable(Interface View)
================================================

qos micro-burst detection enable(Interface View)

Function
--------

The **qos micro-burst detection enable** command enables microburst detection.

The **undo qos micro-burst detection enable** command disables microburst detection.

By default, microburst detection is disabled on interfaces.

![](../public_sys-resources/note_3.0-en-us.png)
 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.





Format
------

**qos micro-burst detection enable**

**undo qos micro-burst detection enable**



Parameters
----------

None


Views
-----

100GE interface view,10GE interface view,25GE interface view,400GE interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

To detect microbursts on an outbound interface, you must enable microburst detection on a switch and interfaces. This helps locate packet loss caused by microbursts.

In default microburst detection mode, the packet sampling interval is 5 ms. In enhanced microburst detection mode, the packet sampling interval is 1 ms.

**Precautions**

Before enabling microburst detection on an interface, you must enable this function on the slot where the interface resides.



Example
-------

# enable microburst detection on
100GE
1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] qos micro-burst detection enable

```