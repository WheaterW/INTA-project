Before You Start
================

Before configuring ATM OAM, familiarize yourself with the
applicable environment, complete the pre-configuration tasks, and
obtain the required data. This can help you complete the configuration
task quickly and accurately.

#### Usage Scenario

OAM provides various optional methods of detecting and locating
the faults on an ATM link. Choose the configuration as required.

* To detect the link status and report faults in real time without
  interrupting services, activate the CC function or configure the end-to-end
  loopback detection function.
  + The CC function detects the link status in real time by sending
    CC cells periodically and does not restrict the connection point attribute.
  + The end-to-end loopback detection function detects the link status
    in real time by sending loopback cells periodically and is available
    on only the PVP/PVC with the connection point attribute of
    end-point.Check whether the device supports CC cells or loopback cells
  and choose configurations based on the OAM connection point attribute.
  
  The CC function and the end-to-end loopback function cannot be
  configured on the same PVP/PVC.
* To locate and remove the link faults, configure the cell loopback
  function.
* To debug and detect whether the ATM OAM mechanism works normally,
  insert OAM cells manually.
* To respond to the OAM F5 loopback cells on the peer, configure
  the OAM F5 loopback cell response function.

#### Pre-configuration Tasks

Before configuring ATM OAM, complete the following
tasks:

* Configure physical attributes for the Router ATM interface.
* Configure an IP address and mask for the ATM interface or sub-interface.
* Configure an ATM PVC.

#### Data Preparation

To configure ATM OAM, you need the following data.

| No. | Data |
| --- | --- |
| 1 | Number of the ATM interface |
| 2 | VPI/VCI value |
| 3 | Number of times loopback cells are sent |
| 4 | Interval at which end-to-end loopback cells are sent |
| 5 | Number of delayed intervals for responding after the PVP/PVC status changes |