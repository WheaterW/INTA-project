IS-IS Control Packets
=====================

IS-IS Control Packets

#### IS-IS PDU Formats

IS-IS PDUs are mainly classified into Hello PDUs, LSPs, and SNPs. The PDUs are further classified into nine types of PDUs (as listed in [Table 1](#EN-US_CONCEPT_0000001130622640__en-us_concept_0000001176663887_tab_01)), each identified by a 5-digit type code. The nine types of PDUs are used by IS-IS to process control information.

**Table 1** IS-IS PDUs
| PDU Type | Abbreviation | Type Value |
| --- | --- | --- |
| Level-1 LAN IS-IS Hello PDU | L1 LAN IIH | 15 |
| Level-2 LAN IS-IS Hello PDU | L2 LAN IIH | 16 |
| Point-to-point IS-IS Hello PDU | P2P IIH | 17 |
| Level-1 link state PDU | L1 LSP | 18 |
| Level-2 link state PDU | L2 LSP | 20 |
| Level-1 complete sequence numbers PDU | L1 CSNP | 24 |
| Level-2 complete sequence numbers PDU | L2 CSNP | 25 |
| Level-1 partial sequence numbers PDU | L1 PSNP | 26 |
| Level-2 partial sequence numbers PDU | L2 PSNP | 27 |


The first eight octets in all IS-IS PDUs are public. [Figure 1](#EN-US_CONCEPT_0000001130622640__en-us_concept_0000001176663887_fig_dc_vrp_isis_feature_003401) shows the IS-IS PDU format.**Figure 1** IS-IS PDU format  
![](figure/en-us_image_0000001176743835.png)

The main fields are described as follows:

* Intradomain Routing Protocol Discriminator: network layer protocol identifier. In IS-IS, the value is fixed at 0x83.
* Length Indicator: length of the fixed header, in octets.
* ID Length: length of the system ID in this routing domain.
* PDU Type: type of a PDU. For details, see [Table 1](#EN-US_CONCEPT_0000001130622640__en-us_concept_0000001176663887_tab_01).
* Maximum Area Address: maximum number of area addresses supported in the IS-IS area. The value is fixed at 0, indicating that a maximum of three area addresses are supported in this IS-IS area.
* TLV: Each type of PDU has a set of TLV codes. [Table 2](#EN-US_CONCEPT_0000001130622640__en-us_concept_0000001176663887_tab_02) lists the mapping between TLV codes and PDU types.
  
  **Table 2** Mapping between TLV codes and PDU types
  | TLV Code | Name | PDU Type |
  | --- | --- | --- |
  | 1 | Area Addresses | IIH and LSP |
  | 2 | IS Neighbors (LSP) | LSP |
  | 4 | Partition Designated Level2 IS | Level-2 LSP |
  | 6 | IS Neighbors (MAC Address) | LAN IIH |
  | 7 | IS Neighbors (SNPA Address) | LAN IIH |
  | 8 | Padding | IIH |
  | 9 | LSP Entries | SNP |
  | 10 | Authentication Information | IIH, LSP, and SNP |
  | 128 | IP Internal Reachability Information | LSP |
  | 129 | Protocols Supported | IIH and LSP |
  | 130 | IP External Reachability Information | Level-2 LSP |
  | 131 | Inter-Domain Routing Protocol Information | Level-2 LSP |
  | 132 | IP Interface Address | IIH and LSP |


#### Hello PDU

Hello PDUs, also known as IIHs, are used to establish and maintain neighbor relationships. On broadcast networks, Level-1 IS-IS routing devices use Level-1 LAN IIHs, and Level-2 IS-IS routing devices use Level-2 LAN IIHs. On non-broadcast networks, routing devices use P2P IIHs. LAN IIHs and P2P IIHs have different formats.

[Figure 2](#EN-US_CONCEPT_0000001130622640__en-us_concept_0000001176663887_fig_dc_vrp_isis_feature_003402) shows the format of IIHs on a broadcast network.**Figure 2** Level-1/Level-2 LAN IIH format  
![](figure/en-us_image_0000001130784176.png)

[Figure 3](#EN-US_CONCEPT_0000001130622640__en-us_concept_0000001176663887_fig_dc_vrp_isis_feature_003403) shows the format of IIHs on a P2P network.**Figure 3** P2P IIH format  
![](figure/en-us_image_0000001176663939.png)

As shown in [Figure 3](#EN-US_CONCEPT_0000001130622640__en-us_concept_0000001176663887_fig_dc_vrp_isis_feature_003403), most fields in a P2P IIH are the same as those in a LAN IIH. However, the P2P IIH does not have the **Priority** or **LAN ID** field, and instead has a **Local Circuit ID** field, which indicates the local link ID.


#### LSP Format

LSPs are used to exchange link-state information and are classified as Level-1 or Level-2 LSPs. Level-1 IS-IS transmits Level-1 LSPs, Level-2 IS-IS transmits Level-2 LSPs, and Level-1-2 IS-IS can transmit both. Level-1 and Level-2 LSPs have the same format, as shown in [Figure 4](#EN-US_CONCEPT_0000001130622640__en-us_concept_0000001176663887_fig_dc_vrp_isis_feature_003404).

**Figure 4** Level-1 or Level-2 LSP  
![](figure/en-us_image_0000001176663935.png)

[Table 3](#EN-US_CONCEPT_0000001130622640__en-us_concept_0000001176663887_table183278394331) describes the main fields.

**Table 3** Main fields in the LSP format
| Field | Description | Function |
| --- | --- | --- |
| ATT | Area attachment bit | After a Level-1 routing device receives a Level-1 LSP with the ATT bit set to 1 from a Level-1-2 routing device, the Level-1 routing device creates a default route, with the Level-1-2 routing device as the next hop.  Although the ATT bit is defined in both Level-1 and Level-2 LSPs, it can only be set to 1 in Level-1 LSPs and by Level-1-2 routing devices. |
| OL | LSDB overload bit | LSPs with the OL bit set to 1 are still flooded on the network, but these LSPs are ignored during calculation of the routes that pass through the routing device that sets the OL bit to 1. Specifically, if a device sets the OL bit to 1, other devices ignore this device (except for direct routes to it) when performing SPF calculation. |
| IS Type | Type of the IS-IS generating the LSP | The value **01** indicates Level-1 IS-IS; the value **11** indicates Level-2 IS-IS. |



#### SNP

SNPs describe all or some LSPs in the LSDB and are used for LSDB synchronization and maintenance. SNPs consist of CSNPs and PSNPs.

Each CSNP contains the summary of all LSPs in an LSDB. CSNPs help ensure LSDB synchronization between neighboring routing devices. On broadcast networks, CSNPs are sent by the DIS at an interval (10s by default), while on P2P links they are sent only when a neighbor relationship is initially established. [Figure 5](#EN-US_CONCEPT_0000001130622640__en-us_concept_0000001176663887_fig_dc_vrp_isis_feature_003405) shows the CSNP format.

**Figure 5** Level-1/Level-2 CSNP format  
![](figure/en-us_image_0000001176663933.png)

[Table 4](#EN-US_CONCEPT_0000001130622640__en-us_concept_0000001176663887_table115521523163220) describes the main fields in the CSNP format.

**Table 4** Main fields in the CSNP format
| Field | Description |
| --- | --- |
| Source ID | System ID of the device that sends the CSNP |
| Start LSP ID | ID of the first LSP in the CSNP |
| End LSP ID | ID of the last LSP in the CSNP |

PSNP: Each PSNP lists only the sequence numbers of recently received LSPs and can acknowledge the reception of multiple LSPs at a time. In addition, if the local LSDB is not updated, the local end sends a PSNP to request new LSPs from a neighbor. [Figure 6](#EN-US_CONCEPT_0000001130622640__en-us_concept_0000001176663887_fig_dc_vrp_isis_feature_003406) shows the PSNP format.

**Figure 6** Level-1/Level-2 PSNP format  
![](figure/en-us_image_0000001176663937.png)