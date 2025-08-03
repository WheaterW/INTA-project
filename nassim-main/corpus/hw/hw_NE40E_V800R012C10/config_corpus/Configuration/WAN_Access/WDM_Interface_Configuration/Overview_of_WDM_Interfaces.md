Overview of WDM Interfaces
==========================

This section describes basic concepts of the optical transport network (OTN) and WDM.

#### Overview of WDM

Wavelength-division multiplexing (WDM), a technology used in the MAN and WAN, is used to transmit two or more optical signals of different wavelengths through the same optical fiber. A WDM system uses a multiplexer at the transmitter to join multiple optical carrier signals of different wavelengths (carrying different information) together on a single optical fiber, and a demultiplexer at the receiver to split the optical carrier signals apart. Then, an optical receiver further processes and restores the optical carrier signals to the original signals.

WDM interfaces supported by the NE40E consist of two interfaces, namely the controller WDM interface and its corresponding GE interface. Parameters related to the optical layer and electrical layer are configured in the controller WDM interface view, and all service features are configured in the GE interface view. The mapping mode of service signals on WDM interfaces is Ethernet over OTN.


#### Overview of OTN

Currently, the Synchronous Digital Hierarchy over Synchronous Optical Network (SDH/SONET) and WDM networks are usually used as transport networks. SDH/SONET processes and schedules services at the electrical layer and WDM processes and schedules services at the optical layer. With the increasing of data services, more and more bandwidths are required. The SDH/SONET network cannot meet the requirements on cross scheduling and network scalability. In addition, operators require the WDM network of high maintainability, security, and service scheduling flexibility. As a result, the OTN is developed to solve the problems.

The OTN technology applies the operability and manageability of SDH/SONET networks to the WDM system so that the OTN acquires the advantages of both the SDH/SONET network and the WDM network. In addition, the OTN technology defines a complete system structure, including the management and monitoring mechanism for each network layer and the network survival mechanism of the optical layer and electrical layer. In this manner, operators' carrier-class requirements are really met.

The OTN, which consists of optical network elements connected through optical fiber links, provides the transport, multiplexing, routing, management, monitoring, and protection (survival) capabilities to optical channels that are used to transmit client signals. The OTN features that the transport settings of any digital client signal are independent of specified client features, namely, client independence. Optical Transport Hierarchy (OTH) is a new connection-oriented transport technology that is used to develop the OTN. Owing to the great scalable capability, the OTN is applicable to the backbone mesh network. Ideally, the future transport network is an all OTN network. Compared with SDH networks, the OTN is the optical transport network of the next generation.

Compared with the traditional SDH and SONET networks, the OTN has the following advantages:

* Higher FEC capability
* Tandem Connection Monitoring (TCM) of more levels
* Transparent transport of client signals
* Measurable data exchange


#### FEC Overview

The communication reliability is of great importance to communication technologies. Multiple channel protection measures and automatic error correction coding techniques are used to enhance reliability.

The OTU overhead of an OTN frame contains FEC information. FEC, which corrects data by using algorithms, can effectively improve the transport performance of the system where the signal-to-noise ratio (SNR) and dispersion are limited. In this manner, the investment cost on the transport system is reduced accordingly. In addition, in the system using FEC, the receiver can receive signals of a lower SNR. The maximum single span is enlarged or the number of spans increases. In this manner, the total transmission distance of signals is prolonged.


#### TTI Overview

Trail trace identifier (TTI) is a byte string in the overhead of an optical transport unit (OTU) or an optical data unit (ODU). Like the J byte in the SDH segment overhead, the TTI identifies the source and destination stations to which each optical fiber is connected to prevent incorrect connection. If the received TTI differs from the expected value, a TIM alarm is generated.

OTU overhead: contains information about the transmission function of optical channels, and defines FAS, MFAS, GCC0, and SM (such as TTI, BIP-8, BDI, BEI/BIAE, and IAE) overheads. Among these overheads, TTI is a 64-byte string monitoring the connectivity of the OTU segment.

ODU overhead: contains information about the maintenance and operation function of optical channels, and defines TCM, PM, GCC1/GCC2, APS/PCC, and FTFL overheads. Among these overheads, TCM monitors the serial connection, and PM monitors ODU paths.