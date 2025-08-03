Configuration Precautions for Device Management
===============================================

Configuration_Precautions_for_Device_Management

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| When selecting a loopback interface for L2TPv3, the system does not select the board that has entered the energy-saving state.  Boards that have been selected as loopback interfaces by L2TPv3 do not enter the energy saving state. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Do not insert, remove, power on, power off, or reset a board during the upgrade of the board firmware. Otherwise, the board is damaged. In this case, you need to run commands to upgrade the board again or return the board for repair. During a board firmware upgrade, a message is displayed when an attempt is made to power on, power off, or reset the board by running the corresponding command. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| After anti-theft is enabled, if the device is rolled back to a version that does not support anti-theft due to startup problems, only the anti-theft service configuration control policies take effect, and no information or alarm related to anti-theft is displayed.  To unlock the device, upgrade the device to a version that supports anti-theft in BootROM mode. The NMS then delivers authorization information to unlock the device. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| After anti-theft is enabled, a device cannot be replaced with a version that does not support anti-theft through the serial port. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| After the anti-theft function is enabled, the device version cannot be replaced with a version that does not support anti-theft through commands. In addition, the version cannot be replaced through commands if the device is locked. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| After anti-theft is enabled and the device is locked, the interface bandwidth is limited to 10 Mbit/s or is periodically set to Down. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| After anti-theft is enabled, if no authorization is obtained, the current configuration cannot be modified, the configuration file for the next startup cannot be specified, and the current configuration file cannot be modified. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Before enabling anti-theft on a device, run the snmp-agent target-host command to configure the NMS as the target host for sending traps and use SNMPv2c or SNMPv3 to communicate with the NMS. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Before replacing a main control board, disable the anti-theft function. Otherwise, the subcard may fail to register. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Before installing a patch, disable the anti-theft function or set the device to the anti-theft authorization state. Otherwise, the patch may fail to be installed. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Only one user is allowed to run an upgrade command at the same time. During the upgrade of the board firmware, if the upgrade command is delivered again, the corresponding prompt is displayed. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| The LAK is the identity certificate assigned by the user to the HTM component. By default, the device uses the IAK assigned by Huawei to the HTM component before delivery.  To enable LAK, you must configure the IP address of the server that issues certificates on the device to issue digital certificates to LAK. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |