dot1x timer tx-period
=====================

dot1x timer tx-period

Function
--------



The **dot1x timer tx-period** command sets the interval at which the device sends authentication requests.

The **undo dot1x timer tx-period** command restores the default configuration.



By default, the device sends authentication requests at an interval of 30 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**dot1x timer tx-period** *tx-period-value*

**undo dot1x timer tx-period**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *tx-period-value* | Specifies the interval for sending authentication requests. | The value is an integer that ranges from 1 to 120. The default value is 30. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The device starts the tx-period timer in either of the following situations:

* The device starts this timer after sending a unicast Request/Identity packet to the client. If the client does not respond within the period set by the timer, the device retransmits the authentication request.
* To authenticate the 802.1X clients that cannot initiate authentication, the device sends multicast Request/Identity packets through the 802.1X-enabled interface at the interval set by the timer.
* Generally, it is recommended that you retain the default value of the timer.


Example
-------

# Set the interval at which the device sends authentication requests to 90 seconds.
```
<HUAWEI> system-view
[~HUAWEI] dot1x timer tx-period 90

```