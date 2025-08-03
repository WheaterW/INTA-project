DCBX
====

DCBX

#### Context

To implement lossless Ethernet on a converged data center network, both ends of a link must have the same PFC and ETS parameter settings. Configuring these parameters manually will lead to heavy workload, and errors may occur. DCBX is a link discovery protocol that enables devices at both ends of a link to discover and exchange DCB configurations, reducing the workload for administrators.


#### Fundamentals

DCBX provides the following functions:

* Discovers the DCB configuration of the remote device.
* Detects the DCB configuration errors of the remote device.
* Configures DCB parameters of the remote device.

DCBX enables devices at both ends to exchange the following DCB configurations:

* ETS priority group
* PFC

DCBX encapsulates DCB configurations into Link Layer Discovery Protocol (LLDP) TLVs so that devices at both ends of a link can exchange DCB configurations.

In [Figure 1](#EN-US_CONCEPT_0000001563869625__fig_dc_fd_dcb_000603), PFC is used as an example to illustrate DCBX implementation through LLDP.**Figure 1** DCBX implementation through LLDP  
![](figure/en-us_image_0000001512830118.png)

As shown in [Figure 1](#EN-US_CONCEPT_0000001563869625__fig_dc_fd_dcb_000603), LLDP is enabled globally and on PortA and PortB, and PortA is configured to send DCBX TLVs. DCBX is implemented as follows:

1. Set PFC parameters on PortA and PortB, and enable DCBX. The DCBX module instructs PortA and PortB to encapsulate their PFC parameters into LLDPDUs and send the LLDPDUs to each other.
2. The LLDP module of PortA sends LLDPDUs carrying DCBX TLVs to PortB at its own packet sending intervals.
3. PortB parses the DCBX TLVs in the received LLDPDUs and sends PFC parameters of PortA to the DCBX module. The DCBX module compares PFC parameters of PortA with its own PFC parameters. Through negotiation, PFC parameters on the two ends are made consistent, and a configuration file is then generated.


#### DCBX TLV

As shown in [Figure 2](#EN-US_CONCEPT_0000001563869625__fig_dc_fd_dcb_000602), the DCB configuration is encapsulated into specified TLVs. The Type field has a fixed value of 127, and the OUI field varies depending on the protocol type. The OUI field of the IEEE DCBX is 0x0080c2, and the OUI field of the INTEL DCBX is 0x001b21.

**Figure 2** DCBX TLV format  
![](figure/en-us_image_0000001512670526.png)

IEEE DCBX TLVs include the ETS Configuration TLV, ETS Recommendation TLV, PFC Configuration TLV and App TLV, as described in [Table 1](#EN-US_CONCEPT_0000001563869625__tab_dc_fd_dcb_000601).

**Table 1** IEEE DCBX TLVs
| TLV | Subtype | Length | Description |
| --- | --- | --- | --- |
| ETS Configuration TLV | 09 | 25 | Local ETS configuration:   * Priority group configuration: ID and bandwidth usage of a priority group * Priority queue configuration: priority queue ID and its priority group ID |
| ETS Recommendation TLV | 0A | 25 | Recommended ETS configuration, used for ETS configuration negotiation between two ends for configuration consistency:   * Priority group configuration: ID and bandwidth usage of a priority group * Priority queue configuration: priority queue ID and its priority group ID |
| PFC Configuration TLV | 0B | 6 | Local PFC configuration:   * Priority queue ID * Whether PFC is applied to a queue |
| App TLV | 0C | Unfixed value | Carried only when PFC is configured to work in auto mode for interconnection between products and between NICs. |

INTEL DCBX TLVs include the DCBX Control Sub-TLV, Priority Group Sub-TLV, Priority Flow Control Sub-TLV, and App Sub-TLV, as described in [Table 2](#EN-US_CONCEPT_0000001563869625__tab_dc_fd_dcb_000603) and [Table 3](#EN-US_CONCEPT_0000001563869625__tab_dc_fd_dcb_000602).

**Table 2** INTEL DCBX v1.00 TLVs
| TLV | Subtype | Length | Description |
| --- | --- | --- | --- |
| DCBX Control Sub-TLV | 01 | 10 | Information of DCBX packets. |
| Priority Group Sub-TLV | 02 | 28 | Recommended ETS configuration, used for ETS configuration negotiation between two ends for configuration consistency:   * Bandwidth usage of a priority group * Priority group ID |
| Priority Flow Control Sub-TLV | 03 | 5 | Local PFC configuration:   * Priority queue ID * Whether PFC is applied to a queue |
| App Sub-TLV | 05 | Unfixed value | Carried only when PFC is configured to work in auto mode for interconnection between products and between NICs. |


**Table 3** INTEL DCBX v1.01 TLVs
| TLV | Subtype | Length | Description |
| --- | --- | --- | --- |
| DCBX Control Sub-TLV | 01 | 10 | Information of DCBX packets. |
| Priority Group Sub-TLV | 02 | 17 | Recommended ETS configuration, used for ETS configuration negotiation between two ends for configuration consistency:   * Priority group configuration: ID and bandwidth usage of a priority group * Priority queue configuration: priority queue ID and its priority group ID |
| Priority Flow Control Sub-TLV | 03 | 6 | Local PFC configuration:   * Priority queue ID * Whether PFC is applied to a queue |
| App Sub-TLV | 04 | Unfixed value | Carried only when PFC is configured to work in auto mode for interconnection between products and between NICs. |