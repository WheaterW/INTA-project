smart-link flush receive control-vlan
=====================================

smart-link flush receive control-vlan

Function
--------



The **smart-link flush receive control-vlan** command enables a device to receive Flush packets and specifies the control VLAN ID and password for receiving Flush packets.

The **undo smart-link flush receive** command disables a device from receiving Flush packets.



By default, an interface is disabled from receiving Flush packets.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**smart-link flush receive control-vlan** *vlan-id* [ **password** { **sha** | **simple** | **hmac-sha256** } *password* ]

**undo smart-link flush receive**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vlan-id* | Specifies the control VLAN ID of Smart Link Flush packets. | The value is an integer ranging from 1 to 4094. |
| **password** | Specifies the encryption mode of the password in Flush packets. | - |
| *password* | Specifies a password carried in Flush packets. | The value is a string of 1 to 16 case-sensitive characters or a string of 24, 32, or 48 case-sensitive characters.   * If the password is a simple password, the value is a string of 1 to 16 characters. * If the password is encrypted using SHA or HMAC SHA256, the value is a string of 48 characters. * If the source version supports a ciphertext password of 24 or 32 characters, the target version is automatically compatible with the ciphertext password. |
| **sha** | Specifies the password of Flush packets is in SHA encryption mode. | - |
| **simple** | Specifies the password of Flush packets is in simple text. | - |
| **hmac-sha256** | Specifies the password of Flush packets is in HMAC-SHA256 encryption mode. | - |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

* When a link switchover occurs in a Smart Link group, the existing forwarding entries no longer apply to the new topology. Therefore, the MAC address entries and ARP entries on the entire network need to be updated. The Smart Link group sends Flush packets to notify upstream devices of the topology change. Upstream devices can update their MAC address entries and ARP entries only if they are enabled to receive Flush packets. If a device rejects Flush packets, it cannot forward packets correctly after a link failover occurs in the Smart Link group.

**Prerequisites**

A Smart Link group on a downstream device has been enabled to send Flush packet using the **flush send** command.

**Precautions**

* After you run this command to configure the encryption mode and password, the original encryption mode and password are deleted. If the control VLAN ID is changed, the password must be reconfigured.
* If a password is encrypted in SHA or HMAC SHA256 mode, the password cannot be restored after being configured. If you forget the password, you need to reconfigure it.
* This command does not add an interface to the control VLAN. You need to configure the interface to allow packets of the control VLAN to pass through. Flush packets can be received only when the control VLAN ID and password in the Flush packet are the same as the configured control VLAN ID and password. The Flush packets that do not meet the requirements are discarded.
* The format of Flush packets varies according to device manufacturers. Therefore, Flush packets are used only for communication between Huawei switching devices.
* If you do not specify a password for receiving Flush packets or specify a simple password for receiving Flush packets, security problems may occur.

Example
-------

# Configure 100GE1/0/1 to receive Flush packets with control VLAN ID 100 and password YsHsjx\_202206.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] smart-link flush receive control-vlan 100 password sha YsHsjx_202206

```