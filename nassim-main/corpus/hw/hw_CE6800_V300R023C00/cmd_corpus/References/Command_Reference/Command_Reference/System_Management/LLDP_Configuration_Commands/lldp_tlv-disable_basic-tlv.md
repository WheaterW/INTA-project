lldp tlv-disable basic-tlv
==========================

lldp tlv-disable basic-tlv

Function
--------

The lldp tlv-enable basic-tlv command configures TLVs that cannot be advertised by an interface.

The undo lldp tlv-enable basic-tlv command configures TLVs that can be advertised by an interface.

By default, LLDP advertises all basic TLVs.



Format
------

**lldp tlv-disable basic-tlv** { **all** | **management-address** | **port-description** | **system-capability** | **system-description** | **system-name** }

**undo lldp tlv-disable basic-tlv** { **all** | **management-address** | **port-description** | **system-capability** | **system-description** | **system-name** }



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Indicates all optional TLVs contained in Dot3 TLVs. | - |
| **management-address** | Indicates Management-address TLVs. | - |
| **port-description** | Indicates Port Description TLVs. | - |
| **system-capability** | Indicates System Capabilities TLVs. | - |
| **system-description** | Indicates System Description TLVs. | - |
| **system-name** | Indicates System Name TLVs. | - |
| **basic-tlv** | Indicates types of basic TLVs that can be advertised:   * Management-address TLV. * Port Description TLV. * System Capabilities TLV. * System Description TLV. * System Name TLV. | - |




Views
-----

Management interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

TLVs are the basic information units of Link Layer Discovery Protocol Data Units (LLDPDUs), where T, L, and V indicate the information type, length, and value, respectively. The device encapsulates information such as the main capability, management address, device ID, and interface ID into TLVs, encapsulates the TLVs into LLDPDUs, and then encapsulates the LLDPDUs into LLDP packets to be exchanged with the directly connected neighboring node. During the process of exchanging LLDP packets between devices, the LLDPDU encapsulated in an LLDP packet carries different TLVs as required. A device sends its information and receives the neighbor node's information based on these different TLVs.

TLVs that can be encapsulated into an LLDPDU include basic TLVs, TLVs defined by IEEE 802.1, TLVs defined by IEEE 802.3, and DCBX TLVs.

* Basic TLVs implement basic LLDP functions. Basic TLVs include three mandatory TLVs, which must be encapsulated into LLDPDUs to be advertised. Basic TLVs also include five optional TLVs: management-address, port-description, system-capability, system-description, and system-name.

**Prerequisites**

LLDP has been enabled globally using the lldp enable command in the system view.

**Precautions**

When you configure the type of basic TLVs that cannot be advertised on an interface, if the all parameter is specified, all optional TLVs contained in the basic TLVs are not advertised. If the all parameter is not specified, only one type of optional TLV cannot be advertised on the interface. You can run this command multiple times to disable the interface from advertising multiple types of optional TLVs.



Example
-------

# Disable the management interface from advertising management-address TLVs.
```
<HUAWEI> system-view
[~HUAWEI] lldp enable
[*HUAWEI] interface MEth 0/0/0
[*HUAWEI-MEth0/0/0] lldp tlv-disable basic-tlv management-address

```