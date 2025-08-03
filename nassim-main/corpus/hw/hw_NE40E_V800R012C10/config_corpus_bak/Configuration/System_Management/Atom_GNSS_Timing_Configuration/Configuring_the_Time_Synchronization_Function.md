Configuring the Time Synchronization Function
=============================================

This section describes how to configure the time synchronization function for the Atom GNSS timing system.

#### Usage Scenario

On the IP RAN shown in [Figure 1](#EN-US_TASK_0000001779081726__fig_dc_ne_atom-gnss_cfg_900301), time synchronization needs to be performed between gNodeBs. In this case, you can deploy the Atom GNSS timing solution as follows: Insert an Atom GNSS module into an access aggregation node ASG. The Atom GNSS module synchronizes time signals from the GNSS, and the ASG synchronizes time signals from the Atom GNSS module. You can deploy the time synchronization function so that time signals are transmitted to other devices on the transport network, achieving network-wide time synchronization.

**Figure 1** Atom GNSS timing  
![](figure/en-us_image_0000001778922054.png "Click to enlarge")  


#### Pre-configuration Tasks

Before configuring the time synchronization function, complete the following tasks:

* Configure physical parameters of an interface and set the physical status of the interface to Up.
* Configure the Atom GNSS module to properly process GNSS time signals.


[Configuring the Time Synchronization Function on an Atom GNSS Module](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_atom-gnss_cfg_9010.html)

This section describes how to configure the time synchronization function on an Atom GNSS module so that GNSS time signals can be transmitted to the Router where the Atom GNSS module resides through 1588v2 packets and then to downstream devices.

[Configuring the 1588v2 Synchronization Function on the Router Where an Atom GNSS Module Resides](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_atom-gnss_cfg_9011.html)

Configuring 1588v2 globally involves operations such as enabling 1588v2 in the system view and setting the device type to BC. After enabling 1588v2 in the system view, enable it in the interface view. 

[Configuring the G.8275.1 Synchronization Function on the Router Where an Atom GNSS Module Resides](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_atom-gnss_cfg_9018.html)

To ensure G.8275.1 for time synchronization, you need to globally enable G.8275.1 in the system view, set the device type to T-BC, and configure basic information such as the domain value. After enabling G.8275.1 in the system view, you need to enable G.8275.1 in the interface view.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_atom-gnss_cfg_9012.html)