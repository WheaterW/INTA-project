mac-address m-lag notification disable
======================================

mac-address m-lag notification disable

Function
--------



The **mac-address m-lag notification evpn disable** command enables a device not to send the MAC address of the VBDIF interface synchronized from the peer device to EVPN in an M-LAG scenario.

The **undo mac-address m-lag notification evpn disable** command disables a device from not sending the MAC address of the VBDIF interface synchronized from the peer device to EVPN in an M-LAG scenario.

The **mac-address m-lag notification vbdif disable** command enables a device not to synchronize the MAC address of the VBDIF interface to the peer device in an M-LAG scenario.

The **undo mac-address m-lag notification vbdif disable** command disables a device from not synchronizing the MAC address of the VBDIF interface to the peer device in an M-LAG scenario.

The **mac-address m-lag notification vlanif disable** command enables a device not to synchronize the MAC address of the VLANIF interface to the peer device in an M-LAG scenario.

The **undo mac-address m-lag notification vlanif disable** command disables a device from not synchronizing the MAC address of the VLANIF interface to the peer device in an M-LAG scenario.



By default, DeviceA synchronizes the MAC address of the local VLANIF/VBDIF interface to DeviceB in an M-LAG scenario. In the M-LAG scenario, after receiving the MAC address of the VBDIF interface synchronized from DeviceA, DeviceB sends the MAC address to the EVPN.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**mac-address m-lag notification evpn disable**

**mac-address m-lag notification vbdif disable**

**undo mac-address m-lag notification evpn disable**

**undo mac-address m-lag notification vbdif disable**

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**mac-address m-lag notification vlanif disable**

**undo mac-address m-lag notification vlanif disable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

In an M-LAG, DeviceA synchronizes the MAC address of the local VLANIF interface to DeviceB. The MAC address occupies resources in the software MAC address table of DeviceB, which may affect the number of MAC addresses that can be dynamically learned by DeviceB. You can run the **mac-address m-lag notification Vlanif disable** command to disable DeviceA from synchronizing the MAC address of the VLANIF interface to DeviceB in the M-LAG.In an M-LAG, DeviceA synchronizes the MAC address of the local VBDIF interface to DeviceB. The MAC address occupies resources in the software MAC address table of DeviceB, which may affect the number of MAC addresses that can be dynamically learned by DeviceB. You can run the **mac-address m-lag notification Vbdif disable** command to disable DeviceA from synchronizing the MAC address of the VBDIF interface to DeviceB in the M-LAG.In an M-LAG, DeviceA synchronizes the MAC address of the local VBDIF interface to DeviceB. After receiving the MAC address of the VBDIF interface synchronized from DeviceA, DeviceB sends the MAC address to EVPN, occupying resources in the EVPN table. You can run the **mac-address m-lag notification evpn disable** command to disable DeviceB from sending the MAC address of the VBDIF interface synchronized from DeviceA to EVPN.


Example
-------

# Configure a device not to send the MAC address of the VBDIF interface synchronized from the peer device to EVPN in an M-LAG scenario.
```
<HUAWEI> system-view
[~HUAWEI] mac-address m-lag notification evpn disable

```