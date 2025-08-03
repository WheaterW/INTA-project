RADIUS Server Status Detection
==============================

Availability and maintainability of a RADIUS server are the prerequisites of user access authentication. If a device cannot communicate with the RADIUS server, the server cannot perform authentication or authorization for users.

#### RADIUS Server Status

A device can mark the RADIUS server status as up, down, or force-up. The following table describes the three RADIUS server statuses and their scenarios.

| Status | Whether the RADIUS Server Is Available | Condition for Switching the Server Status |
| --- | --- | --- |
| Up | The RADIUS server is available. | * The device initially marks the RADIUS server status as up. * The device marks the RADIUS server status as up after receiving packets from the server. |
| Down | The RADIUS server is unavailable. | The conditions for marking the RADIUS server status as down are met. |
| Force-up | When no RADIUS server is available, the device selects the RADIUS server in force-up state. | The device marks the RADIUS server status as force-up if the timer specified by **dead-time** expires. |

The RADIUS server status is initially marked as up. After a RADIUS Access-Request packet is received and the conditions for marking the RADIUS server status as down are met, the RADIUS server transitions to down. The RADIUS Access-Request packet that triggers the server status transition can be sent during user authentication or constructed by the administrator. For example, the RADIUS Access-Request packet can be a test packet sent when the [**test-aaa**](cmdqueryname=test-aaa) command is run or a detection packet sent during automatic detection.

The device changes the RADIUS server status from down to up or to force-up in the following scenarios:

* Down to force-up: The timer specified by **dead-time** starts after the device marks the RADIUS server status as down. The timer indicates the duration for which the server status remains down. After the timer expires, the device marks the RADIUS server status as force-up. If a new user needs to be authenticated using RADIUS and no RADIUS server is available, the device attempts to re-establish a connection with a RADIUS server in force-up state.
* Down to up: After receiving packets from the RADIUS server, the device changes the RADIUS server status from down to up. For example, after automatic detection is configured, the device receives response packets from the RADIUS server.


#### Conditions for Marking the RADIUS Server Status as Down

Whether the status of a RADIUS server can be marked as down depends on the following factors:

* Longest unresponsive interval of the RADIUS server (specified by **max-unresponsive-interval**)
* Number of times the RADIUS Access-Request packet is sent
* Interval for sending the RADIUS Access-Request packet
* Interval for detecting the RADIUS server status
* Number of RADIUS server detection interval cycles
* Maximum number of consecutive unacknowledged packets in each detection interval (specified by **dead-count**)

The device marks the RADIUS server status as down if either of the following conditions is met.

Condition 1: The device marks the RADIUS server status as down during RADIUS server status detection. After the system starts, the RADIUS server status detection timer runs. If the device does not receive any packet from the RADIUS server after sending the first RADIUS Access-Request packet to the server and the number of times the device does not receive any packet from the server (n) is greater than or equal to the maximum number of consecutive unacknowledged packets in a detection interval (specified by **dead-count**), a communication interruption is recorded. If the device still does not receive any packet from the RADIUS server, the device marks the RADIUS server status as down when recording the communication interruption for the same times as the detection interval cycles.

![](public_sys-resources/note_3.0-en-us.png) 

If the device does not record any communication interruption in a detection interval, all the previous communication interruption records are cleared.

Condition 2: The device marks the RADIUS server status as down if no response is received from the server for a long period of time. If the user access frequency is low, the device receives only a few RADIUS Access-Request packets from users, conditions for marking the RADIUS server status as down during RADIUS server status detection cannot be met, and the interval between two consecutive unacknowledged RADIUS Access-Request packets is greater than the value of **max-unresponsive-interval**, then the device marks the RADIUS server status as down. This mechanism ensures that users can obtain escape authorization.

