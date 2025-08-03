timer keepalive hold (BGP multi-instance view)
==============================================

timer keepalive hold (BGP multi-instance view)

Function
--------



The **timer keepalive hold** command sets the Keepalive time and hold time of BGP.

The **undo timer keepalive hold** command restores the default Keepalive time and hold time.

The **timer send-hold** command sets the hold time of a BGP session on the sender.

The **undo timer send-hold** command restores the default value of the hold time of a BGP session on the sender.



By default, the keepalive time is 60s, the hold time is 180s, and the session hold time is 86400s.


Format
------

**timer keepalive** *keepalive-time* **hold** *hold-time* [ **min-holdtime** *min-hold-value* ]

**timer send-hold** *send-hold-time*

**undo timer keepalive hold** [ **min-holdtime** ]

**undo timer keepalive** *keepalive-time* **hold** *hold-time* [ **min-holdtime** *min-hold-value* ]

**undo timer send-hold** *send-hold-time*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **hold** *hold-time* | Specifies the hold time. | The value is 0 or an integer ranging from 3 to 65535, in seconds. The default value is 180.  It is recommended that the configured hold time be related to the total number of BGP address family peers. For details, see the mapping between the total number of BGP peers in each address family and the recommended minimum hold time in the usage guide of the peer timer command. |
| **min-holdtime** *min-hold-value* | Specifies the minimum hold time. On the same device, min-hold-value must be less than hold-time. | The value is an integer ranging from 20 to 65535, in seconds. |
| **send-hold** *send-hold-time* | Specifies the interval for holding a session when the local end fails to send messages. | The value is 0 or an integer ranging from 360 to 172800, in seconds. The default value is 86400. The value 0 indicates that the function is disabled. |
| **keepalive** *keepalive-time* | Specifies the Keepalive time. | The value is an integer ranging from 0 to 21845, in seconds. The default value is 60. |



Views
-----

BGP multi-instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After a connection is established between peers, the values of keepalive-time and hold-time are negotiated by the peers. In the preceding information:

* The smaller hold-time value in Open messages sent by both peers is used as the hold-time value.
* The smaller value between the negotiated hold-time value divided by 3 and the locally configured keepalive-time value is used as the keepalive-time value.If the hold time configured on the peer is smaller than min-hold-value configured on the local device, the two devices cannot establish a peer relationship. If the hold time configured for a peer is 0, the rule does not take effect and the peer relationship can still be established.The send-hold-time value is used to set the session hold time. If both BGP Update and Keepalive messages fail to be sent within twice the hold-time, an alarm is reported. If the alarm is not cleared within the period specified by send-hold-time, the BGP connection is reset.

**Configuration Impact**



The timers configured for a specific peer or peer group using the **peer timer** command override the timers configured for all BGP peers using the **timer** command.



**Precautions**

If the value of a timer changes, the BGP peer relationship between devices is interrupted. This is because the peers need to renegotiate the values of keepalive-time and hold-time. Exercise caution when changing the value of the timer.In actual configuration, the hold time must be at least three times the Keepalive time. Avoid the following situations:

* Both keepalive-time and hold-time are set to 0. In this case, the BGP timers become invalid. That is, BGP does not detect link faults based on the timers.
* The hold-time value is much greater than the keepalive-time value. For example, if the **timer keepalive 1 hold 65535** command is run, link faults cannot be detected in time.
* Keepalive-time is set to 0. In this case, the keepalive timer is not started and the send-hold timer function does not take effect.BGP messages are sent to peers through an update peer-group. When there is only one peer in the update peer-group or there is no message in the update peer-group, the session hold time does not take effect.


Example
-------

# Set the Keepalive time, hold time, and minimum hold time to 30s, 90s, and 60s, respectively.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] timer keepalive 30 hold 90 min-holdtime 60

```

# On a BGP device, set the Keepalive time to 30s and the hold time to 90s.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] timer keepalive 30 hold 90

```

# Set the BGP session hold time to 720 seconds.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] timer send-hold 720

```