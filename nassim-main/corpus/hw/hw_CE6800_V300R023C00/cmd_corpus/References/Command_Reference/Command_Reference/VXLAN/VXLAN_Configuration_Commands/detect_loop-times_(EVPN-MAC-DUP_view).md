detect loop-times (EVPN-MAC-DUP view)
=====================================

detect loop-times (EVPN-MAC-DUP view)

Function
--------



The **detect loop-times** command sets loop detection parameters for MAC duplication suppression.

The **undo detect loop-times** command restores the default configuration.



By default, the loop detection period for MAC duplication suppression is 180s, and the threshold for MAC entry flaps is 5 within a detection period.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**detect loop-times** *loop-times* **detect-cycle** *detect-cycle-time*

**undo detect loop-times detect-cycle**

**undo detect loop-times** *loop-times* **detect-cycle** *detect-cycle-time*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *loop-times* | Specifies the maximum number of times MAC entry flapping is allowed in a detection period. | The value is an integer ranging from 3 to 10. |
| **detect-cycle** *detect-cycle-time* | Specifies a detection period. | The value is an integer ranging from 60 to 900, in seconds. The value must be a multiple of 10. |



Views
-----

EVPN-MAC-DUP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On an EVPN VXLAN network, two PEs may interconnect through both network-side and access-side links. If this is the case, BUM traffic loops and MAC route flapping both occur, preventing devices from working properly. In this case, MAC duplication suppression on the devices works. By default, the system checks the number of times a MAC address entry flaps within a detection period (180s by default). If the number of times a MAC address entry flaps exceeds the upper threshold (5 by default), the system considers MAC route flapping to be occurring on the network and consequently suppresses the flapping MAC routes. The suppressed MAC routes cannot be sent to a remote PE through a BGP EVPN peer relationship. To modify the detection period or the threshold for MAC address entry flapping, run the **detect loop-times** command.

**Configuration Impact**

If the **detect loop-times** command is run in both EVPN instance view and global EVPN configuration view, the configuration in the EVPN instance view takes precedence.

**Precautions**

This command takes effect does not take effect for MAC/IP routes but takes effect only for MAC routes.


Example
-------

# Set loop detection parameters for MAC duplication suppression.
```
<HUAWEI> system-view
[~HUAWEI] evpn
[*HUAWEI-evpn] mac-duplication
[*HUAWEI-evpn-mac-dup] detect loop-times 4 detect-cycle 100

```