Overview
========

This section describes POS interfaces in terms of basic SONET and SDH concepts, channelization and non-channelization, and SDH frame structure.

#### Introduction to SONET and SDH

Synchronous Optical Network (SONET) is a synchronous digital transmission standard defined by the American National Standards Institute (ANSI) and mainly used in North America and Japan. Clocks at each level on the entire network are provided by a precise master clock.

SONET defines the line rate hierarchical structure of synchronous transmission for the optical transmission system. The basic transmission rate of SONET is 51.84 Mbit/s and approximately equals the transmission rate of E3.

* For an electrical signal, the transmission rate is called Level 1 Synchronous Transport Signal (STS-1).
* For an optical signal, the transmission rate is called Level 1 Optical Carrier (OC-1).

With synchronous signals, SONET can easily multiplex multiple signals.

Based on SONET, synchronous digital hierarchy (SDH) is an international standard defined by the ITU-T and mainly used in Europe. The corresponding standard of SDH is the proposals from G.707 to G.709 passed in 1988 and the proposals added in 1992.

SDH is similar to SONET to a great extent. The basic transmission rate of SDH is 155.52 Mbit/s, which is called Level 1 Synchronous Transfer Module (STM-1). This rate equals the OC-3 rate in SONET.

With synchronous multiplexing and flexible mapping, SDH can multiplex or demultiplex low-speed tributary signals from SDH signals without using multiplexing or demultiplexing devices. SDH reduces signal consumption and equipment investment.

[Table 1](#EN-US_CONCEPT_0172364012__tab_dc_ne_pos_cfg_200101) lists the common transmission rates of SONET and SDH. The transmission rates for different types of signals are increasing by four times. For convenience, the approximations in the parentheses are often used to express transmission rates.

**Table 1** Relationship between common transmission rates of SONET and SDH
| SONET | | SDH | Transmission Rate (Mbit/s) |
| --- | --- | --- | --- |
| Electrical Signal | Optical Signal | Optical Signal |
| STS-1 | OC-1 | - | 51.840 |
| STS-3 | OC-3 | STM-1 | 155.520 (155) |
| STS-9 | OC-9 | STM-3 | 466.560 |
| STS-12 | OC-12 | STM-4 | 622.080 (622) |
| STS-18 | OC-18 | STM-6 | 933.120 |
| STS-24 | OC-24 | STM-8 | 1244.160 |
| STS-36 | OC-36 | STM-12 | 1866.240 |
| STS-48 | OC-48 | STM-16 | 2488.320 (2.5 Gbit/s) |
| STS-96 | OC-96 | STM-32 | 4876.640 |
| STS-192 | OC-192 | STM-64 | 9953.280 (10 Gbit/s) |



#### Introduction to POS

Packet over SDH/SONET (POS), a technique for WANs and MANs, uses high-speed transport channels provided by SONET/SDH to directly transmit IP data packets. POS encapsulates IP packets into PPP or HDLC packets, maps the encapsulated packets to the payload of SONET/SDH signals by using the service adapter of the SONET/SDH channel, puts the payload into a SONET/SDH frame after adding the channel overhead at the transmission layer and the section overhead at the section layer, and finally sends the SONET/SDH frame to the optical network so that frames can be transmitted over optical fibers on the optical network. POS adopts connectionless-oriented transmission of IP and inherits the merit of IP packets.


#### SDH Frame Structure

This section describes the frame structure of an SDH signal, that is, the structure of an STM-N frame.

To add or drop low-speed tributary signals to or from high-speed signals, try to distribute tributary signals in the frame evenly and regularly. The ITU-T regulates that STM-N frames are rectangular and expressed in bytes, as shown in [Figure 1](#EN-US_CONCEPT_0172364012__fig_dc_ne_pos_cfg_200101).

**Figure 1** STM-N frame structure  
![](figure/en-us_image_0256711413.png)

STM-N is a frame with the dimension of 9 rows x 270 x N columns. Here, N is the same as that in STM-N, indicating how many STM-1 signals are multiplexed to this STM-N signal.

An STM-N frame consists of the following parts:

* Section overhead (SOH): includes regenerator section overhead (RSOH) and multiplex section overhead (MSOH).
* Administration unit pointer (AU-PTR): is the pointer that specifies the first byte of the payload. The receiver can correctly extract the payload according to the location of the pointer.
* Payload

#### Overhead Bytes

SDH provides monitoring and management at layers. Monitoring is classified as section monitoring or path monitoring. Section monitoring is classified as regenerator section monitoring or multiplex section monitoring. Path monitoring is classified as higher-order path monitoring or lower-order path monitoring. Different overhead bytes help to implement the monitoring functions.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This section describes only the SDH overhead bytes used in configuration.

* SOH
  
  SOH consists of RSOH and MSOH.
  
  The payload of an STM-N frame contains the path overhead (POH) that monitors low-speed tributary signals.
  
  J0, the regenerator section trace byte is contained in RSOH. This byte is used to transmit the Section Access Point Identifiers (SAPIs) repeatedly to check the connection between the receiver and the transmitter. The byte can be any character in a carrier's network, whereas the J0 bytes of the receiver and transmitter must match each other at the border of two carriers' networks. With the J0 byte, a carrier can locate and rectify faults in advance to speed up network recovery.
* Path overhead
  
  SOH monitors section layers, whereas POH monitors path layers. POH is classified as lower-order path overhead or higher-order path overhead.
  
  The higher-order path overhead monitors the paths at VC-4 and VC-3 levels.
  
  J1, the higher-order VC-N path trace byte, is contained in the higher-order path overhead. Similar to J0, J1 is used to transmit SAPIs repeatedly to check the connection between the receiver and the transmitter. The J1 bytes of the receiver and transmitter must match each other.
  
  C2, the path signal label byte, is contained in higher-order path overhead. C2 is used to specify the multiplexing structure and the attributes of the information payload in a VC frame, including whether the path is loaded with services, service types, and the mapping mode. The C2 bytes of the receiver and transmitter must match each other.

#### Terms

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The following terms may be used in interface configurations:

* Multiplexing units: Basic SDH multiplexing units include container (C-n), virtual container (VC-n), tributary unit (TU-n), tributary unit group (TUG-n), administrative unit (AU-n), and administrative unit group (AUG-n). Here, n stands for the number of the unit level.
* Container: It is used to carry service signals that are transmitted at different rates. G.709 defines specifications for five types of standard containers: C-11, C-12, C-2, C-3, and C-4.
* VC: It is an information terminal of SDH channels and is used to support connections between SDH channel layers. VCs are classified as lower-order VCs or higher-order VCs. VC-3 in AU-3 and VC-4 are higher-order VCs.
* TU and TUG: A TU provides adaptation between lower-order and higher-order path layers. A collection of TUs, occupying a fixed position in the payload of the higher-order VC, is called a TUG.
* AU and AUG: An AU provides adaptation between higher-order channel layer and multiplex section layer. A collection of AUs, occupying a fixed position in the payload of STM-N, is called an AUG.