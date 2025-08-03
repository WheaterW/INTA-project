fec mode none
=============

fec mode none

Function
--------



The **fec mode none** command disables the Base-R FEC or RS-FEC function on an interface.

The **undo fec mode none** command restores the default FEC configuration on an interface.

The **undo fec mode** command restores the default FEC mode on an interface.



By default, the FEC status depends on the medium type and auto-negotiation status.


Format
------

**fec mode none**

**undo fec mode none**

**undo fec mode**


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

You can run the display interface command in any view or the **display this interface** command in the interface view to check whether the FEC function is enabled on an interface based on the Fec field in the command output.

**Prerequisites**

You can run this command on a 25GE or 50GE interface only when the following conditions are met:

* Install a 25GE medium, or run the **device transceiver** command in the interface view or port group view to pre-configure the medium type as 25GBASE-COPPER or 25GBASE-FIBER.
* Auto-negotiation is disabled on the interface.

You can run this command on 400GE interfaces, 200GE interfaces, 25GE interfaces split from 100GE interfaces, and 50GE interfaces split from 100GE interfaces only when the following conditions are met:

* Install a 100GE medium, or run the **device transceiver** command in the interface view or port group view to pre-configure the medium type as 100GBASE-FIBER or 100GBASE-COPPER.
* Auto-negotiation is disabled on the interface.

You can run this command on a 100GE interface only when the following conditions are met:

* Install a 100GE medium or QSFP28 50GE high-speed cable, or run the **device transceiver** command in the interface view or port group view, the medium type is pre-configured as 100GBASE-FIBER, 100GBASE-COPPER, or QSFP28-50GBASE-COPPER.
* Auto-negotiation is disabled on the interface.

**Precautions**

The loopback internal and **fec mode** commands cannot be used together.


Example
-------

# Disable the FEC function on 100GE 1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] fec mode none

```