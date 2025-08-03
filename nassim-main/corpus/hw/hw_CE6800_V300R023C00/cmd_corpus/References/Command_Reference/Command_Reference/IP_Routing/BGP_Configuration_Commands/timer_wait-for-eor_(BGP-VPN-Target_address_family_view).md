timer wait-for-eor (BGP-VPN-Target address family view)
=======================================================

timer wait-for-eor (BGP-VPN-Target address family view)

Function
--------



The **timer wait-for-eor** command sets the maximum time for the BGP-VPN-Target address family to wait for the End-Of-RIB flag.

The **undo timer wait-for-eor** command restores the default setting.



By default, the period is 180s.


Format
------

**timer wait-for-eor** *eor-time*

**undo timer wait-for-eor**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *eor-time* | Specifies the maximum time to wait for the end flag of RIB route sending. | The value is an integer ranging from 3 to 3000, in seconds. |



Views
-----

BGP-VPN-target address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



In a VPN ORF-enabled scenario, when a BGP session is established or reestablished, if no End-Of-RIB flag is received from the BGP-VPN-Target address family within the period set using the **timer wait-for-eor** command, EVPN route advertisement is not triggered during this period. If a device receives an End-Of-RIB flag from the BGP-VPN-Target address family within the specified period, the device immediately advertises EVPN routes. If the device does not receive the End-Of-RIB flag from the BGP-VPN-Target address family within the period set using this command, EVPN route advertisement is triggered immediately.




Example
-------

# Set the period during which the BGP-VPN-Target address family waits for the End-Of-RIB flag to 100s.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-target
[*HUAWEI-af-vpn-target] timer wait-for-eor 100

```