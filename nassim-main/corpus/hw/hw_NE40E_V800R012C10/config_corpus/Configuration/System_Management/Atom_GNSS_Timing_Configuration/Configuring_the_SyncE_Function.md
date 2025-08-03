Configuring the SyncE Function
==============================

This section describes how to configure the SyncE function.

#### Usage Scenario

On the IP RAN shown in [Figure 1](#EN-US_TASK_0000001825721605__fig_dc_ne_atom-gnss_cfg_900301), clock synchronization needs to be achieved between gNodeBs. The Atom GNSS timing solution can be deployed as follows to allow clock synchronization: Insert an Atom GNSS module into an ASG so that the Atom GNSS module can synchronize clock signals with the GNSS and the ASG can synchronize clock signals with the Atom GNSS module. Then, configure the SyncE function to allow transmission of clock signals to downstream devices and then to NodeBs. In this manner, network-wide clock synchronization is achieved.

**Figure 1** Networking of Atom GNSS timing  
![](figure/en-us_image_0000001778922054.png)

#### Pre-configuration Tasks

Before configuring the SyncE function, complete the following task:

* Configure the Atom GNSS module to properly process GNSS clock signals.


[Configuring the SyncE Function on an Atom GNSS Module](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_atom-gnss_cfg_9006.html)



[Configuring the SyncE Function on the Device Where an Atom GNSS Module Resides](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_atom-gnss_cfg_9007.html)

After the device where the Atom GNSS module resides synchronizes clock information from the Atom GNSS module, the device needs to transmit clock signals to downstream devices in order to achieve network-wide clock synchronization. Therefore, the SyncE function needs to be configured on the device.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_atom-gnss_cfg_9008.html)