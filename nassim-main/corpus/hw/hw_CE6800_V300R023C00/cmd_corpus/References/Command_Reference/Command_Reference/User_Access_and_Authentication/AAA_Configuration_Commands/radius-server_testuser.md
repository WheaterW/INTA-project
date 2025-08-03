radius-server testuser
======================

radius-server testuser

Function
--------

The **radius-server testuser** command enables the automatic detection function and configures an automatic detection account.

The **undo radius-server testuser** command restores the default settings.

By default, the automatic detection function is disabled.



Format
------

**radius-server testuser username** *username* **password** **cipher** *password*

**undo radius-server testuser**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **username** *username* | Specifies a user name used for automatic detection. | The value is a string of 1 to 253 case-sensitive characters. If the user name contains spaces, you must enclose the name with double quotation marks ("), for example, "user for test". |
| **password** | The user password. | - |
| **cipher** *password* | Specifies the user password for automatic detection. | The value is a string of 1 to 128 case-sensitive characters in plaintext or a string of 128 to 268 case-sensitive characters in ciphertext. The string can contain spaces if it is enclosed in double quotation marks ("). |




Views
-----

RADIUS server template view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

After the RADIUS server status is marked as down, you can configure the automatic detection function to test the RADIUS server reachability.

The automatic detection function can be enabled when the user name and password used for automatic detection are configured in the RADIUS server template view on the device. The user name and password do not need to be configured on the RADIUS server. Authentication success is not required. If the device receives an authentication failure response packet, the RADIUS server is properly working and the device marks the RADIUS server status as up. If the device does not receive any response packet, the RADIUS server is unavailable and the device marks the RADIUS server status as down.Automatic detection is classified into the following conditions depending on the RADIUS server status:

* Down: By default, the device automatically detects only RADIUS servers in down state. After the RADIUS server status is marked as down and the automatic detection period expires, the device sends detection packets to the RADIUS server. If the device receives a response packet from the RADIUS server within the timeout period for detection packets, the device marks the RADIUS server status as up; otherwise, the RADIUS server status remains down.
* Up: The device can also be enabled to automatically detect RADIUS servers in up state using a command. After the automatic detection period expires, the device sends detection packets to the RADIUS server. If the conditions for marking the RADIUS server status to down are met, the device marks the RADIUS server status as down.

On a large enterprise network, you are advised not to enable automatic detection of RADIUS servers in up state. This is because if automatic detection is enabled on multiple NAS devices, RADIUS servers periodically receive a large number of detection packets when processing RADIUS Access-Request packets from users, which may deteriorate processing performance of the RADIUS servers.

* Force-up: After marking the RADIUS server status as Force-up and having automatic detection enabled, the device immediately sends a detection packet. If the device receives a response packet from the RADIUS server within the timeout period for detection packets, the device marks the RADIUS server status as up; otherwise, the device marks the RADIUS server status as down.To set the timeout period of detection packets, run the **radius-server detect-server timeout** command.


Example
-------

# Create an automatic detection account in the RADIUS server template acs, and set the user name to test and password to YsHsjx\_202206.
```
<HUAWEI> system-view
[~HUAWEI] radius-server template acs
[*HUAWEI-radius-acs] radius-server testuser username test password cipher YsHsjx_202206
Info: This account is used only to test the connectivity of the RADIUS server. Do not use the actual account.

```