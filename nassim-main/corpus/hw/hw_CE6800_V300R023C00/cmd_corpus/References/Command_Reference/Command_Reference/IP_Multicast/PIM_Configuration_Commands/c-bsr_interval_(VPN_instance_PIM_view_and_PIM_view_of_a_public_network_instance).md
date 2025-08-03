c-bsr interval (VPN instance PIM view/PIM view of a public network instance)
============================================================================

c-bsr interval (VPN instance PIM view/PIM view of a public network instance)

Function
--------



The **c-bsr interval** command sets the interval at which the bootstrap router (BSR) sends bootstrap messages.

The **undo c-bsr interval** command restores the default setting.



By default, the interval at which the BSR sends bootstrap messages is 60 seconds.


Format
------

**c-bsr interval** *interval*

**undo c-bsr interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies an interval at which the C-BSR sends bootstrap messages. | The value is an integer ranging from 1 to 107374177, in seconds. |



Views
-----

VPN instance PIM view,PIM view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To maintain the BSR status, a BSR dynamically elected among candidate-bootstrap routers (C-BSRs) needs to periodically send bootstrap messages carrying the BSR IP address and the rendezvous point (RP)-set information to the C-BSRs. To set the interval (called BS\_interval) at which the BSR sends bootstrap messages, run the **c-bsr interval** command.Only the BSR sends bootstrap messages, and each C-BSR starts a timer and waits to receive bootstrap messages from the BSR before the timer times out. The timeout period (called holdtime) of the timer can be configured using the **c-bsr holdtime** command.

* If a C-BSR receives a bootstrap message from the BSR, the C-BSR resets the timer.
* If a C-BSR does not receive a bootstrap message after the holdtime times out, the C-BSR considers the BSR faulty and triggers a new round of BSR election to prevent service interruptions.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.

**Configuration Impact**

If the **c-bsr interval** command is run more than once, the latest configuration overrides the previous one

**Precautions**

You must set the same BS\_interval and the same holdtime on all C-BSRs in the same PIM domain. Otherwise, a BSR may be frequently elected. Note the following points:

* If both BS\_interval and holdtime are set, ensure that BS\_interval is smaller than holdtime.
* If only BS\_interval or Holdtime is set, calculate the other one using the formula: Holdtime = 2 x BS\_interval + 10.
* If the holdtime is configured and the calculated BS\_interval is smaller than the minimum value of BS\_interval, the minimum value of BS\_interval is used.
* If the BS\_interval is configured and the calculated holdtime is greater than the maximum value of holdtime, the maximum value of holdtime is used.
* If neither the BS\_interval nor the holdtime is configured, the default values are used. The default BS\_interval is 60 seconds, and the default holdtime is 130 seconds.

Example
-------

# In the public network instance, specify 30 seconds as the interval at which the BSR sends bootstrap messages.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] c-bsr interval 30

```