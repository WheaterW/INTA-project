radius-attribute disable
========================

radius-attribute disable

Function
--------

The **radius-attribute disable** command disables a RADIUS attribute.

The **undo radius-attribute disable** command enables a disabled RADIUS attribute.

By default, no RADIUS attribute is disabled.



Format
------

**radius-attribute disable** *attribute-name* { **receive** | **send** } \*

**undo radius-attribute disable** [ *attribute-name* ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *attribute-name* | Specifies the name of a RADIUS attribute. | The value is a string of 1 to 64 characters. After the name is entered, the system automatically associates the RADIUS attribute with the name. |
| **receive** | Disables a RADIUS attribute for received packets. | - |
| **send** | Disables a RADIUS attribute for sent packets. | - |




Views
-----

RADIUS server template view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

Generally, a RADIUS server connects to multiple network devices, which can be one vendor's devices or different vendors' devices. If some vendors' devices require the RADIUS server to deliver an attribute to support a specified feature but other vendors' device do not support the delivered attribute, the RADIUS attribute may fail to be parsed.

The device may communicate with RADIUS servers of different vendors. Some RADIUS servers require the device to send some attributes but other RADIUS servers cannot process the attributes. Errors may occur.The radius-attribute disable command disables RADIUS attributes on the device. You can configure the device to ignore incompatible attributes when receiving RADIUS packets to prevent parsing failures. You can also configure the device to disable RADIUS attributes when sending RADIUS packets. When the device sends RADIUS packets, it does not encapsulate the disabled RADIUS attributes in the RADIUS packets.

**Prerequisites**

The RADIUS attribute translation function has been enabled using the **radius-server attribute translate** command.

**Precautions**

Before disabling RADIUS attributes, run the display radius-attribute command to view the RADIUS attributes supported by the device.



Example
-------

# Disable the NAS-Port-Type attribute in sent packets.
```
<HUAWEI> system-view
[~HUAWEI] radius-server template test1
[*HUAWEI-radius-test1] radius-server attribute translate
[*HUAWEI-radius-test1] radius-attribute disable NAS-Port-Type send

```