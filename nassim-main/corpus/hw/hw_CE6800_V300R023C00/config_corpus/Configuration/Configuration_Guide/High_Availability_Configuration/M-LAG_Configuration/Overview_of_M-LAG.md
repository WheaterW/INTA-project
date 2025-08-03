Overview of M-LAG
=================

Overview of M-LAG

#### Definition

Multichassis Link Aggregation Group (M-LAG) implements link aggregation among multiple devices. In [Figure 1](#EN-US_CONCEPT_0000001564009069__dc_cfg_m-lag_0002_fig_01), M-LAG bundles multiple physical links connecting DeviceA and DeviceB to ServerA (a device or host) into a logical link, and allows DeviceA and DeviceB to appear to ServerA as a single device, improving link reliability from the card level to the device level.**Figure 1** M-LAG diagram  
![](figure/en-us_image_0000001564129021.png)


#### Purpose

Ethernet link aggregation (Eth-Trunk) connects two single devices. If one of these devices, or the Eth-Trunk between them, becomes faulty, the two ends can no longer communicate with each other. M-LAG aggregates interfaces on both devices in an M-LAG dual-active system (known as M-LAG member devices) into one logical interface. If one device in the M-LAG dual-active system or one member link suddenly fails, the M-LAG can still forward traffic, ensuring reliable data transmission. In addition to improving link reliability, M-LAG provides the following benefits:

* Virtualizes both M-LAG member devices into one logical device which provides a loop-free Layer 2 topology, simplifying the logical networking and improving bandwidth efficiency.
* Allows both M-LAG member devices to be upgraded separately, improving upgrade efficiency and minimizing service interruptions.

As such, M-LAG is recommended for scenarios that require high network reliability and the shortest possible service interruptions during a device upgrade.