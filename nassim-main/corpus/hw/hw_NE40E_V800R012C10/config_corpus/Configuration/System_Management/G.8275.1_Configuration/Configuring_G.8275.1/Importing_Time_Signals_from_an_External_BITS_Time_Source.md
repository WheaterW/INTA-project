Importing Time Signals from an External BITS Time Source
========================================================

On a G.8275.1 network, time signals are typically imported from an external BITS time source. You can configure multiple Routers to import time signals from an external BITS time source. A master clock can be selected dynamically using the BMCA.

#### Context

For details about how to import time signals from an external BITS time source, see [Importing Time Signals from an External BITS Time Source](dc_ne_1588v2_cfg_5005.html).

![](../../../../public_sys-resources/note_3.0-en-us.png) 

When a device connects to an external BITS source, the configuration needs to be performed on the local device. By default, the clock accuracy value of a BITS source is 0x20. When the default value is used, downstream devices cannot communicate with the local device using the G.8275.1 protocol of the 2014 version. This is because the clock accuracy in this version can only be set to 0x21 or 0xFE. In this scenario, you are advised to set the clock accuracy of a BITS source to 0x21.