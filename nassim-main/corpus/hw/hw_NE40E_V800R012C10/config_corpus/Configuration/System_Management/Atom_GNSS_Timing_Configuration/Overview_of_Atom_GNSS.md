Overview of Atom GNSS
=====================

Overview of Atom GNSS

#### Background

As the commercialization of LTE-TDD and LTE-A accelerates, there is a growing need for time synchronization on base stations. Traditionally, the GNSS (GPS/GLONASS/Beidou) and PTP solutions were used on base stations to implement time synchronization.

If base stations connect directly to the GNSS, each base station must pay GNSS deployment costs. Consequently, the total cost of ownership (TCO) increases as the number of base stations increases. If base stations obtain the PTP time from the network, the entire network must support PTP time synchronization, which results in high network-wide reconstruction costs.

Using the GNSS solution also has additional limitations. For example, the GNSS antenna must be installed outdoors and positioned to receive signals from GNSS satellites. As a result, long feeders must be used to connect to devices that are deployed indoors, and holes must be drilled through walls in order to route these feeders indoors. In addition, requirements such as lightning protection must be considered when selecting antenna sites. These limitations make it difficult and costly to deploy GNSS antennas for indoor devices. Furthermore, rented indoor equipment rooms may have restrictions in place that prevent or strictly control through-wall installation of cables, and obtaining permissions for such installation may be complex.

The Atom GNSS timing system of the NE40E has been developed to overcome the problems. The Atom GNSS module can be installed in a device to function as a lightweight BITS source capable of providing GNSS access for the transport network. The Atom GNSS module can receive clock and time signals from the GNSS. The clock and time signals are converted into SyncE and 1588v2 signals, respectively, and then output to the NE40E where the module resides. PTP is used to synchronize the time to all base stations on the network. This significantly reduces the TCO of time synchronization for carriers.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The Atom GNSS functions described in this section are implemented by the Atom GPS 2.0 module (AE 905S B module).



#### Supported Interface Type

An Atom GNSS module supports only GE optical interfaces and the 1000M full duplex mode. It does not support the adaptive mode.


#### Supported PTP Device Type

The PTP device type supported by an Atom GNSS module can be boundary clock (BC) or telecom boundary clock (T-BC). A BC or T-BC has multiple clock interfaces. On a BC/T-BC, one interface is used to implement time synchronization with upstream devices, and other interfaces (passive interfaces excluded) are used to transmit time information to downstream devices.


#### Supported Delay Measurement Mechanism

By default, an Atom GNSS module supports the delay request-response mechanism, which is the PTP link delay measurement mechanism. Configuring this mechanism is not supported.