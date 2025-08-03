dldp compatible-mode local-mac
==============================

dldp compatible-mode local-mac

Function
--------



The **dldp compatible-mode local-mac** command configures a MAC address for sending DLDPDUs in the DLDP-compatible mode.

The **undo dldp compatible-mode local-mac** command restores the default setting.



By default, the MAC address for sending DLDPDUs is the MAC address of a device.


Format
------

**dldp compatible-mode local-mac** *mac-address*

**undo dldp compatible-mode local-mac**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *mac-address* | Specifies a MAC address for sending DLDPDUs in the DLDP-compatible mode. | The value is in the format of H-H-H. Each H indicates one to four hexadecimal digits.  The configured MAC address must have one byte of 0 and cannot be a multicast MAC address. |



Views
-----

Layer 2 100GE interface view,100GE interface view,Layer 2 10GE interface view,10GE interface view,Layer 2 200GE interface view,200GE interface view,25GE-L2 view,25GE interface view,400GE-L2 view,400GE interface view,Layer 2 50GE interface view,50GE interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In order to allow Huawei devices to communicate with non-Huawei devices, run the dldp compatible-mode local-mac command to configure a MAC address for sending DLDPDUs. The configuration prevents communications interruptions resulted from different MAC addresses carried in DLDPDUs.

**Prerequisites**

The DLDP-compatible mode has been enabled using the **dldp compatible-mode enable** command.

**Configuration Impact**

The MAC address carried in the DLDPDUs sent from a port is the configured MAC address.


Example
-------

# Set the source MAC address of the DLDP packets sent by 100GE 1/0/1 in DLDP compatible mode to 00e0-fc12-3457.
```
<HUAWEI> system-view
[~HUAWEI] dldp enable
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] dldp enable
[~HUAWEI-100GE1/0/1] dldp compatible-mode enable
[*HUAWEI-100GE1/0/1] dldp compatible-mode local-mac 00e0-fc12-3457

```