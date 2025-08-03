lldp tlv-disable
================

lldp tlv-disable

Function
--------



The **lldp tlv-disable** command configures the types of TLVs that are not allowed to be advertised on an interface.

The **undo lldp tlv-disable** command configures the types of TLVs that can be advertised on an interface.



By default, LLDP advertises basic, dot1, and dot3 TLVs.

The Protocol Identity TLV of the dot1 type is not advertised.




Format
------

**lldp tlv-disable** { { **basic-tlv** { **all** | **management-address** | **port-description** | **system-capability** | **system-description** | **system-name** } } | { **dot1-tlv** { **all** | **port-vlan-id** | **protocol-vlan-id** [ *vlan-id* ] | **vlan-name** [ *vlan-id* ] } } | { **dot3-tlv** { **all** | **link-aggregation** | **mac-physic** | **max-frame-size** } } }

**undo lldp tlv-disable** { { **basic-tlv** { **all** | **management-address** | **port-description** | **system-capability** | **system-description** | **system-name** } } | { **dot1-tlv** { **all** | **port-vlan-id** | **protocol-vlan-id** [ *vlan-id* ] | **vlan-name** [ *vlan-id* ] } } | { **dot3-tlv** { **all** | **link-aggregation** | **mac-physic** | **max-frame-size** } } }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **basic-tlv** | Indicates types of basic TLVs. | - |
| **all** | Indicates all 802.1 TLVs. | - |
| **all** | Indicates all 802.3 TLVs. | - |
| **all** | Indicates all basic TLVs. | - |
| **management-address** | Indicates Management-address TLVs. | - |
| **port-description** | Indicates Port Description TLVs. | - |
| **system-capability** | Indicates System Capabilities TLVs. | - |
| **system-description** | Indicates System Description TLVs. | - |
| **system-name** | Indicates System Name TLVs. | - |
| **dot1-tlv** | Indicates TLVs defined by IEEE 802.1. | - |
| **port-vlan-id** | Indicates Port VLAN TLVs. | - |
| **protocol-vlan-id** | Indicates Port and Protocol VLAN ID TLVs. | - |
| *vlan-id* | Specifies the VLAN ID carried in advertised VLAN Name TLVs.  If you do not specify this parameter, the device uses the smallest VLAN ID to which the interface that advertises VLAN Name TLVs belongs. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **vlan-name** | Indicates VLAN Name TLVs. | - |
| **dot3-tlv** | Indicates TLVs defined by IEEE 802.3. | - |
| **link-aggregation** | Indicates Link Aggregation TLVs. | - |
| **mac-physic** | Indicates MAC/PHY Configuration/Status TLVs. | - |
| **max-frame-size** | Indicates Maximum Frame Size TLVs. | - |



Views
-----

Layer 2 100GE interface view,100GE interface view,Layer 2 10GE interface view,10GE interface view,Layer 2 200GE interface view,200GE interface view,25GE-L2 view,25GE interface view,400GE-L2 view,400GE interface view,Layer 2 50GE interface view,50GE interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

TLVs are the basic information units of Link Layer Discovery Protocol Data Units (LLDPDUs), where T, L, and V indicate the information type, length, and value, respectively. The device encapsulates information such as the main capability, management address, device ID, and interface ID into TLVs, encapsulates the TLVs into LLDPDUs, and then encapsulates the LLDPDUs into LLDP packets to be exchanged with the directly connected neighboring node. During the process of exchanging LLDP packets between devices, the LLDPDU encapsulated in an LLDP packet carries different TLVs as required. A device sends its information and receives the neighbor node's information based on these different TLVs.TLVs that can be encapsulated into an LLDPDU include basic TLVs, TLVs defined by IEEE 802.1, TLVs defined by IEEE 802.3, and DCBX TLVs.

* Basic TLVs implement basic LLDP functions. Basic TLVs include three mandatory TLVs, which must be encapsulated into LLDPDUs to be advertised. Basic TLVs also include five optional TLVs: management-address, port-description, system-capability, system-description, and system-name.
* TLVs defined by IEEE 802.1, TLVs defined by IEEE 802.3, and DCBX TLVs are used to enhance the LLDP function. These TLVs are optional. You can determine whether to encapsulate them into LLDPDUs for advertisement as needed.

**Prerequisites**

LLDP has been enabled globally using the lldp enable command in the system view.

**Precautions**

When you disable an interface from advertising basic TLVs, TLVs defined by IEEE 802.1, and TLVs defined by IEEE 802.3, if the all parameter is specified, all optional TLVs contained in the TLVs are not advertised. If the all parameter is not specified, only one type of optional TLVs cannot be advertised on the interface. You can run this command multiple times to disable the interface from advertising multiple types of optional TLVs.If you want to allow the advertisement of Protocol Identity TLVs, run the **lldp tlv-enable** command.If you want to disable the advertisement of the mac-physic TLVs in dot3 TLVs, run the undo lldp tlv-enable med-tlv capability command.


Example
-------

# Configure an interface not to advertise the optional Link Aggregation TLV defined in IEEE 802.3.
```
<HUAWEI> system-view
[~HUAWEI] lldp enable
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] lldp tlv-disable dot3-tlv link-aggregation

```