Checking the Device Status
==========================

Checking the Device Status

#### Context

You can obtain hardware information by displaying the hardware status, making it easier to detect and locate exceptions.


#### Procedure

**Table 1** Checking the device status
| Operation | Command | Description |
| --- | --- | --- |
| Check the device's equipment serial number (ESN). | [**display device esn**](cmdqueryname=display+device+esn) | The ESN is unique to each device, and is mandatory for license application. |
| Check electronic labels of a device. | [**display device elabel**](cmdqueryname=display+device+elabel) [ **slot** *slot-id* [ **brief** ] ] | Electronic labels identify the hardware information of a device. |
| Check device information. | [**display device**](cmdqueryname=display+device) [ **slot** *slot-id* | **all** ] | You can run this command to check the type and status of components on a device. |
| [**display device board**](cmdqueryname=display+device+board) | You can run this command to display the type and status of a device. The command output excludes information about power modules and fan modules. |
| [**display device configuration**](cmdqueryname=display+device+configuration) | You can run this command to check the types and status of devices, including pre-configured devices and installed devices. |
| Check power supply information. | [**display device power**](cmdqueryname=display+device+power) [ **verbose** ] | If the power supply of a device is abnormal, run this command to check the power supply information, including the slot number, status, and working mode of each power module. |
| Check power information. | [**display device power system**](cmdqueryname=display+device+power+system) | You can run this command to check the power information (including the interval at which power consumption data is updated and the power redundancy mode) of a device to provide the optimal power solution for the device. |
| Check the fan status. | [**display device fan**](cmdqueryname=display+device+fan) | If a device is not able to properly dissipate heat, its hardware may be damaged by the high temperature. To avoid this, if the device is overheated, run this command to check the fan status.  To manually adjust the fan speed, see [Configuring the Fan Speed](galaxy_devmgt_cfg_0095.html). |
| Check optical module information on a device port. | [**display interface**](cmdqueryname=display+interface) [ *interface-type* *interface-number* ] **transceiver** [ **verbose** | **brief** ] | You can run this command to check general, manufacturing, and alarm information about the optical module on a port. |
| Check information about a non-Huawei-certified optical module. | [**display interface transceiver**](cmdqueryname=display+interface+transceiver) **non-certified** [ **verbose** ] | You can run this command to check general, manufacturing, and alarm information about a non-Huawei-certified optical module. |
| Check temperature information. | [**display device temperature**](cmdqueryname=display+device+temperature) [ **slot** *slot-id* ] | You can run this command to check the current temperature of a device. Hardware may be damaged if the device's temperature is too high or low.  If the temperature of a device reaches a configured alarm threshold, a corresponding alarm is generated, prompting you to adjust working environment variables.  For details about how to adjust the temperature alarm threshold of a device, see [Configuring Temperature Alarm Thresholds](galaxy_devmgt_cfg_0097.html). |
| Check the CPU usage. | [**display cpu-usage**](cmdqueryname=display+cpu-usage) [ **slot** *slot-id* [ **cpu** *cpu-id* ] | **all** ] | You can run this command to check the CPU usage statistics. |
| [**display cpu-usage threshold**](cmdqueryname=display+cpu-usage+threshold) [ **slot** *slot-id* [ **cpu** *cpu-id* ] ] | You can run this command to check the CPU usage thresholds. |
| [**display cpu-usage monitor**](cmdqueryname=display+cpu-usage+monitor) { **all** | **slot** *slot-id* [ **cpu** *cpu-id* ] } | You can run this command to check the overload information about the CPU usage. |
| [**display cpu-usage monitor history**](cmdqueryname=display+cpu-usage+monitor+history) [ **slot** *slot-id* [ **cpu** *cpu-id* ] ] | You can run this command to check the historical overload information about the CPU usage. |
| Check the memory usage. | [**display memory**](cmdqueryname=display+memory) [ **slot** *slot-id* [ **cpu** *cpu-id* ] ] | You can run this command to check the memory usage statistics. |
| [**display memory threshold**](cmdqueryname=display+memory+threshold) [ **slot** *slot-id* [ **cpu** *cpu-id* ] ] | You can run this command to check the memory usage thresholds. |
| Check the device health status. | [**display health**](cmdqueryname=display+health) [ **verbose** ] | You can run this command to view the voltage, temperature, power supply information, fan information, CPU usage, and memory usage of a device. |
| Check the system MAC address of a device. | [**display system mac-address**](cmdqueryname=display+system+mac-address) [ **all** ] | - |
| Check the reset information of a device. | [**display reboot information**](cmdqueryname=display+reboot+information) **slot** *slot-id* | - |
| Check KPIs during device running. | [**display system resource usage**](cmdqueryname=display+system+resource+usage) { **slot** *slotId* [ **cpu** *cpuID* ] | **all** } | You can run this command to check KPIs to learn the overall running status of the device. |
| Check CPU and memory information. | [**display system resource brief**](cmdqueryname=display+system+resource+brief) | You can run this command to view the simplified summary of CPU and memory information. |
| Check disk partition information. | [**display disk partition**](cmdqueryname=display+disk+partition) *partitionName* [ **slot** *slotId* ] | - |