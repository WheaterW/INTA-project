Overview of Timestamp-Refresh
=============================

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This configuration is supported only by the NE40E-M2K and NE40E-M2K-B.


#### Definition

Timestamp-refresh is used for time synchronization and applies to Real-time Transport Protocol (RTP) packets. Timestamp-refresh allows a device to refresh the timestamps in RTP packets of input multicast streams that match the traffic policy on the multicast inbound interface to be synchronous with the local time of the device. Timestamp-refresh ensures consistency between the timestamps in packets and the local time of a router, preventing artifacts and black screens caused by time asynchronization.


#### Purpose

Currently, clock synchronization of signals cannot be ensured in the following scenarios, and local clock synchronization needs to be performed through timestamp refresh:

* The signal source is not synchronized with the PTP of the local device.
* The signal source is synchronized with the local PTP. However, due to long-distance transmission, the PTP lags behind. As a result, the packet timestamp is inconsistent with the local time of the device.

After timestamp-refresh is deployed, the timestamps of RTP packets can be refreshed to be synchronous with the local time of the device. In this way, the adverse impact caused by signal clock asynchronization can be eliminated.