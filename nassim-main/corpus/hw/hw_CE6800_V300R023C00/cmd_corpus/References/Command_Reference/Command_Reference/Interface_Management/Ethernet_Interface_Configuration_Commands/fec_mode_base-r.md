fec mode base-r
===============

fec mode base-r

Function
--------



The **fec mode base-r** command enables the Base-R FEC function on an interface.

The **undo fec mode base-r** command restores the default FEC function on an interface.



By default, the Base-R FEC status depends on the medium type and auto-negotiation status.


Format
------

**fec mode base-r**

**undo fec mode base-r**


Parameters
----------

None

Views
-----

Layer 2 100GE interface view,100GE interface view,25GE-L2 view,25GE interface view,400GE-L2 view,400GE interface view,Layer 2 50GE interface view,50GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Base-R FEC is a bit error correction mode. In this mode, error correction information is added to data packets at the transmit end, and the error correction information is used at the receive end to correct bit errors generated during data packet transmission. You can enable the Base-R FEC function to improve signal quality.You can run the display interface command in any view or the **display this interface** command in the interface view to check the FEC status on the interface.When two interfaces are connected, ensure that the FEC status on both ends of the link is the same. One end must be Base-R FEC, and the other end must also be Base-R FEC.

**Prerequisites**

You can run this command on a 25GE or 50GE interface only when the following conditions are met:

* Install a 25GE medium, or run the **device transceiver** command in the interface view or port group view to pre-configure the medium type as 25GBASE-COPPER or 25GBASE-FIBER.
* Auto-negotiation is disabled on the interface.

You can run this command on a 25GE interface split from a 100GE interface only when the following conditions are met:

* A QSFP28 optical module and an MPO-4\*DLC fiber or a 1-to-4 high-speed cable have been installed, or the **device transceiver** command has been run in the interface view or port group view to pre-configure the medium type as 100GBASE-FIBER or 100GBASE-COPPER.
* Auto-negotiation is disabled on the interface.
* A 25GE interfaces split from the 100GE interface on the CE8855, CE8851-32CQ4BQ, CE6885-SAN, CE6885, CE6885-T, CE6885-LL, CE6863E-48S8CQ and CE6855-48XS8CQ do not support the Base-R FEC function.

You can run this command on a 50GE interface split from a 100GE interface only when the following conditions are met:

* Install a QSFP28 optical module or high-speed cable, or run the **device transceiver** command in the interface view or port group view to pre-configure the medium type as 100GBASE-FIBER or 100GBASE-COPPER.
* Auto-negotiation is disabled on the interface.

You can run this command on a 100GE interface only when the following conditions are met:

* Install a QSFP28 50G high-speed cable, or run the **device transceiver** command in the interface view or port group view to pre-configure the medium type as QSFP28\_50GBASE\_COPPER.
* Auto-negotiation is disabled on the interface.
* A 100GE interface on the CE8855, CE8851-32CQ4BQ, CE6885-SAN, CE6885, CE6885-T, CE6885-LL, CE6863E-48S8CQ and CE6855-48XS8CQ do not support the Base-R FEC function.

**Precautions**

When interfaces are connected, you are advised to enable FEC on both ends of a link to reduce the transmission bit error rate of the physical link. Otherwise, error packets may be generated.If the Base-R FEC function is enabled at one end, the Base-R FEC function must also be enabled at the other end to ensure that the Base-R FEC status at both ends of the link is the same.The loopback internal and **fec mode** commands cannot be used together.


Example
-------

# Enable the Base-R FEC function on 25GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 25ge 1/0/1
[~HUAWEI-25GE1/0/1] fec mode base-r

```