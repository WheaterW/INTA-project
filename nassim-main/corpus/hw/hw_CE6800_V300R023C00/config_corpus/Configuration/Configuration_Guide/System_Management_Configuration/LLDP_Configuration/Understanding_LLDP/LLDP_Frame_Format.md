LLDP Frame Format
=================

LLDP frames are Ethernet frames encapsulated with LLDP data units (LLDPDUs). LLDP frames support two encapsulation modes: Ethernet II and Subnetwork Access Protocol (SNAP). Currently, the device supports the Ethernet II encapsulation mode. [Figure 1](#EN-US_CONCEPT_0000001176662623__fig_dc_vrp_lldp_feature_000501) shows the format of an Ethernet II LLDP frame.

**Figure 1** LLDP frame format  
![](figure/en-us_image_0000001130782878.png)  

[Table 1](#EN-US_CONCEPT_0000001176662623__tab_dc_vrp_lldp_feature_000501) describes the fields in an LLDP frame.

**Table 1** Fields in an LLDP frame
| Field | Description |
| --- | --- |
| Destination MAC address | Destination MAC address, a fixed multicast MAC address 0x0180-C200-000E. |
| Source MAC address | Source MAC address, a MAC address for an interface or a bridge MAC address for a device (Use the MAC address for an interface if there is one; otherwise, use the bridge MAC address for a device). |
| Type | Packet type, fixed at 0x88CC. |
| LLDPDU | LLDP data unit, body of an LLDP frame. |
| FCS | Frame check sequence. |



#### LLDPDU

An LLDPDU is a data unit encapsulated in the data field in an LLDP frame.

A device encapsulates local device information in type-length-value (TLV) format and combines several TLVs into an LLDPDU to be encapsulated in the data field of an LLDP frame for transmission. You can combine various TLVs to form an LLDPDU as required. TLVs allow a device to advertise its own status and learn the status of neighboring devices.

[Figure 2](#EN-US_CONCEPT_0000001176662623__fig_dc_vrp_lldp_feature_000502) shows the LLDPDU format.

**Figure 2** LLDPDU format  
![](figure/en-us_image_0000001130782880.png)  

LLDP prescribes that each LLDPDU can carry a maximum of 28 types of TLVs and that each LLDPDU must start with the Chassis ID TLV, Port ID TLV, and Time to Live TLV, and end with the End of LLDPDU TLV. The Chassis ID TLV, Port ID TLV, and Time to Live TLV are mandatory TLVs, and other TLVs are selected as needed. You can determine whether to combine them into an LLDPDU for transmission.


#### TLV

A TLV is the smallest unit of an LLDPDU. It gives type, length, and other information for a device object. [Figure 3](#EN-US_CONCEPT_0000001176662623__fig_dc_vrp_lldp_feature_000503) shows the TLV format.

**Figure 3** TLV format  
![](figure/en-us_image_0000001176742539.png)

* TLV type: a 7-bit field. Each value uniquely identifies a TLV type. For example, value 0 indicates End of LLDPDU TLV, and value 1 indicates a Chassis ID TLV.
* TLV information string length: a 9-bit field indicating the length of a TLV string.
* TLV information string: a string that contains TLV information. This field contains a maximum of 511 bytes.

For example, a device ID is carried in the Chassis ID TLV, an interface ID in the Port ID TLV, and a network management address in the Management Address TLV.

LLDPDUs can carry basic TLVs, TLVs defined by IEEE 802.1, TLVs defined by IEEE 802.3, Data Center Bridging Capabilities Exchange Protocol (DCBX) TLVs.

* Basic TLVs: are the basis for network device management.
  
  **Table 2** Basic TLVs
  | TLV Name | TLV Type Value | Description | Mandatory |
  | --- | --- | --- | --- |
  | End of LLDPDU TLV | 0 | End of an LLDPDU. | Yes |
  | Chassis ID TLV | 1 | Bridge MAC address of the transmit device. | Yes |
  | Port ID TLV | 2 | Number of a transmit interface of a device. | Yes |
  | Time To Live TLV | 3 | Timeout period of local device information on neighboring devices. | Yes |
  | Port Description TLV | 4 | String describing an Ethernet interface. | No |
  | System Name TLV | 5 | Device name. | No |
  | System Description TLV | 6 | System description. | No |
  | System Capabilities TLV | 7 | Primary functions of the system and whether these primary functions are enabled. | No |
  | Management Address TLV | 8 | Management address. | No |
  | Reserved | 9â126 | Reserved for special use. | No |
* Organizationally specific TLVs: include TLVs defined by IEEE 802.1 and those defined by IEEE 802.3. They are used to enhance network device management. Use these TLVs as needed.
  
  **TLVs defined by IEEE 802.1**
  
  **Table 3** Description of TLVs defined by IEEE 802.1
  | TLV Name | TLV Type Value | Description |
  | --- | --- | --- |
  | Reserved | 0 | Reserved for special use. |
  | Port And Protocol VLAN ID TLV | 1 | Protocol VLAN ID of an interface. |
  | VLAN Name TLV | 3 | VLAN name on an interface. |
  | Protocol Identity TLV | 4 | Protocol type that an interface supports. |
  | Reserved | 5â255 | Reserved for special use. |
  
  
  
  **TLVs defined by IEEE 802.3**
  
  **Table 4** Description of TLVs defined by IEEE 802.3
  | TLV Name | TLV Type Value | Description |
  | --- | --- | --- |
  | Reserved | 0 | Reserved for special use. |
  | MAC/PHY Configuration/Status TLV | 1 | Whether the interface supports rate auto-negotiation, whether auto-negotiation is enabled, as well as the current bit-rate and duplex settings of the device. |
  | Link Aggregation TLV | 3 | Link aggregation status. |
  | Maximum Frame Size TLV | 4 | Maximum frame length supported by interfaces. The maximum transmission unit (MTU) of an interface is used. |
  | Reserved | 5â255 | Reserved for special use. |
* DCBX TLVs:
  
  Include Data Center Bridging (DCB) information. Neighboring nodes on the data center network use the Data Center Bridging Exchange (DCBX) protocol to exchange and negotiate DCB information so that they have the same DCB information. This prevents packet loss on the data center network. DCBX encapsulates DCB information in DCBX TLVs and uses LLDP frames to exchange DCB information between neighboring nodes.