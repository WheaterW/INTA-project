fec mode rs
===========

fec mode rs

Function
--------



The **fec mode rs** command enables the RS-FEC function on an interface.

The **undo fec mode rs** command restores the default FEC configuration on an interface.



By default, the FEC status depends on the medium type and auto-negotiation status.


Format
------

**fec mode rs**

**undo fec mode rs**


Parameters
----------

None

Views
-----

Layer 2 100GE interface view,100GE interface view,Layer 2 200GE interface view,200GE interface view,25GE-L2 view,25GE interface view,400GE-L2 view,400GE interface view,Layer 2 50GE interface view,50GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

RS-FEC is a bit error correction technology that adds correction information to data packets at the transmit end, and corrects bit errors generated during data packet transmission at the receive end based on the correction information. RS-FEC improves the signal quality, but increases the signal transmission delay. You can disable this function based on requirements to reduce the signal transmission delay.You can run the display interface command in any view or the **display this interface** command in the interface view to check whether the FEC function is enabled on an interface based on the Fec field in the command output.

**Prerequisites**

You can run this command on a 25GE or 50GE interface only when the following conditions are met:

* Install a 25GE medium, or run the **device transceiver** command in the interface view or port group view to pre-configure the medium type as 25GBASE-COPPER or 25GBASE-FIBER.
* Auto-negotiation is disabled on the interface.

You can run this command on a 25GE interface split from a 100GE interface only when the following conditions are met:

* A QSFP28 optical module and an MPO-4\*DLC fiber or a 1-to-4 high-speed cable have been installed, or the **device transceiver** command has been run in the interface view or port group view to pre-configure the medium type as 100GBASE-FIBER or 100GBASE-COPPER.
* Auto-negotiation is disabled on the interface.

You can run this command on a 50GE interface split from a 100GE interface only when the following conditions are met:

* Install a QSFP28 optical module or high-speed cable, or run the **device transceiver** command in the interface view or port group view to pre-configure the medium type as 100GBASE-FIBER or 100GBASE-COPPER.
* Auto-negotiation is disabled on the interface.

You can run this command on a 100GE interface only when the following conditions are met:

* Install a QSFP28 50G high-speed cable, or run the **device transceiver** command in the interface view or port group view to pre-configure the medium type as QSFP28\_50GBASE\_COPPER.
* Auto-negotiation is disabled on the interface.

**Precautions**

When interfaces are connected using 25GE media, you are advised to enable FEC on both ends of the link to reduce the transmission bit error rate of the physical link. Otherwise, error packets may be generated.If the RS-FEC function is enabled at one end, the RS-FEC function must also be enabled at the other end to ensure that the RS-FEC status at both ends of the link is consistent.The loopback internal and **fec mode** commands cannot be used together.


Example
-------

# Enable the RS-FEC function on 100GE 1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] fec mode rs
Info: Set the same config on the peer end.

```