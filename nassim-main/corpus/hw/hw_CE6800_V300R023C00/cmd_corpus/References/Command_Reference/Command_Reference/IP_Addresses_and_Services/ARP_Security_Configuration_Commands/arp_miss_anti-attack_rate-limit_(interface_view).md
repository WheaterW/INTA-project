arp miss anti-attack rate-limit (interface view)
================================================

arp miss anti-attack rate-limit (interface view)

Function
--------



The **arp miss anti-attack rate-limit** command sets a rate limit for ARP Miss messages on an interface.

The **undo arp miss anti-attack rate-limit** command restores the default rate limit for ARP Miss messages on an interface.



By default, the rate of ARP Miss messages on an interface is not limited.


Format
------

**arp miss anti-attack rate-limit** *maximum*

**undo arp miss anti-attack rate-limit**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *maximum* | Specifies a rate limit for ARP Miss messages on an interface. | The value is an integer ranging from 0 to 65536, in pps. 0 indicates that ARP Miss message rate limiting is disabled. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,1200ge sub-interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To prevent a device from sending a large number of broadcast ARP requests triggered by ARP Miss messages, run the arp miss anti-attack rate-limit command on the upstream interface to set a rate limit for ARP Miss messages.


Example
-------

# Set the rate limit to 100 pps for ARP Miss messages.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] arp miss anti-attack rate-limit 100

```