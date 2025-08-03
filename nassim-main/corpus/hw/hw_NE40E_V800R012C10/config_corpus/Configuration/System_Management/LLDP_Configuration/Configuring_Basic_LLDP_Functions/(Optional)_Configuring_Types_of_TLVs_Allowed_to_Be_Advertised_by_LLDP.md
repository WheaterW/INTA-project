(Optional) Configuring Types of TLVs Allowed to Be Advertised by LLDP
=====================================================================

During the process of exchanging Link Layer Discovery Protocol (LLDP) packets between devices, the LLDP data unit (LLDPDU) encapsulated in an LLDP packet carries different type-length-values (TLVs) as needed. A device sends its status information and receives neighbor status information based on these different TLVs.

#### Background

TLVs that can be encapsulated into an LLDPDU include basic TLVs, TLVs defined by IEEE 802.1, TLVs defined by IEEE 802.3.

* Basic TLVs implement basic LLDP functions. In addition to optional **management-address**, **port-description**, **system-capability**, **system-description**, and **system-name** TLVs, basic TLVs also include three mandatory TLVs that must be encapsulated into LLDPDUs to be advertised. For details, see NE40E Feature Description > System Management > LLDP.
* TLVs defined by IEEE 802.1, TLVs defined by IEEE 802.3 are optional TLVs used to enhance the LLDP function. You can decide whether to encapsulate these TLVs into LLDPDUs to be advertised based on their functions and your actual requirements. For details, see NE40E Feature Description > System Management > LLDP.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

When configuring a device to advertise basic TLVs, TLVs defined by IEEE 802.1, and TLVs defined by IEEE 802.3:

* If you specify the **all** parameter, all optional TLVs of the same type will be advertised.
* If you do not specify the **all** parameter, only one optional TLV of the same type can be configured and advertised at a time. You can configure the device repeatedly to advertise multiple optional TLVs of different types.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The interface view is displayed.
3. Run **lldp tlv-enable basic-tlv** { **all** | **management-address** | **port-description** | **system-capability** | **system-description** | **system-name** }
   
   
   
   The type of TLVs that can be advertised by LLDP is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.