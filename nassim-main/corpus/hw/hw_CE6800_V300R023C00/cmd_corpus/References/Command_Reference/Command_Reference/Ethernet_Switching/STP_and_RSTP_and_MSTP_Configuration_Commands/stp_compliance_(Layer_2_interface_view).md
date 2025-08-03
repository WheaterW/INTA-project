stp compliance (Layer 2 interface view)
=======================================

stp compliance (Layer 2 interface view)

Function
--------



The **stp compliance** command configures a format for sent and received Multiple Spanning Tree Protocol (MSTP) BPDUs.

The **undo stp compliance** command restores the default format of sent and received MST BPDUs.



By default, the format of sent and received MST BPDUs is auto.


Format
------

**stp compliance** { **auto** | **dot1s** | **legacy** }

**undo stp compliance**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **auto** | Indicates that the MST BPDU format is self-adaptive. | - |
| **dot1s** | Indicates that the MST BPDU format is standard IEEE 802.1s. | - |
| **legacy** | Indicates that the MST BPDU format is proprietary. | - |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



MST BPDUs have two formats: dot1s (IEEE 802.1s standard) and legacy (proprietary). To facilitate device communication, run the stp compliance command to set an MST BPDU format for a local device based on the format of MST BPDUs from the remote device.To allow a port to automatically accommodate to the format of MST BPDUs sent by a remote device, configure the auto format.



**Precautions**



If you configure different MST BPDU formats on the same interface in the interface view, the latest configuration overrides the previous one.




Example
-------

# Set the MST BPDU format to IEEE 802.1s.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] portswitch
[~HUAWEI-100GE1/0/1] stp compliance dot1s

```