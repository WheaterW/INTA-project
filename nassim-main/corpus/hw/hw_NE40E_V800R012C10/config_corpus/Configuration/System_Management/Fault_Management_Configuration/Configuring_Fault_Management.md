Configuring Fault Management
============================

You can configure FM on a device to use the alarm masking, alarm delivery, and alarm suppression functions.

#### Usage Scenario

As the network scale expands, the network becomes increasingly complex, and therefore more network configurations and applications are deployed. If a module on a device fails, multiple alarms may be generated on one or more devices. The devices and NMS, however, may not be able to process all alarms, causing alarm loss during the alarm transmission. If some alarms that users are concerned about cannot be obtained, network management becomes difficult. FM dynamically manages and reports alarms generated on devices in a centralized manner.

The NE40E supports the following FM functions:

* Filters out repeated alarms, intermittent alarms, and flapping alarms.
* Masks the alarms that users are not concerned about.
* Displays alarm configurations, active alarms, historical alarms, and alarm statistics to present details about network faults.
* Clears historical alarms to simplify the alarm display.
* Simulates and reports alarms to check whether the terminal and NMS host are correctly configured and whether the management link is reachable.

#### Pre-configuration Tasks

Before configuring FM, complete the following tasks:

* Install the Router and power it on properly.
* Complete the alarm definition on the Router.


[Setting the Alarm Severity](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_fm_cfg_0022.html)

You can change the default alarm severity.

[Configuring a Suppression Period for an Alarm](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_fm_cfg_0005.html)

You can configure a suppression period for an alarm to prevent the alarm from being reported frequently.

[Configuring Alarm Suppression](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_fm_cfg_0006.html)

In normal cases, the system suppresses repeated alarms, flapping alarms, and intermittent alarms. You can disable alarm suppression of alarms that you are concerned about, hardware alarms, and ambient alarms.

[Masking All Alarms](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_fm_cfg_0009.html)

Terminal users can mask all alarms.

[Configuring an Alarm Masking Table to Mask Alarms](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_fm_cfg_0008.html)

This section describes how to edit and apply an alarm masking table. An alarm masking table can be used by different terminal users to mask the alarms that they are not concerned about.

[Configuring Alarm Inversion](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_fm_cfg_0030.html)

If you do not want an interface to generate loss alarms for services that have been deployed but not accessed, configure alarm inversion.

[Configuring NMS-based Correlative Alarm Suppression](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_fm_cfg_0025.html)

This section describes how to configure NMS-based correlative alarm suppression. This function enables the system to mask NMS-based correlative alarms and only reports root alarms to an NMS.

[Enabling Alarm Status Re-check](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_fm_cfg_0026.html)

After you enable alarm status re-check for a device, the device re-checks the status of a specified type of status change alarm and reports alarms again.