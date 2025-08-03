Configuring SNMP Proxy Using User-Defined Parameter Settings
============================================================

This section describes how to configure Simple Network Management Protocol (SNMP) proxy using default parameter settings.

#### Usage Scenario

As shown in [Figure 1](#EN-US_TASK_0172361028__en-us_task_0172361026_fig_dc_vrp_snmp_cfg_002601), a middle-point device and the cabinet control unit (CCU) of a managed device are placed in an outdoor cabinet. The middle-point device needs to communicate management information between the network management station (NMS) and managed device, so that the NMS can manage the configurations and system software version of the managed device.**Figure 1** Networking diagram for configuring SNMP proxy using default parameter settings  
![](images/fig_dc_vrp_snmp_cfg_002601.png)

If you want to use the NMS to manage the master device and the monitored device in a unified manner, deploy SNMP proxy on the master device. The NMS considers the master device and the monitored device as a virtual management unit, which significantly reduces the number of NEs to be managed by the NMS. This saves network management costs, monitors device running performance in real time, and improves service quality.

If you do not want the middle-point device to communicate with the managed device based on default parameter settings, configure SNMP proxy using user-defined parameter settings. After you configure SNMP proxy, the middle-point device communicates with the managed device based on the user-defined parameter settings.


#### Pre-configuration Tasks

Before configuring a device to communicate with an NMS using an SNMP proxy, complete the following tasks:

* Configure a routing protocol to ensure that there are reachable routes between the NMS and the middle-point device and between the middle-point device and the managed device.

#### Precautions

In this type of SNMP proxy configuration, you must configure SNMP on the managed device.


[Configuring the Middle-Point Device](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_snmp_cfg_0028.html)

This section describes how to use user-defined parameter settings to configure Simple Network Management Protocol (SNMP) proxy on the middle-point device.

[Configuring the Managed Device](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_snmp_cfg_0029.html)

This section describes how to configure the Simple Network Management Protocol (SNMP) on the managed device, so that the managed device can communicate with the network management station (NMS).

[Verifying the Configuration of SNMP Proxy Using User-Defined Parameter Settings](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_snmp_cfg_0030.html)

After configuring SNMP proxy using user-defined parameters, verify the SNMP configuration on the managed device and check whether the middle-point device communicates with the managed device based on user-defined parameter settings.