[Figure 1](#EN-US_CONCEPT_0000001512676482__fig_dc_cfg_aaa_601801) shows the flowchart for marking the RADIUS server status as down. In this example, the detection interval cycles twice. If multiple servers are configured in the RADIUS server template, the overall status detection time is related to the number of servers and the server selection algorithm. If a user terminal uses the client software for authentication and the timeout period of the terminal client software is less than the sum of all the status detection time, the terminal client software may dial up repeatedly and cannot access the network. If the user escape function is configured, the sum of all the status detection time must be less than the timeout period of the terminal client software so that the users can obtain escape rights.

**Figure 1** Flowchart for marking the RADIUS server status as down  
![](figure/en-us_image_0000001563756057.png)

The following table lists the related commands.

| Command | Description |
| --- | --- |
| [**radius-server**](cmdqueryname=radius-server) { **dead-interval** *dead-interval* | **dead-count** *dead-count* | **detect-cycle** *detect-cycle* } | Configures conditions for marking the RADIUS server status as down during RADIUS server status detection.   * **dead-interval** *dead-interval*: specifies the detection interval. The default value is 5 seconds. * **dead-count** *dead-count*: specifies the maximum number of consecutive unacknowledged packets. The default value is 2. * **detect-cycle** *detect-cycle*: specifies the number of detection interval cycles. The default value is 2. |
| [**radius-server max-unresponsive-interval**](cmdqueryname=radius-server+max-unresponsive-interval) *max-unresponsive-interval* | Configures the maximum unresponsive interval of the RADIUS server. The default value is 300 seconds.  If the interval between two consecutive unacknowledged RADIUS Access-Request packets is greater than the value of **max-unresponsive-interval**, the device marks the RADIUS server status as down. |
| [**radius-server dead-time**](cmdqueryname=radius-server+dead-time) *dead-time* | Configures the duration for which the RADIUS server status remains down.  *dead-time*: specifies the duration for which the RADIUS server status remains down after the server status is marked as down. After the duration expires, the device marks the server status as force-up. The default value is 5 minutes. |



#### Automatic Detection

After the RADIUS server status is marked as down, you can configure the automatic detection function to test the RADIUS server reachability.

The automatic detection function needs to be enabled manually and can be enabled when the user name and password used for automatic detection are configured in the RADIUS server template view on the device. Authentication success is not required. If the device can receive an authentication failure response packet, the RADIUS server is working properly and the device marks the RADIUS server status as up. If the device cannot receive any response packet, the RADIUS server is unavailable and the device marks the RADIUS server status as down.

![](public_sys-resources/note_3.0-en-us.png) 

In a scenario where user accounts are stored on the third-party server, for example, user accounts are stored on the AD or LDAP server, you are advised to configure accounts for automatic detection on the local RADIUS server; otherwise, the server performance deteriorates because the local RADIUS server needs to query accounts through the third-party server.


After the automatic detection function is enabled, automatic detection is classified into the following conditions depending on differences of the RADIUS server status.

| Server Status | Whether Automatic Detection Is Supported | Time When an Automatic Detection Packet Is Sent | Condition for Switching the Server Status |
| --- | --- | --- | --- |
| Down | Automatic detection is supported by default. | An automatic detection packet is sent after the automatic detection period expires. | If the device receives a response packet from the RADIUS server within the timeout period for detection packets, the device marks the RADIUS server status as up; otherwise, the RADIUS server status remains down. |


The following table lists commands related to automatic detection.

| Command | Description |
| --- | --- |
| [**radius-server testuser username**](cmdqueryname=radius-server+testuser+username) *username* **password cipher** *password* | Enables the automatic detection function.   * *user-name*: specifies the user name for automatic detection. * *password*: specifies the password for automatic detection. |
| [**radius-server detect-server interval**](cmdqueryname=radius-server+detect-server+interval) *interval* | Specifies the automatic detection interval for RADIUS servers in down state. The default value is 60 seconds. |



#### Processing After the RADIUS Server Status Is Marked as Down

After the device marks the RADIUS server status as down, you can configure the escape function to make users obtain escape authorization. After the device detects that the RADIUS server becomes up, you can configure the reauthentication function to make users obtain authorization from the server through reauthentication, as shown in [Figure 2](#EN-US_CONCEPT_0000001512676482__fig_dc_cfg_aaa_601802).

![](public_sys-resources/note_3.0-en-us.png) 

After the RADIUS server goes up, 802.1Xauthentication users exit escape authorization and are re-authenticated


**Figure 2** Processing after the RADIUS server status is marked as down  
![](figure/en-us_image_0000001512676586.png)

The following table lists the commands for configuring escape rights upon transition of the RADIUS server status to down and configuring the reauthentication function.

| Command | Description |
| --- | --- |
| [**authentication event**](cmdqueryname=authentication+event) **authen-server-down action authorize** { **vlan** *vlan-id* | **service-scheme** *service-scheme-name* } [ **response-fail** ] | Configures the escape function upon transition of the RADIUS server status to down. |
| [**authentication event authen-server-up action re-authen**](cmdqueryname=authentication+event+authen-server-up+action+re-authen) | Configures the reauthentication function for users in escape state when the RADIUS server becomes up. |