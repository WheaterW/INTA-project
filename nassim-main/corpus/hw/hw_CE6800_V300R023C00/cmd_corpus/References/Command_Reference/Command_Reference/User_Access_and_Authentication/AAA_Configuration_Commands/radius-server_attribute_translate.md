radius-server attribute translate
=================================

radius-server attribute translate

Function
--------

The **radius-server attribute translate** command enables RADIUS attribute translation.

The **undo radius-server attribute translate** command disables RADIUS attribute translation.

By default, RADIUS attribute translation is disabled.



Format
------

**radius-server attribute translate**

**undo radius-server attribute translate**



Parameters
----------

None


Views
-----

RADIUS server template view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

Currently, RADIUS servers of different vendors may support different RADIUS attributes and have vendor-specific RADIUS attributes. To communicate with different RADIUS servers, the device provides the RADIUS attribute translation function. After RADIUS attribute translation is enabled, the device can translate RADIUS attributes when sending or receiving packets.

**Follow-up Procedure**

After RADIUS attribute translation is enabled, perform either of the following operations to make the function to take effect:

* Run the **radius-attribute translate** command to specify the RADIUS attributes that you want to translate.
* Run the **radius-attribute disable** command to specify the RADIUS attributes that you do not want to translate.


Example
-------

# Enable RADIUS attribute translation.
```
<HUAWEI> system-view
[~HUAWEI] radius-server template test1
[*HUAWEI-radius-test1] radius-server attribute translate

```