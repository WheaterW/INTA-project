Overview
========

Overview

#### PTP Clock Types Supported by the NE40E

CU-106 defines the following types of PTP clocks:

* Telecom grandmaster (T-GM): is a master-only clock that can have one or more PTP ports. It does not trace other PTP clocks.
* Telecom boundary clock (T-BC): can be either a master clock or a clock tracing another PTP clock.
* Telecom transparent clock (T-TC): forwards CU-106 packets. T-TCs correct the forwarding delay in CU-106 packets, instead of synchronizing time with any port.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The NE40E can function only as a T-BC or T-TC, but cannot function as a T-GM.

[Figure 1](#EN-US_CONCEPT_0000001825840797__fig10511341163915) shows the positions of the T-GM, T-BC, and T-TC on a time synchronization network.

**Figure 1** Positions of the T-GM, T-BC, and T-TC on a time synchronization network  
![](figure/en-us_image_0000001778921474.png)

#### Delay Measurement Mechanism Supported by the NE40E

The NE40E supports the delay request-response mechanism. Specifically, the system calculates the time offset according to the link delay between the master and slave clocks.


#### Clock Source Tracing Modes Supported by the NE40E

**BMCA**

On a CU-106 network, all clocks are deployed in a hierarchical structure according to the master-slave relationship. The grandmaster clock provides the reference time and is at the highest stratum level. Such a topology can be automatically generated through the best master clock algorithm (BMCA).