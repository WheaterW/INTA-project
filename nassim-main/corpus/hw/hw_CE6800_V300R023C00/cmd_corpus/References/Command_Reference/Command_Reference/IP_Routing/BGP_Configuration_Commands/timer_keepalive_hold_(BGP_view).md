timer keepalive hold (BGP view)
===============================

timer keepalive hold (BGP view)

Function
--------



The **timer keepalive hold** command sets the Keepalive time and hold time.

The **undo timer keepalive hold** command restores the default Keepalive time and hold time.



By default, the Keepalive time is 60s, and the hold time is 180s.


Format
------

**timer keepalive** *keepalive-time* **hold** *hold-time* [ **min-holdtime** *min-hold-value* ]

**undo timer keepalive hold** [ **min-holdtime** ]

**undo timer keepalive** *keepalive-time* **hold** *hold-time* [ **min-holdtime** *min-hold-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **hold** *hold-time* | Specifies the hold time. | The value is 0 or an integer ranging from 3 to 65535, in seconds. The default value is 180.  It is recommended that the configured hold time be related to the total number of BGP address family peers. For details, see the mapping between the total number of BGP peers in each address family and the recommended minimum hold time in the usage guide of the peer timer command. |
| **min-holdtime** *min-hold-value* | Specifies the minimum hold time. On the same device, min-hold-value must be less than hold-time. | The value is an integer ranging from 20 to 65535, in seconds. |
| **keepalive** *keepalive-time* | Specifies the Keepalive time. | The value is an integer ranging from 0 to 21845, in seconds. The default value is 60. |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After a connection is established between peers, keepalive-time and hold-time are negotiated by the peers.

* The smaller hold-time carried by Open messages of both peers is used as the hold-time.
* The smaller value of one third of hold-time and the locally configured keepalive-time is used as the keepalive-time.If the hold time configured on a remote device is less than the min-hold-value configured on the local device, no BGP peer relationship can be established between the two devices. However, if the hold time configured on the remote device is 0s, a BGP peer relationship can be established between the two devices.

**Configuration Impact**



The timers configured for a specific peer or peer group using the **peer timer** command override the timers configured for all BGP peers using the **timer** command.



**Precautions**

If the value of a timer changes, the BGP peer relationship between devices is interrupted. This is because the peers need to renegotiate the values of keepalive-time and hold-time. Exercise caution when changing the value of the timer.In actual configuration, the hold time must be at least three times the Keepalive time. Avoid the following situations:

* Both keepalive-time and hold-time are set to 0. In this case, the BGP timers become invalid. That is, BGP does not detect link faults based on the timers.
* The hold-time value is much greater than the keepalive-time value. For example, if the **timer keepalive 1 hold 65535** command is run, link faults cannot be detected in time.


Example
-------

# Set the Keepalive time, hold time, and minimum hold time to 30s, 90s, and 60s, respectively.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] timer keepalive 30 hold 90 min-holdtime 60

```

# Set the BGP Keepalive time to 30s and hold time to 90s.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] timer keepalive 30 hold 90

```