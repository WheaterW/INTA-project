Overview of Atom GPS Timing
===========================

Overview of Atom GPS Timing

#### Background

As the commercialization of LTE-TDD and LTE-A accelerates, there is a growing need for time synchronization on base stations. Traditionally, the GPS and PTP solutions were used on base stations to implement time synchronization.

The GPS solution requires GPS antenna to be deployed on each base station, leading to high TCO. The PTP solution requires PTP support on network-wide devices, resulting in huge costs on network reconstruction for network carriers.

Furthermore, GPS antenna can properly receive data from GPS satellites only when they are placed outdoor and meet installation angle requirements. When it comes to indoor deployment, long feeders are in place to penetrate walls, and site selection requires heavy consideration due to high-demanding lightning protection. These disadvantages lead to high TCO and make GPS antenna deployment challenging on indoor devices. Another weakness is that most indoor equipment rooms are leased, which places strict requirements for coaxial cables penetrating walls and complex application procedure. For example, taking security factors into consideration, the laws and regulations in Japan specify that radio frequency (RF) cables are not allowed to be deployed in rooms by penetrating walls.

To address the preceding challenges, the Atom GPS timing system is introduced to NE40Es. Specifically, an Atom GPS module which is comparable to a lightweight BITS device is inserted to a NE40E to provide GPS access to the transport network. Upon receipt of GPS clock signals, the Atom GPS module converts them into SyncE signals and then sends the SyncE signals to the NE40E. Upon receipt of GPS time signals, the Atom GPS module converts them into 1588v2 signals and then sends the 1588v2 signals to base stations. This mechanism greatly reduces the TCO for carriers.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The Atom GPS functions described in this section are implemented by the Atom GPS 1.0 module (AE 905S module).



#### Interface Types Supported by the Atom GPS Module

The Atom GPS module can be inserted into only GE optical interfaces and supports only the 1000M full duplex mode, rather than the auto-sensing mode.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

After the Atom GPS module is inserted into a device interface, the interface can be configured with only the clock feature, rather than other services.



#### PTP Device Types Supported by the Atom GPS Module

The PTP device type supported by the Atom GPS module can only be boundary clock (BC) or telecom boundary clock (T-BC). A BC or T-BC has multiple clock interfaces: One is used to synchronize the time with the upstream device, and the others (passive interfaces excluded) are used to transmit time information to downstream devices.


#### Delay Measurement Mechanism Supported by the Atom GPS Module

By default, the Atom GPS module supports the delay request-response mechanism of PTP. This default setting cannot be modified.