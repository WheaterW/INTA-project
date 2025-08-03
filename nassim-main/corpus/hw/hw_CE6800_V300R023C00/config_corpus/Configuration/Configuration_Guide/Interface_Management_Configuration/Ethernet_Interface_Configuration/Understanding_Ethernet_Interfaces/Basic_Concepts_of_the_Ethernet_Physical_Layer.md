Basic Concepts of the Ethernet Physical Layer
=============================================

Basic Concepts of the Ethernet Physical Layer

#### CSMA/CD

**CSMA/CD definition:** Carrier sense multiple access with collision detection (CSMA/CD) is a media access control (MAC) method used most notably on the early Ethernet where multiple stations, such as computers and peripherals, are connected through a shared physical line. Because the stations can only access the shared line in half-duplex mode, CSMA/CD is used for collision detection and avoidance. Details are as follows:

* CS: carrier sense. Before transmitting data, a station checks to see if the line is idle. By doing so, chances of collision are decreased.
* MA: multiple access. The data sent by a station can be received by multiple other stations at the same time.
* CD: collision detection. A collision occurs if two stations transmit electrical signals simultaneously, because the signals are superimposed, doubling the normal voltage amplitude. The stations stop transmitting after sensing the conflict, and resume after a random amount of time.

**CSMA/CD implementation:** A station continuously checks whether the shared line is idle. If so, the station sends data. Otherwise, the station waits until the line is idle. If two stations send data simultaneously, a conflict occurs on the line, and the signal becomes unstable. After detecting an instability, the station immediately stops sending data but sends a series of interference pulses.

The pulses inform other stations that a conflict has occurred on the line. After detecting a conflict, the station waits for a random period, and then resumes the data transmission.


#### Minimum Frame Length

Due to the CSMA/CD algorithm limits, an Ethernet frame cannot be shorter than 64 bytes. This length is determined based on the maximum transmission distance and the collision detection mechanism. The use of a minimum frame length prevents conflicts from occurring in situations in which a station (for example, station A) finishes sending the last bit of a frame, but the first bit has not yet arrived at a faraway station (for example, station B). In this scenario, station B senses that the line is idle and begins to send data.

The upper layer protocol must ensure that each frame's Data field contains at least 46 bytes. In this way, the Data field with a 14-byte Ethernet frame header and 4-byte check code at the end of the frame equals the required minimum frame length of 64 bytes. If the Data field is less than 46 bytes, the upper layer must pad the gap. The maximum length of a frame's Data field has been set to 1500 bytes, as required by the memory cost and buffer of low-cost LAN controllers.


#### Maximum Transmission Distance

The maximum transmission distance depends on factors such as line quality and signal attenuation.


#### Duplex Modes

The Ethernet physical layer can work in either half- or full-duplex mode.

* Half-duplex mode: Data can only be sent or received at any time. The half-duplex mode has the following characteristics:
  
  + The CSMA/CD mechanism is used.
  + The maximum transmission distance is limited.
* Full-duplex mode: Data can be sent and received simultaneously. It has resolved conflicts, eliminated the need for CSMA/CD, and has the following features: The full-duplex mode has the following characteristics:
  
  + The maximum throughput is theoretically twice that of the half-duplex mode.
  + This mode extends the maximum transmission distance of the half-duplex mode.

#### Auto-Negotiation

**Auto-negotiation definition:** Auto-negotiation is a capability that enables devices at both ends of a physical link to automatically negotiate a working mode by exchanging information. The negotiated parameters include the half- or full-duplex mode and transmission speed. After the negotiation, the devices operate in negotiated mode.

