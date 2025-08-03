lldp tlv-enable(Interface view)
===============================

lldp tlv-enable(Interface view)

Function
--------



The **lldp tlv-enable** command configures TLVs that can be advertised by an interface.

The **undo lldp tlv-enable** command configures TLVs that cannot be advertised by an interface.



An interface by default can advertise all TLVs except DCBX TLVs or Protocol Identity TLVs.


Format
------

**lldp tlv-enable** *dcbx*

**undo lldp tlv-enable** *dcbx*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *dcbx* | TLV Type. | The value is a string of 1 to 7 case-sensitive characters, spaces not supported. |



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

* Basic TLVs implement basic LLDP functions. Except for optional management-address, port-description, system-capability, system-description, and system-name TLVs, basic TLVs also include four mandatory TLVs that must be encapsulated into an LLDPDU to be advertised. For details, see "LLCP Packet Format" in "LLDP Fundamentals".
* TLVs defined by IEEE 802.1 and IEEE 802.3 and DCBX TLVs are optional TLVs used to enhance LLDP functions. Determine whether to encapsulate these TLVs into LLDPDUs for advertisement as needed.

**Prerequisites**

LLDP has been enabled globally using the lldp enable command in the system view.

**Precautions**

An interface by default can advertise all types of TLVs except DCBX TLVs and Protocol Identity TLVs. To disable LLDP on an interface from advertising any TLVs except DCBX TLVs and Protocol Identity TLVs, run the **lldp tlv-disable** command.


Example
-------

# Configure an interface to advertise DCBX TLV.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] lldp tlv-enable dcbx

```