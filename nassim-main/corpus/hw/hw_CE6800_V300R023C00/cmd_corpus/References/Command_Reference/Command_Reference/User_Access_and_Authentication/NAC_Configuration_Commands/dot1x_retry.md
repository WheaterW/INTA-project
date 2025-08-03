dot1x retry
===========

dot1x retry

Function
--------



The **dot1x retry** command configures the number of times an authentication request or handshake packet is retransmitted to an 802.1X user.

The **undo dot1x retry** command restores the default configuration.



By default, the device can retransmit an authentication request or handshake packet to an 802.1X user twice.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**dot1x retry** *max-retry-value*

**undo dot1x retry**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *max-retry-value* | Specifies the number of times an authentication request or handshake packet is retransmitted to an 802.1X user. | The value is an integer that ranges from 1 to 10. The default value is 2. |



Views
-----

802.1X access profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the device does not receive any response from a user within a specified time after sending an authentication request or handshake packet to the user, the device sends the authentication request or handshake packet again. If the authentication request or handshake packet has been sent for the maximum retransmission times and no response is received, the user authentication or handshake fails. In this process, the total number of authentication requests or handshake packets sent by the device is max-retry-value plus 1.

**Precautions**

Repeated authentication requests occupy a lot of system resources. When using the dot1x retry command, you can set the maximum number of times according to user requirements and device resources. The default value is recommended.


Example
-------

# In the 802.1X access profile d1, configure the number of times an authentication request or handshake packet can be retransmitted to 802.1X users to 4.
```
<HUAWEI> system-view
[~HUAWEI] dot1x-access-profile name d1
[~HUAWEI-dot1x-access-profile-d1] dot1x retry 4

```