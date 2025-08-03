mac-address
===========

mac-address

Function
--------



The **mac-address** command configures a MAC address for an interface.

The **undo mac-address** command restores the default MAC address of an interface.



By default, the MAC address of the interface is the system MAC address.


Format
------

**mac-address** *mac-address*

**undo mac-address**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *mac-address* | Specifies the MAC address of the interface. | The value is in the format of H-H-H, in which each H is a hexadecimal number of 1 to 4 digits, such as 00e0 and fc01. If an H contains fewer than 4 digits, the left-most digits are padded with zeros. For example, e0 is displayed as 00e0. A MAC address cannot be set to all 0s or 1s.  The device supports 128 any unicast MAC addresses, including virtual MAC addresses in the range from 0000-5e00-0100 to 0000-5e00-01ff.  The device supports eight virtual MAC addresses. |



Views
-----

Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To ensure the normal transmission of service data flows, run the mac-address command to configure the MAC address of the interface based on users' requirements.

**Configuration Impact**

After the MAC address of an interface is changed, the device sends gratuitous ARP packets to update the mapping relationship between MAC addresses and interfaces.


Example
-------

# Configure a MAC address for Eth-Trunk 1.
```
<HUAWEI> system-view
[~HUAWEI] interface eth-trunk 1
[*HUAWEI-Eth-Trunk1] undo portswitch
[*HUAWEI-Eth-Trunk1] mac-address 00e0-fc12-3456

```