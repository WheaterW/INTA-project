mac-address bpdu
================

mac-address bpdu

Function
--------



The **mac-address bpdu** command configures a BPDU MAC address.

The **undo mac-address bpdu** command deletes the configured or default BPDU MAC address.



By default, the device has the following BPDU MAC addresses:

0180-c200-008a ffff-ffff-ffff

0180-c200-8585 ffff-ffff-ffff

010f-e200-0001 ffff-ffff-ffff

0180-c200-0000 ffff-ffff-ffff

0180-c200-0001 ffff-ffff-ffff

0180-c200-0002 ffff-ffff-ffff

0180-c200-0003 ffff-ffff-ffff

0180-c200-0004 ffff-ffff-ffff

0180-c200-0005 ffff-ffff-ffff

0180-c200-0006 ffff-ffff-ffff

0180-c200-0007 ffff-ffff-ffff

0180-c200-0008 ffff-ffff-ffff

0180-c200-0009 ffff-ffff-ffff

0180-c200-000a ffff-ffff-ffff

0180-c200-000b ffff-ffff-ffff

0180-c200-000c ffff-ffff-ffff

0180-c200-000d ffff-ffff-ffff

0180-c200-000e ffff-ffff-ffff

0180-c200-000f ffff-ffff-ffff

0180-c200-0010 ffff-ffff-ffff

0180-c200-0020 ffff-ffff-fff0




Format
------

**mac-address bpdu** *mac-address* [ *mac-address-mask* ]

**undo mac-address bpdu** *mac-address* [ *mac-address-mask* ]

**undo mac-address bpdu**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *mac-address* | Specifies a MAC address. | The value is a hexadecimal number in the format of H-H-H. H is a 4-bit hexadecimal number, such as 00e0 or fc01. If an H contains fewer than 4 digits, the left-most digits are padded with zeros. For example, e0 is displayed as 00e0. The MAC address cannot be set to FFFF-FFFF-FFFF.  The first digit must be 0 and the second digit must be an odd number. |
| *mac-address-mask* | Specifies the mask of a MAC address. | The value is a hexadecimal number in the format of H-H-H. H is a 4-bit hexadecimal number, such as 00e0 or fc01. If an H contains fewer than 4 digits, the left-most digits are padded with zeros. For example, e0 is displayed as 00e0. The MAC address cannot be set to FFFF-FFFF-FFFF.  The binary value converted from the MAC address mask must consist of consecutive 1s and 0s, and the first digit cannot be 0. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, the device does not perform Layer 2 forwarding for BPDUs with the default configuration. When proprietary protocol packets of devices from other vendors need to be processed as BPDUs, you can run this command to configure the MAC addresses of these packets as BPDU MAC addresses. In this way, the device discards these packets with BPDU MAC addresses.The BPDU MAC addresses corresponding to common protocol packet types are as follows:

* STP/RSTP/MSTP: 0180-C200-0000, used to send BPDUs
* LACP: 0180-C200-0002, used to send LACPDUs
* LLDP: 0180-C200-000e, used to send LLDPDUs


Example
-------

# Configure a BPDU MAC address.
```
<HUAWEI> system-view
[~HUAWEI] mac-address bpdu 0111-1234-5678

```