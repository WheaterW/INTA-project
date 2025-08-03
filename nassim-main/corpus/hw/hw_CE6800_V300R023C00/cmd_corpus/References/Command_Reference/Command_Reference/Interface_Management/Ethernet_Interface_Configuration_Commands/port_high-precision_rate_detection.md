port high-precision rate detection
==================================

port high-precision rate detection

Function
--------



The **port high-precision rate detection** command enables millisecond-level real-time rate change monitoring on an interface when packet loss occurs on the interface.

The **undo port high-precision rate detection** command restores the default setting.



By default, high-precision interface rate detection is disabled.


Format
------

**port high-precision rate detection interface** { *interface-name* | *interface-type* *interface-number* } **duration** *detect-value*

**undo port high-precision rate detection**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies the name of an interface. | The value is a string of 1 to 63 case-insensitive characters. It cannot contain spaces. |
| *interface-type* | Specifies the type of an interface. | Enumerated type. |
| *interface-number* | Specifies an interface number. | The value is a string of 1 to 63 case-insensitive characters. It cannot contain spaces. |
| **duration** *detect-value* | Duration. | The value is an integer ranging from 1 to 1440, in minutes. |
| **interface** | Indicates an interface name. | - |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

When packet loss occurs on an interface, you can run this command to monitor the rate change in milliseconds on the interface to check whether traffic surges.

**Follow-up Procedure**

After the high-precision rate detection function is enabled on an interface, you can run the **display port high-precision rate detection result** command to view the interface rate.

**Precautions**

When the high-precision rate detection function is enabled on a port, the last detection result is cleared.


Example
-------

# Enable high-precision rate detection on 100GE1/0/1 and set the detection duration to 2 minutes.
```
<HUAWEI> port high-precision rate detection interface 100GE1/0/1 duration 2

```