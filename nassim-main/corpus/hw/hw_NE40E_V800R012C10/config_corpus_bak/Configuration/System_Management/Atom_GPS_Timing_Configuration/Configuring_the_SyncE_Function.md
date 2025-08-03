Configuring the SyncE Function
==============================

This section describes how to configure the SyncE function for the Atom GPS timing system.

#### Usage Scenario

On the IP RAN shown in [Figure 1](#EN-US_TASK_0000001825721077__fig_dc_ne_gps-sfp_cfg_900301), clock synchronization needs to be achieved between gNodeBs. In this case, you can deploy the Atom GPS timing solution as follows: Insert the Atom GPS module into the access aggregation node ASG. The Atom GPS module synchronizes clock signals from the GPS, and the ASG synchronizes clock signals from the Atom GPS module. You can deploy the SyncE function so that clock signals are transmitted to downstream devices, which then transmit the clock signals to gNodeBs, achieving network-wide clock synchronization.

**Figure 1** Networking diagram of Atom GPS timing  
![](figure/en-us_image_0000001779081238.png)

#### Pre-configuration Tasks

Before configuring the SyncE function, complete the following task:

* Configure the Atom GPS module to properly process GPS clock signals.


[Configuring the SyncE Function on an Atom GPS Module](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_gps-sfp_cfg_9006.html)



[Configuring the SyncE Function on the Device Where the Atom GPS Module Resides](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_gps-sfp_cfg_9007.html)

After the device where the Atom GPS module resides synchronizes clock information from the Atom GPS module, the device needs to transmit clock signals to downstream devices in order to achieve network-wide clock synchronization. Therefore, the SyncE function needs to be configured on the device.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_gps-sfp_cfg_9008.html)