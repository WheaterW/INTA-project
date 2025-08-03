authentication handshake
========================

authentication handshake

Function
--------



The **authentication handshake** command enables the handshake with pre-connection users and authorized users.

The **undo authentication handshake** command disables the handshake with pre-connection users and authorized users.



By default, the handshake with pre-connection users and authorized users is enabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**authentication handshake**

**undo authentication handshake**


Parameters
----------

None

Views
-----

Authentication profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The device creates entries for pre-connection users, users who fail to be authenticated and are assigned network access rights, and users who are authenticated. After users go offline in normal situations, the system immediately deletes the corresponding user entries. However, if some users go offline due to exceptions such as network disconnections, the system cannot immediately delete the corresponding user entries. If there are a large number of such user entries, other users may fail to access the network.To solve this problem, run the **authentication handshake** command to enable the handshake with pre-connection users and authorized users. If a user does not respond to the handshake request from the device within the handshake period (handshake interval x number of handshakes) (configured using the **authentication timer handshake-period handshake-times** command), the device deletes the user entry.

**Precautions**

* 802.1X authentication users support this function when they are in the pre-connection phase, fail or succeed the authentication.
* This function takes effect only for wired users who have obtained IP addresses. If a user does not obtain an IP address, the device does not detect the user within 30 minutes. After 30 minutes, the device waits for another handshake period. If a user does not generate traffic within the handshake period, the device disconnects the user.
* The handshake function is implemented using ARP probe packets or neighbor discovery (ND) probe packets.
* The handshake function can also be implemented by detecting whether there is user traffic on the access device. Assuming that the handshake period is 3n, the device will detect user traffic at n and 2n. The 0-n time range is used as an example. The n-2n time range is similar to the 0-n time range.
* If user traffic passes through the device within the period from 0 to n, the device considers that the user is online at n, does not send probe packets at that time, and resets the number of handshakes.
* If no user traffic passes the device during the 0-n period, the device cannot detect whether the user is online at n and sends a probe packet.
* If the device receives the response packet from the user, it considers the user online and resets the number of handshakes. If the device does not receive the response packet, it considers the user offline.
* If user traffic passes through the device within the period from 2n to 3n, the device considers that the user is online at 3n and resets the number of handshakes.
* If no user traffic passes through the device within the period from 2n to 3n, the device cannot detect whether the user is online at 3n and considers that the user is offline.
* If the device considers that the user is offline at n, 2n, or 3n, the device deletes all entries of the user. To prevent users from going offline unexpectedly when no operation is performed on the PC, do not set a short handshake period.


Example
-------

# In the authentication profile p1, enable the handshake with pre-connection users and authorized users.
```
<HUAWEI> system-view
[~HUAWEI] authentication-profile name p1
[*HUAWEI-authen-profile-p1] authentication handshake

```