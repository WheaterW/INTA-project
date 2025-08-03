Overview of CPOS
================

This section describes packet over SONET/SDH (POS) and channelized packet over SDH/SONET (CPOS) interfaces, exploring topics such as synchronous optical network (SONET) and synchronous digital hierarchy (SDH) concepts, channelized and unchannelized modes, and the SDH frame structure.

#### SONET and SDH

The SONET standard was defined by the American National Standards Institute (ANSI) for synchronous digital transmission. Mainly used in North America and Japan, it relies on clock synchronization across the entire network, where clocks of different stratums are synchronized with a very precise master clock.

In terms of synchronous transmission, SONET defines hierarchical line rates for the optical transmission system, with 51.84 Mbit/s as the baseline.

* For electrical signals, this baseline rate is called synchronous transport signal level 1 (STS-1).
* For optical signals, this baseline rate is called optical carrier level 1 (OC-1).

Synchronous transmission enables SONET to easily multiplex multiple signals.

SONET-based SDH is an international standard defined by the International Telecommunication Union Telecommunication Standardization Sector (ITU-T) and mainly used in Europe. Corresponding standards include recommendations G.707 to G.709 approved in 1988 and more than a dozen recommendations added in 1992.

SDH and SONET are essentially the same except the baseline transmission rate in SDH is 155.52 Mbit/s. This rate is called synchronous transport module level 1 (STM-1) and is equivalent to OC-3 in SONET.

Because SDH adopts synchronous multiplexing and flexible mapping, low-speed tributary signals can be added to or removed from SDH signals without the need to use many multiplexing/demultiplexing devices. This not only slashes costs in terms of equipment investment, but also reduces signal loss.

