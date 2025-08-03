Overview of BFD
===============

Overview of BFD

#### Definition

Bidirectional Forwarding Detection (BFD) is a fast fault detection mechanism. After a BFD session is established between two systems, BFD packets are periodically sent over the path between the two systems. If one system does not receive BFD packets within a specified period, a fault has occurred on the link. After detecting the link fault through BFD, the upper-layer protocol can take measures to promptly rectify the fault.


#### Purpose

To minimize the impact of link faults on services and improve network reliability, a network device must be able to quickly detect faults when communicating with adjacent devices. Measures can then be taken to promptly rectify the faults to ensure service continuity.

On a live network, link faults can be detected using either of the following mechanisms:

* Hardware detection: For example, the Synchronous Digital Hierarchy (SDH) alarm function can be used to quickly detect link hardware faults.
* Hello detection: If hardware detection is unavailable, Hello detection can be used to detect link faults.

However, the two mechanisms have the following issues:

* Only certain media support hardware detection.
* Hello detection takes more than 1 second to detect faults. When traffic is transmitted at gigabit rates, such slow detection causes great packet loss.
* On a Layer 3 network, the Hello packet detection mechanism cannot detect faults for all routes, such as static routes.

BFD provides the following functions:

* Provides a low-overhead, short-duration method to detect faults in a path between adjacent forwarding engines. The faults can be interface, data link, and even forwarding engine faults.
* Provides a single, unified mechanism to monitor any media and protocol layers in real time.
* Supports hardware-based BFD fault detection. The minimum interval for sending BFD packets can reach 3.3 ms.

#### Benefits

BFD offers the following benefits:

* BFD rapidly monitors link and IP route connectivity to improve network performance.
* Adjacent systems running BFD rapidly detect communication failures and establish a backup channel to restore communications, which improves network reliability.