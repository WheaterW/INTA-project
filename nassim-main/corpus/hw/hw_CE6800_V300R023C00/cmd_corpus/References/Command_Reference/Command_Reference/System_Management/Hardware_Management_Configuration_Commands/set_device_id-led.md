set device id-led
=================

set device id-led

Function
--------



The **set device id-led** command sets the status of a device ID indicator.



By default, a device ID indicator is off.


Format
------

**set device id-led** { **off** | **on** } [ **slot** *slotid* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **off** | Specifies that the ID indicator is off. | - |
| **on** | Specifies that the ID indicator is on. | - |
| **slot** *slotid* | Indicates the slot number. | The value is a string of 1 to 49 case-insensitive characters. It cannot contain spaces.  If no slot ID is specified, the configuration takes effect for all slots. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



When users need to locate and repair a device, you can run the set device id-led command to remotely set the status of the device ID indicator.




Example
-------

# Set a specified ID indicator to steady on.
```
<HUAWEI> set device id-led on slot 1
Info: Set slot 1 ID LED success.

```

# Set a specified ID indicator to steady off.
```
<HUAWEI> set device id-led off slot 1
Info: Set slot 1 ID LED success.

```

# Set all ID indicators to steady off.
```
<HUAWEI> set device id-led off
Info: Set slot 1 ID LED success.

```

# Set all ID indicators to steady on.
```
<HUAWEI> set device id-led on
Info: Set slot 1 ID LED success.

```