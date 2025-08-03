mac-address notification
========================

mac-address notification

Function
--------



The **mac-address notification** command enables the trap function for MAC address learning or aging.

The **undo mac-address notification** command disables the trap function for MAC address learning or aging.



By default, the trap function for MAC address learning or aging is disabled.


Format
------

**mac-address notification** { **all** | **learning** | **aging** }

**undo mac-address notification** { **learning** | **aging** | **all** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Enables the trap function for MAC address learning and aging. | - |
| **learning** | Enables the trap function for MAC address learning. | - |
| **aging** | Enables the trap function for MAC address aging. | - |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To learn MAC address change in a timely manner, run the mac-address notification command to enable the trap function for MAC address learning or aging.


Example
-------

# Enable the trap function for MAC address learning on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] portswtich
[~HUAWEI-100GE1/0/1] mac-address notification learning

```