**Auto-negotiation implementation:** The auto-negotiation mechanism applies to twisted pair cables only. When no data is transmitted over a twisted pair cable, the cable is not idle. Instead, it keeps transmitting the normal link pulses (NLPs) at a low frequency. Any Ethernet adapter with interfaces for twisted pair cables can identify these pulses. After lower-frequency pulses â fast link pulses (FLPs) â are inserted into the NLPs, the devices at both ends can also identify the pulses. By using FLPs to convey a small amount of data, the devices achieve auto-negotiation. [Figure 1](#EN-US_CONCEPT_0000001512681778__fig_dc_vrp_ethernet_feature_000401) shows the pulse insertion process.

**Figure 1** Pulse insertion  
![](figure/en-us_image_0000001512681850.png)  

Auto-negotiation priorities on Ethernet duplex links are listed as follows in descending order:

* 1000M full-duplex
* 1000M half-duplex
* 100M full-duplex
* 100M half-duplex
* 10M full-duplex
* 10M half-duplex

A configuration register in a device's network adapter saves the working modes that the adapter supports. For example, if a network adapter supports 100M and 10M working modes, the corresponding content is set in the corresponding register. After the network adapter is powered on, if auto-negotiation is allowed, the network adapter reads its configuration register, encodes the content, and sends it through FLPs. At the same time, it receives auto-negotiation data from the peer. It then compares the received data with the data in its configuration register and selects the optimal working mode. For example, if the device and its peer both support 100M full-duplex, the working mode 100M full-duplex is selected; if the peer supports only 10M full-duplex, the working mode 10M full-duplex is selected. If they do not share any capabilities, auto-negotiation fails, and they cannot communicate.

If auto-negotiation succeeds, the Ethernet adapter activates the link to transmit data. If auto-negotiation fails, the link cannot be used.

Auto-negotiation is implemented through physical layer coding and does not require any special data packets or bring upper-layer protocol overheads.

**Interface auto-negotiation rules:** Two connected interfaces can communicate with each other only when they work in the same mode.

* If both interfaces work in the same non-auto-negotiation mode, the interfaces can communicate.
* If both interfaces work in auto-negotiation mode, the interfaces can communicate through negotiation. The negotiated working mode depends on the interface with a lower capability. For example, if one interface works in full-duplex mode and the other in half-duplex mode, the negotiated working mode is half-duplex. The auto-negotiation function also allows the interfaces to negotiate the use of the traffic control function.
* If a local interface works in auto-negotiation mode and the remote interface works in a non-auto-negotiation mode, the negotiated working mode of the local interface depends on the working mode of the remote interface.
  
  [Table 1](#EN-US_CONCEPT_0000001512681778__table99802913810) describes the auto-negotiation rules for interfaces of the same type.
  
  **Table 1** Auto-negotiation rules for interfaces of the same type (local interface working in auto-negotiation mode)
  | Interface Type | Working Mode of the Remote Interface | Auto-Negotiation Result | Description |
  | --- | --- | --- | --- |
  | GE electrical interface | 10M half-duplex | 10M half-duplex | If the remote interface works in 10M full-duplex or 100M full-duplex mode, the working modes of the two interfaces are different after auto-negotiation, and packets may be dropped. Therefore, if the remote interface works in 10M full-duplex or 100M full-duplex mode, configure the local interface to work in the same mode. |
  | 10M full-duplex | 10M half-duplex |
  | 100M half-duplex | 100M half-duplex |
  | 100M full-duplex | 100M half-duplex |
  | 1000M full-duplex | 1000M full-duplex |
  
  According to the auto-negotiation rules described in [Table 1](#EN-US_CONCEPT_0000001512681778__table99802913810), if an interface works in auto-negotiation mode and the connected interface works in a non-auto-negotiation mode, packets may be dropped, or auto-negotiation may fail. To prevent such problems, configure two connected interfaces to work in the same mode to ensure that they can communicate properly.
  
  ![](public_sys-resources/note_3.0-en-us.png) 
  
  If interface hardware complies with auto-negotiation standards, it is recommended that Ethernet interfaces work in auto-negotiation mode.
  
  Manually setting interface rates and duplex modes usually complicates network planning and maintenance, and improper settings will affect or even interrupt the network communication.
  
  FE and higher-rate optical interfaces support only the full-duplex mode. Auto-negotiation enabled on GE optical interfaces is only for the negotiation of traffic control. When devices are directly connected using GE optical interfaces, auto-negotiation is enabled on the optical interfaces to detect unidirectional fiber faults. If one of two fibers is faulty, the fault information is synchronized on both ends through auto-negotiation to ensure that the interfaces on both ends go down. After the fault is rectified, the interfaces go up again through auto-negotiation.