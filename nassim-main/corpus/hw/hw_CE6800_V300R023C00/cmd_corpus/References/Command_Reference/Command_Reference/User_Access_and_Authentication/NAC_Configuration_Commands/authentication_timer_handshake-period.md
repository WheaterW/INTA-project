authentication timer handshake-period
=====================================

authentication timer handshake-period

Function
--------



The **authentication timer handshake-period handshake-times** command sets the handshake interval of the device with pre-connection users and authorized users.

The **undo authentication timer handshake-period** command restores the default setting.



By default, the handshake interval between the device and pre-connection users and between the device and authorized users is 100 seconds, and the number of handshakes is 3.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**authentication timer handshake-period** *handshake-period-value* [ **handshake-times** *handshake-times-value* ]

**undo authentication timer handshake-period**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *handshake-period-value* | Specifies the handshake interval. | The value is an integer that ranges from 5 to 7200. The default value is 100. |
| **handshake-times** *handshake-times-value* | Specifies the number of handshakes. | The value is an integer that ranges from 1 to 255. The default value is 3. |



Views
-----

Authentication profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After enabling the handshake with pre-connection users and authorized users using the **authentication handshake** command, you can run this command to set the handshake interval. After that, if a user does not respond to the handshake request from the device within the handshake interval, the device deletes the user entry.

**Precautions**

* 802.1X authentication users support this function when they are in the pre-connection phase, fail or succeed the authentication.
* This function takes effect only for wired users. If a wired user does not have an IP address after 30 minutes, traffic detection is performed. If traffic passes through the device, the user is not logged out. If no user traffic passes through the access device, the user is logged out.
* This function takes effect only for users who go online after the configuration is successful.
* The handshake function can be implemented by sending ARP probe packets or ND probe packets.
* If the number of ARP probe packets exceeds the default CAR value, ARP probe fails and users are logged out. To resolve this problem, the following methods are recommended:
* Ensure that the handshake period is the handshake interval multiplied by the number of handshakes.
* Increase the handshake period based on the number of users. The default handshake period is recommended when there are less than 8000 users. When there are more than 8000 users, the handshake period should be no less than 600 seconds.
* Configure port attack defense on access devices to limit the rate of packets sent to the CPU.


Example
-------

# In the authentication profile p1, set the handshake interval of the device with pre-connection users and authorized users to 200 seconds and the number of handshakes to 3.
```
<HUAWEI> system-view
[~HUAWEI] authentication-profile name p1
[*HUAWEI-authen-profile-p1] authentication timer handshake-period 200 handshake-times 3

```