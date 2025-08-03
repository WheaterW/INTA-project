retry-cycle(EVPN-MAC-DUP view)
==============================

retry-cycle(EVPN-MAC-DUP view)

Function
--------



The **retry-cycle** command sets a hold-off time to unsuppress MAC duplication.

The **undo retry-cycle** command restores the default configuration.



By default, MAC duplication is unsuppressed after 540 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**retry-cycle** *retry-times*

**undo retry-cycle**

**undo retry-cycle** *retry-times*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *retry-times* | Specifies a hold-off time to unsuppress MAC duplication suppression. | The value is an integer ranging from 120 to 3600, in seconds. The value must be a multiple of 10. |



Views
-----

EVPN-MAC-DUP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On an EVPN VXLAN, two PEs may interconnect through both network-side and access-side links. If this is the case, BUM traffic loops and MAC route flapping both occur, preventing devices from working properly. In this case, MAC duplication suppression on the devices works. By default, the system checks the number of times a MAC address entry flaps within a detection period. If the number of times a MAC address entry flaps exceeds the upper threshold, the system considers MAC route flapping to be occurring on the network and consequently suppresses the flapping MAC routes. The suppressed MAC routes cannot be sent to a remote PE through a BGP EVPN peer relationship. Then, the system starts a hold-off timer to unsuppress MAC duplication. After the timer expires, MAC routes are automatically unsuppressed. To modify the hold-off time, run the **retry-cycle** command.

**Configuration Impact**

If the **retry-cycle** command is run in both EVPN instance view and global EVPN configuration view, the configuration in the EVPN instance view takes precedence.

**Precautions**

This command takes effect does not take effect for MAC/IP routes but takes effect only for MAC routes.


Example
-------

# Set the hold-off time to unsuppress MAC duplication to 200 seconds.
```
<HUAWEI> system-view
[~HUAWEI] evpn
[*HUAWEI-evpn] mac-duplication
[*HUAWEI-evpn-mac-dup] retry-cycle 200

```