hwtacacs-server accounting-stop-packet resend
=============================================

hwtacacs-server accounting-stop-packet resend

Function
--------

The **hwtacacs-server accounting-stop-packet resend** command enables retransmission of accounting-stop packets and sets the number of accounting-stop packets that can be retransmitted each time.

By default, three accounting-stop packets can be retransmitted each time.



Format
------

**hwtacacs-server accounting-stop-packet resend** { **disable** | **enable** *number* }



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **disable** | Disables the retransmission of accounting-stop packets. | - |
| **enable** *number* | Enables the retransmission of accounting-stop packets, and specifies the number of packets that can be retransmitted each time. | The value is an integer that ranges from 1 to 300. The default value is 3. |




Views
-----

System view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

After a user goes offline, the device sends an accounting-stop packet to an accounting server. After the accounting server receives the accounting-stop packet, it stops accounting for the user. If the accounting server does not receive the accounting-stop packet because of network faults, it continues to perform accounting for the user. As a result, the user is charged incorrectly. To solve this problem, configure the device to send accounting-stop packets multiple times.

**Precautions**

If the **disable** parameter is configured, an accounting-stop packet is sent only once and will not be retransmitted even if the packet fails to be sent.

If the
**enable**
*number*parameter is configured, an accounting-stop packet is retransmitted if no response is returned or transmission fails. number specifies the number of retransmitted accounting-stop packets.

Example
-------

# Enable the retransmission of accounting-stop packets and set the number of accounting-stop packets that can be retransmitted each time to 50.
```
<HUAWEI> system-view
[~HUAWEI] hwtacacs-server accounting-stop-packet resend enable 50

```