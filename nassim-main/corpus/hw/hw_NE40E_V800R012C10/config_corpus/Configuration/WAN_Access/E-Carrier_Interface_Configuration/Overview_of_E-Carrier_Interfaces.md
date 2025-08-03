Overview of E-Carrier Interfaces
================================

E-carrier interfaces can work in channelized, unchannelized, or clear channel mode.

#### Basic E-Carrier Concepts

The present digital transmission system uses pulse code modulation (PCM). PCM was initially designed to enable multi-line telephony along a trunk cable between two telephone exchanges. PCM has two incompatible international standards:

* European 30-channel PCM, which is also called E1
* North America 24-channel PCM, which is also called T1

E-carrier is a digital communication system recommended by the International Telecommunication Union-Telecommunication Standardization Sector (ITU-T). It evolves from E1 and has been applied in regions except North America.


#### Digital Carrier System

The carrier system enables a single physical communication channel to contain multiple logical channels. Therefore, the carrier system supports multi-channel communication.

In the digital carrier system, a single large-capacity digital circuit supports multiple logical channels, each of which supports one independent channel.


#### Working Mode

E-carrier interfaces can work in any of the following modes:

* Channelized mode: It is a framed mode in which all timeslots can be allocated to multiple channels.
* Unchannelized mode: It is a framed mode in which all timeslots can be bundled only once and allocated to only one channel.
* Clear channel mode: It is also called an unframed mode. There is no frame flag in the data stream, and all bits in the data stream are data. The data in the data stream belongs to only one channel.


#### Introduction to E1 Interfaces

A physical interface that is formed by E1 and can work only in clear channel is an E1 interface. A physical interface that is formed by E1 and can work in unchannelized or channelized mode is a CE1 interface.

* In clear channel mode, or unframed mode:
  
  An E1 interface forms a synchronous serial interface without timeslot division and with a transmission rate of 2.048 Mbit/s. The E1 interface has the same logical features as a synchronous serial interface.
* In unchannelized mode, or framed mode:
  
  A CE1 interface is physically divided into 31 timeslots numbered from 1 to 31. The timeslots can be bundled once into one channel. For example, if timeslots 1 and 2 are bundled into a serial interface of 128 kbit/s, the remaining timeslots cannot be bundled. The serial interface has the same logical features as a synchronous serial interface.
* In channelized mode, or framed mode:
  
  A CE1 interface is physically divided into 31 timeslots numbered from 1 to 31. The timeslots can be randomly bundled to form logical channels, each with a transmission rate of N x 64 kbit/s.
  
  All the timeslots can be grouped into multiple channel-sets. Each bundled channel-set of timeslots is used as an interface with the same logical features as a synchronous serial interface.

#### Introduction to E3 Interfaces

An E3 interface can work in either of the following modes:

* In clear channel mode, also called the unframed mode, an E3 interface functions like an interface with the transmission rate of 34.368 Mbit/s and without timeslot division. The E3 interface has the same logical features as a synchronous serial interface. It supports link layer protocols such as PPP and HDLC.
* In unchannelized mode, also called the framed mode, all timeslots of an E3 interface are bundled to form a serial interface with the transmission rate of 32.768 Mbit/s.

#### Introduction to Channelized Serial Interfaces

The serial interface formed by an E-carrier interface is called a channelized serial interface. A channelized serial interface has the same logical features as a synchronous serial interface.

The naming convention for a channelized serial interface is "**serial** *interface-number*:*set-number*," where *interface-number* specifies the name of the E-carrier interface, and *set-number* specifies the number of the interface that the E-carrier interface timeslots are bundled into.