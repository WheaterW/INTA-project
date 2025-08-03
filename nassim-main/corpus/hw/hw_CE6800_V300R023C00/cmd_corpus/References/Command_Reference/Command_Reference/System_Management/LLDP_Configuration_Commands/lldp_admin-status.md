lldp admin-status
=================

lldp admin-status

Function
--------



The **lldp admin-status** command configures the Link Layer Discovery Protocol (LLDP) working mode for an interface, or enables LLDP and configures an LLDP working mode for an LLDP-disabled interface.

The **undo lldp admin-status** command restores the default LLDP working mode for an interface.



By default, the LLDP working mode of a main interface is Tx/Rx, meaning that the interface both sends and receives LLDP packets.


Format
------

**lldp admin-status** { **tx** | **rx** | **txrx** }

**undo lldp admin-status**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **tx** | Indicates the LLDP TX mode, meaning that an interface only sends LLDP packets. | - |
| **rx** | Indicates the LLDP RX mode, meaning that an interface only receives LLDP packets. | - |
| **txrx** | Indicates the LLDP TX/RX mode, meaning that an interface both sends and receives LLDP packets. | - |



Views
-----

Layer 2 100GE interface view,100GE interface view,Layer 2 10GE interface view,10GE interface view,Layer 2 200GE interface view,200GE interface view,25GE-L2 view,25GE interface view,400GE-L2 view,400GE interface view,Layer 2 50GE interface view,50GE interface view,Layer 2 GE interface view,Interface group view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After LLDP is enabled globally, perform either of the following operations:

* If LLDP is enabled on an interface, run the lldp admin-status command to configure an LLDP working mode for the interface.
* If LLDP is disabled on a main interface, run the lldp admin-status command to enable LLDP and configure an LLDP working mode for the interface. The LLDP working mode can be configured on a sub-interface only after LLDP is enabled on the sub-interface.This configuration allows the interface to work only in a specified mode, reducing the number of LLDP packets exchanged on the network. Therefore, the system load is reduced, and other services are not affected.

**Prerequisites**



LLDP has been enabled globally using the lldp enable command in the system view.




Example
-------

# Configure the LLDP working mode TX on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] lldp enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] lldp admin-status tx

```