lldp tlv-enable dot1-tlv (Interface view)
=========================================

lldp tlv-enable dot1-tlv (Interface view)

Function
--------



The **lldp tlv-enable dot1-tlv** command is used to configure the IEEE 802.1-defined TLV (Type Length Value) type allowed to be published on the interface.

The **undo lldp tlv-enable dot1-tlv** command is used to configure IEEE 802.1-defined TLV types that are prohibited from publishing on the interface.



An interface by default can advertise all TLVs except Protocol Identity TLVs.


Format
------

**lldp tlv-enable dot1-tlv** { **protocol-vlan-id** *vlan-id* | **vlan-name** *vlan-id* | **protocol-identity** }

**undo lldp tlv-enable dot1-tlv** { **protocol-vlan-id** *vlan-id* | **vlan-name** *vlan-id* | **protocol-identity** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **protocol-vlan-id** *vlan-id* | Indicates Port and Protocol VLAN ID TLVs. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **vlan-name** *vlan-id* | Indicates VLAN Name TLVs. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **protocol-identity** | Indicates Protocol Identity TLVs. | - |
| **dot1-tlv** | Indicates TLVs defined by IEEE 802.1, including:   * Port And Protocol VLAN ID TLV. * VLAN Name TLV. * Protocol Identity TLV. | - |



Views
-----

Layer 2 100GE interface view,100GE interface view,Layer 2 10GE interface view,10GE interface view,Layer 2 200GE interface view,200GE interface view,25GE-L2 view,25GE interface view,400GE-L2 view,400GE interface view,Layer 2 50GE interface view,50GE interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A TLV is the basic information unit of an LLDPDU. A device encapsulates information about its main capabilities, management address, device ID, and interface ID into TLVs, encapsulates multiple TLVs into an LLDPDU, and encapsulates an LLDPDU into an LLDP packet. A device exchanges information with neighbors using LLDP packets. During the process of exchanging LLDP packets between devices, the LLDPDU encapsulated in an LLDP packet carries various TLVs as needed. A device sends its status information and receives neighbor status information based on these different TLVs.TLVs that can be encapsulated into an LLDPDU include basic TLVs, TLVs defined by IEEE 802.1, TLVs defined by IEEE 802.3, and DCBX TLVs.

* Basic TLVs implement basic LLDP functions. In addition to optional management-address, port-description, system-capability, system-description, and system-name TLVs, basic TLVs include four mandatory TLVs that must be encapsulated into an LLDPDU to be advertised. For details, see "LLDP Feature Description".
* TLVs defined by IEEE 802.1, TLVs defined by IEEE 802.3, and DCBX TLVs are optional TLVs used to enhance the LLDP function. Determine whether to encapsulate these TLVs into LLDPDUs for advertisement as needed.

**Prerequisites**

LLDP has been enabled globally using the lldp enable command in the system view.

**Precautions**

By default, an interface is allowed to advertise all types of TLVs except DCBX TLVs and Protocol Identity TLVs. To disable an interface from advertising TLVs except DCBX TLVs and Protocol Identity TLVs, run the **undo lldp tlv-enable** command.


Example
-------

# Configure an interface to advertise the Protocol Identity TLV defined in IEEE 802.1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] lldp tlv-enable dot1-tlv protocol-identity

```