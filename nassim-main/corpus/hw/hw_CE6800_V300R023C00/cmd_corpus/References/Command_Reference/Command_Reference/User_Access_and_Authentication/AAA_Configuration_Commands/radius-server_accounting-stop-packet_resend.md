radius-server accounting-stop-packet resend
===========================================

radius-server accounting-stop-packet resend

Function
--------

The **radius-server accounting-stop-packet resend** command enables retransmission of accounting-stop packets and sets the number of accounting-stop packets that can be retransmitted each time.

The **undo radius-server accounting-stop-packet resend** command is used to restore the default configuration.

By default, retransmission of accounting-stop packets is enabled, and the retransmission times is 3.



Format
------

**radius-server accounting-stop-packet resend** [ *resend-times* ]

**undo radius-server accounting-stop-packet resend**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *resend-times* | Specifies the number of accounting-stop packets that can be retransmitted each time. | The value is an integer that ranges from 0 to 300. |




Views
-----

RADIUS server template view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

When accounting-stop packets cannot be sent to the RADIUS server that is unreachable, you can run the **radius-server accounting-stop-packet resend** command to save the accounting-stop packets in the buffer and send them at the preset intervals until the number of allowed retransmissions is reached or the packets are sent successfully.

The number of times that accounting stop packets are retransmitted is the sum of the number of times that accounting stop packets are retransmitted configured using the
**radius-server retransmit** command and the number of times that accounting stop packets are allowed to be retransmitted using the
**radius-server accounting-stop-packet resend** command.

Example
-------

# Enable the retransmission of accounting-stop packets and set the number of accounting-stop packets that can be retransmitted each time to 50.
```
<HUAWEI> system-view
[~HUAWEI] radius-server template test1
[*HUAWEI-radius-test1] radius-server accounting-stop-packet resend 50

```