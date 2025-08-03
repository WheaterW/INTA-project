Configuring Performance Management Functions
============================================

This section describes how to configure performance management (PM) functions. The PM functions enable the system to collect performance statistics and generate performance statistics files. These statistics can then be queried by local and network management system (NMS) users.

#### Usage Scenario

PM collects and monitors performance statistics about the following objects:

* Interface traffic, such as statistics about sent packets on an Ethernet interface
* Protocol packets, such as statistics about Y.1731 packets
* Device operating parameters, such as the CPU usage

To collect service performance statistics, configure PM functions.


#### Pre-configuration Tasks

Before configuring PM functions, configure reachable routes between the device and PM server.


[Configuring a Performance Statistics Task](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pm_cfg_01002.html)

This section describes how to configure a performance statistics task. After the performance statistics collection interval is set and an instance is bound to a performance statistics task, the system starts collecting the performance statistics.

[(Optional) Uploading Performance Statistics Files](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pm_cfg_01003.html)

The system generates performance statistics files based on the collected performance statistics at a specified interval. To view the performance statistics on a performance management (PM) server, upload performance statistics files to the PM server.

[Verifying the Performance Management Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_pm_cfg_01004.html)

After configuring performance management (PM) functions, verify the configuration.