[Table 1](#EN-US_CONCEPT_0172364063__tab_dc_vrp_cpos_cfg_000201) lists the common SONET and SDH transmission rates. For convenience, they are typically rounded up or down to nominal values (provided in parentheses in this table).

**Table 1** Common SONET and SDH transmission rates
| SONET | | SDH | Rate (Mbit/s) |
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




#### Channelized and Unchannelized Modes

Low-speed tributary signals are called channels when they are multiplexed to form SDH signals.

In channelized mode, low-speed tributary STM-N signals are used to transmit multiple independent channels of data over an optical fiber. During the transmission, each channel has its own bandwidth resources as well as start and end points, and follows its own monitoring policy.

In unchannelized mode, all STM-N signals are used to transmit data through a single channel over an optical fiber. During the transmission, all the data has the same identifier as well as the same start and end points, and follows the same monitoring policy.

Using the channelized mode helps utilize bandwidth resources more effectively when multiple channels of low-speed signals need to be transmitted. Conversely, the unchannelized mode is recommended if only a single channel of high-speed signals needs to be transmitted.


#### Channelized Serial Interface

A channelized serial interface is a serial interface formed by CPOS interfaces. It has the same logical features as a synchronous serial interface.

An E1 channel of a CPOS interface can work in either clear channel mode (unframed mode) or channelized mode:

* In clear channel mode, an E1 channel forms a 2.048 Mbit/s channelized serial interface without having timeslot division.
  
  The name and number format of such an interface is **serial** *interface-number*/*e1-number*:0, where *interface-number* specifies a CPOS interface number and *e1-number* specifies an E1 channel number.
* In channelized mode, any of an E1 channel's 31 timeslots (excluding timeslot 0) can be randomly bundled into a serial interface.
  
  The name and number format of such an interface is **serial** *interface-number*/*e1-number*:*set-number*, where *interface-number* specifies a CPOS interface number, *e1-number* specifies an E1 channel number, and *set-number* specifies the index of the interface formed by bundling the timeslots of the CPOS interface's E1 channel.

#### POS and CPOS

POS applies to metropolitan area networks (MANs) and wide area networks (WANs). It supports packet data, such as IP packet data.

CPOS interfaces are channelized POS interfaces. Leveraging the characteristics of the SDH system, these interfaces offer the following benefits:

* Refined bandwidth allocation
* Reduced number of low-speed physical interfaces required on devices
* Enhanced aggregation capability of low-speed interfaces on devices
* Improved private line access capability of devices


#### SDH Frame Structure

This subsection describes the frame structure of an SDH signal, that is, an STM-N signal.

To add or drop low-speed tributary signals to or from high-speed signals, it is necessary to distribute tributary signals in a frame evenly and regularly. The ITU-T defines a rectangular block frame structure (expressed by bytes) for STM-N signals, as shown in [Figure 1](#EN-US_CONCEPT_0172364063__fig5257102744515).

**Figure 1** STM-N frame structure  
![](figure/en-us_image_0000001739374113.png)

The block frame structure of STM-N signals consists of 9 rows and 270 Ã *N* columns. Like the "N" in STM-N, *N* indicates the number of STM-1 signals multiplexed to this STM-N signal.

An STM-N frame consists of three parts: section overhead (SOH), administrative unit pointer (AU-PTR), and payload. SOH is classified as regenerator section overhead (RSOH) or multiplex section overhead (MSOH). AU-PTR is a pointer used to specify the position of the payload's first byte in the STM-N frame, providing a way for the receiver to correctly extract the payload.


#### Related Concepts

* Multiplexing unit: Basic SDH multiplexing units include container (C-*n*), virtual container (VC-*n*), tributary unit (TU-*n*), tributary unit group (TUG-*n*), administrative unit (AU-*n*), and administrative unit group (AUG-*n*), where *n* stands for the number of the unit level.
* Container: It is an information structure used to carry service signals that are transmitted at different rates. G.709 defines specifications for five types of standard containers: C-11, C-12, C-2, C-3, and C-4.
* VC: It is an information structure used to support path-layer connections in the SDH and functions as the information terminal of SDH channels. VCs are classified as lower-order VCs or higher-order VCs. VC-3 in AU-3 and VC-4 are both higher-order VCs.
* TU and TUG: A TU is an information structure that provides adaptation between the lower-order and higher-order path layers. A TUG is comprised of one or more TUs occupying fixed, defined positions in the payload of a higher-order VC.
* AU and AUG: An AU is an information structure that provides adaptation between the higher-order path layer and the multiplex section layer. An AUG is comprised of one or more AUs occupying fixed, defined positions in the STM-N payload.

#### Multiplexing from E1 to STM-1

As specified in recommendation G.709, there is more than one SDH multiplexing path from a valid payload to STM-N. [Figure 2](#EN-US_CONCEPT_0172364063__fig_dc_vrp_cpos_cfg_000202) shows the multiplexing process from E1 to STM-1.**Figure 2** Multiplexing from E1 to STM-1  
![](images/fig_dc_vrp_cpos_cfg_000202.png)  

In real-world applications, the adopted multiplexing path may vary by country and region.


#### Calculation of E1 Channel Sequence Numbers

Because CPOS interfaces use the byte-interleaved multiplexing mode, lower-order VCs in a higher-order VC are not sequentially organized. This subsection describes how to calculate the sequence numbers of TUs. To facilitate configuration, it is assumed that the E1 signals of CPOS interfaces adopt the AU-4 multiplexing path.

The multiplexing process in [Figure 3](#EN-US_CONCEPT_0172364063__fig_dc_vrp_cpos_cfg_000203) shows that the 2 Mbit/s multiplexing structure is 3-7-3 when the AU-4 multiplexing path is adopted. The formula for calculating the numbers of TU-12s located in different positions of a VC-4 is as follows:

VC-12 number = TUG-3 number + (TUG-2 number â 1) x 3 + (TU-12 number â 1) x 21

In a VC-4, all TUG-3s are numbered the same, all TUG-2s are numbered the same, and two TU-12s with a number difference of 1 are adjacent.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The numbers listed in the preceding formula represent the positions in a VC-4 frame. The TUG-3, TUG-2, and TU-12 numbers range from 1 to 3, 1 to 7, and 1 to 3, respectively. The TU-12 number indicates the multiplexing sequence number of the current TU-12 among the 63 TU-12s in a VC-4 frame. It equals the E1 channel number.


**Figure 3** Sequence of TUG-3s, TUG-2s, and TU-12s in a VC-4  
![](images/fig_dc_vrp_cpos_cfg_000203.png)  

If the AU-3 multiplexing path is adopted, the TU-12 number calculation method can be deduced in a similar way.

In scenarios where 63 E1 channels are configured for a CPOS interface, these channels can be directly numbered from 1 to 63. However, pay attention to channel number differences if such interfaces on a Huawei device interwork with channelized STM-1 interfaces on a non-Huawei device.


#### Overhead Bytes

SDH provides section-layer and path-layer monitoring functions. Section-layer monitoring is classified as regenerator section monitoring or multiplex section monitoring; path-layer monitoring is classified as higher-order path monitoring or lower-order path monitoring. These monitoring functions are implemented through different overhead bytes.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

There are various SDH overhead bytes. For brevity, this subsection introduces only some of them used in the configuration process. For details about other SDH overhead bytes, see the related books.

* SOH
  
  SOH is used to implement section-layer monitoring and consists of RSOH and MSOH.
  
  The payload of an STM-N frame contains path overhead (POH) bytes used to monitor low-speed tributary signals.
  
  J0, the regenerator section trace byte, is contained in RSOH. It is used to repetitively transmit a section access point identifier (SAPI) so that a section receiver can verify its continued connection to the intended transmitter. Within the network of a single carrier, the J0 byte can be any character. However, at the boundaries between the networks of different carriers, the J0 bytes of the receiver and transmitter must be the same. Through the J0 byte, carriers can detect and rectify network faults quickly, thereby shortening the network recovery time.
* POH
  
  POH is used to implement path-layer monitoring and is classified as higher-order path overhead or lower-order path overhead.
  
  The higher-order path overhead is used to monitor the paths at VC-4 and VC-3 levels.
  
  J1, the higher-order VC-N path trace byte, is contained in the higher-order path overhead. Similar to the J0 byte, the J1 byte is used to repetitively transmit a higher-order path access point identifier (PAPI) so that a path receiver can verify its continued connection to the intended transmitter. The J1 bytes of the receiver and transmitter must be the same.
  
  C2, the path signal label byte, is also contained in the higher-order path overhead. It is used to indicate the multiplexing structure and the attributes of the payload in a VC frame, including whether the path is loaded with services, the types of services, and the mapping mode. The C2 bytes of the receiver and transmitter must also be the same.

#### CPOS Usage Scenario

[Figure 4](#EN-US_CONCEPT_0172364063__fig_dc_vrp_cpos_cfg_000301) provides a typical example of CPOS networking. Assume that some users (e.g., some governmental agencies and enterprises) use low-end and mid-range devices to access the transmission network over E1 leased lines and that users who require a bandwidth between 2 Mbit/s and 44 Mbit/s (e.g., users of some data centers) simultaneously use several E1 leased lines.

The bandwidth of all these users aggregates on one or more CPOS interfaces over the transmission network. The interfaces are then connected to a high-end device, which identifies each low-end device based on timeslots.

**Figure 4** Typical CPOS networking  
![](images/fig_dc_vrp_cpos_cfg_000301.png)  

In real-world applications, there may be more than one level of transmission networks between CPOS interfaces and low-end devices, and other transmission devices may be needed to relay communication between the low-end devices and transmission networks. Logically, this application is equivalent to a scenario where low-end devices access DeviceA through E1 or *n* x E1 leased lines.