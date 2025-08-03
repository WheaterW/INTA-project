Importing Time Signals from an External BITS Source
===================================================

On an SMPTE-2059-2 network, time signals are typically imported from an external building integrated timing supply system (BITS) source. Multiple Routers can be configured to import time signals from an external BITS source before the grandmaster clock is determined.

#### Context

The BITS time source can provide reference time signals for devices. If dynamic BMCA selection is used, multiple SMPTE-2059-2 devices can be configured to import BITS signals so that all these SMPTE-2059-2 devices can participate in BMCA selection for the determination of the grandmaster clock. The grandmaster clock provides time signals for the entire SMPTE-2059-2 network, and other network devices use the SMPTE-2059-2 protocol to obtain time synchronization information from the grandmaster clock.

For details about how to import time signals from an external BITS time source, see [Importing Time Signals from an External BITS Time Source](dc_ne_1588v2_cfg_5005.html).