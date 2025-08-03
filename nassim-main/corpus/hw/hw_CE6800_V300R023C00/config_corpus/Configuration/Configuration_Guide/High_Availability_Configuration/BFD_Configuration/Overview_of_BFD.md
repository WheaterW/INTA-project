Overview of BFD
===============

Overview of BFD

#### Definition

Bidirectional Forwarding Detection (BFD) is a fast fault detection mechanism. After a BFD session is established between two systems, BFD packets are periodically sent over the path between the two systems. If one system does not receive BFD packets within a specified period, a fault has occurred on the path. After detecting the link fault through BFD, the upper-layer protocol can take measures to promptly rectify the fault.


#### Purpose

To minimize the impact of device faults on services and improve network reliability, a network device must be able to quickly detect faults when communicating with adjacent devices. Measures can then be taken to promptly rectify the faults to ensure service continuity.

On a live network, link faults can be detected using either of the following mechanisms:

* Hardware detection: Hardware faults on links can be rapidly detected using hardware detection signals such as SDH alarms.
* Hello detection: If hardware faults cannot be detected using hardware detection signals, the Hello mechanism of routing protocols can be used to detect faults.

However, the two mechanisms have the following disadvantages:

* Not all media types support fault detection using hardware signals.
* Fault detection using the Hello mechanism takes more than 1 second. When traffic is transmitted at gigabit rates, such slow detection causes serious packet loss.
* On a Layer 3 network, the Hello mechanism cannot detect faults for all routes, such as static routes.

BFD is developed to solve the preceding problems. It is used to detect communication faults between devices by monitoring the connectivity of a data protocol on a path between systems. The path can be a physical or logical link or tunnel. BFD can be regarded as a service provided by the system.

* Upper-layer applications provide BFD with parameters, such as the detection address and detection interval.
* BFD creates, deletes, or modifies sessions based on these parameters and notifies upper-layer applications of the session status.

BFD provides the following functions:

* Lightweight and fast fault detection for channels between adjacent devices. Faults include interface, data link, and device faults.
* A single mechanism for real-time fault detection over any media at any protocol layer.

#### Benefits

BFD offers the following benefits:

* BFD rapidly detects link faults and monitors link and IP route connectivity, helping you improve network performance.
* Adjacent systems rapidly detect communication faults through BFD and establish a backup channel to restore communication, improving network reliability.