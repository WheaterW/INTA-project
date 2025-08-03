wavelength-channel
==================

wavelength-channel

Function
--------



The **wavelength-channel** command sets a wavelength for an optical module.

The **undo wavelength**-channel command deletes the wavelength set for an optical module.



By default, the channel number, center frequency, or wavelength for the center wavelength of optical modules is not configured.


Format
------

**wavelength-channel** *channel*

**wavelength-channel frequency** *frequency\_value*

**wavelength-channel wavelength** *wavelength\_value*

**undo wavelength-channel** [ *channel* ]

**undo wavelength-channel frequency** [ *frequency\_value* ]

**undo wavelength-channel wavelength** [ *wavelength\_value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *channel* | Specifies a channel number. | The value is an integer ranging from 1 to 80. |
| **frequency** *frequency\_value* | Specifies a frequency value. | The value is an integer ranging from 0 to 4294967295. |
| **wavelength** *wavelength\_value* | Specifies a wavelength value. | The value is an integer ranging from 0 to 4294967295, in picometers (pm). |



Views
-----

Layer 2 100GE interface view,100GE interface view,Layer 2 10GE interface view,10GE interface view,Layer 2 200GE interface view,200GE interface view,25GE-L2 view,25GE interface view,400GE-L2 view,400GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A wavelength of an optical wave directly determines transmission quality and efficiency of an optical fiber. Setting a wavelength of an optical wave used in optical communication may enable an optical fiber to more flexibly use different transmission modes in different situations. The system has 80 channels, each corresponding to a wavelength. Before setting the center wavelength of a colored optical module, you can run the **display wavelength-map** command to view the mapping between the channel number and center wavelength of the colored optical module, and then run the wavelength-channel <channel> command to set the channel number corresponding to the center wavelength of the colored optical module.

**Precautions**

This command is supported only after colored optical modules are preconfigured or installed in the interfaces.The wavelengths must be the same for optical modules inserted into two connected interfaces.


Example
-------

# Set the wavelength of an optical module to 1536216 pm.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] wavelength-channel wavelength 1536216

```

# Set the frequency of an optical module to 195150000 MHz.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] wavelength-channel frequency 195150000

```

# Set the channel number 2 for the center wavelength of colored optical modules.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] wavelength-channel 2

```