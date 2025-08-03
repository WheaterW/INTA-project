wtr
===

wtr

Function
--------



The **wtr** command sets a wait-to-restore (WTR) time for a BFD session.

The **undo wtr** command restores the default value.



By default, the value is 0, indicating no waiting.


Format
------

**wtr** *wtr-value*

**undo wtr** [ *wtr-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **wtr** *wtr-value* | Specifies a WTR time for a BFD session. | The value is an integer ranging from 1 to 60, in minutes. |



Views
-----

BFD session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If a BFD session flaps, you can run this command to decrease service flapping caused by the BFD session.

**Prerequisites**

A BFD session has been created.

**Configuration Impact**

If the WTR time is configured, the event that the session becomes Up is reported to the applications after the WTR time expires. Other events are reported immediately.

**Precautions**



The WTR times on both ends of a BFD session must be the same; otherwise, when the session status changes on one end, the application on the other end detects the incorrect BFD session status.The WTR time takes effect for BFD for link-bundle and BFD for per-link sessions, but not their sub-sessions, because the sub-sessions do not directly participate in service association.




Example
-------

# Set the WTR time of the BFD session to 10 minutes.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] bfd s1 bind peer-ip 10.10.20.2
[*HUAWEI-bfd-session-s1] wtr 10

```