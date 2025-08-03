display pim grafts
==================

display pim grafts

Function
--------



The **display pim grafts** command displays the unacknowledged Protocol Independent Multicast-Dense Mode (PIM-DM) Graft messages.




Format
------

**display pim grafts**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

On a PIM-DM network, the Device waits for an ACK message from the upstream device after it sends a Graft message. To check the PIM-DM Graft messages that have been sent but unacknowledged, run the **display pim grafts** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display unacknowledged PIM-DM Graft messages in the public network instance.
```
<HUAWEI> display pim grafts
Source                      Group                    Expire   RetransmitIn
10.0.5.200                  226.3.3.3                00:02:52 00:00:02

```

**Table 1** Description of the **display pim grafts** command output
| Item | Description |
| --- | --- |
| Source | Multicast source address. |
| Group | Multicast group address. |
| Expire | Timeout period of an (S, G) entry. |
| RetransmitIn | Time before the next Graft message is transmitted. |