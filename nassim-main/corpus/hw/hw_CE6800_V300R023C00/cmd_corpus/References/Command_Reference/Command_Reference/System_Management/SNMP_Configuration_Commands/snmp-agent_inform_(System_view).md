snmp-agent inform (System view)
===============================

snmp-agent inform (System view)

Function
--------



The **snmp-agent inform** command sets global parameters of Inform messages. The parameters include the timeout period for waiting for Inform ACK messages, number of times to retransmit Inform messages, and maximum number of Inform messages to be confirmed in the inform buffer.

The **undo snmp-agent inform** command restores the default parameters.



By default, the time-out waiting period for Inform ACK messages is 15 seconds, the number of times to retransmit Inform messages is 3, and the maximum number of informs in the inform buffer is 39.


Format
------

**snmp-agent inform** { **timeout** *seconds* | **resend-times** *times* | **pending** *number* } \*

**undo snmp-agent inform** { **timeout** [ *seconds* ] | **resend-times** [ *times* ] | **pending** [ *number* ] } \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **timeout** *seconds* | Specified the timeout period for waiting for Inform ACK messages from the NMS. | The value is an integer ranging from 1 to 1800, in seconds. The default value is 15, which is equal to the global timeout period configured using the snmp-agent inform command. |
| **resend-times** *times* | Specifies the maximum number of attempts to retransmit an Inform message if no Inform ACK message is returned by the NMS. | The value is an integer ranging from 0 to 10. The default value is 3, which is equal to the global retransmission times configured using the snmp-agent inform command. |
| **pending** *number* | Specifies the maximum number of Inform messages to be confirmed in the inform buffer. | The value is an integer ranging from 1 to 2048. The default value is 39. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

After sending an Inform message, an SNMP agent waits for an Inform ACK message sent by the NMS. You can run the **snmp-agent inform** command to set the timeout, resend-times, and pending parameters for Inform messages.These three parameters affect one another. For example, if the timeout period for waiting for Inform ACK messages prolongs or the number of attempts to retransmit Inform messages increases, but the maximum number of Inform messages to be confirmed is not changed, the number of Inform messages to be confirmed increases, causing the inform buffer to be quickly filled up.Once the inform buffer is filled up, the earliest Inform message in the inform buffer is deleted each time a new Inform message enters the queue. The deleted Inform messages are not retransmitted to the NMS. To prevent this problem, increase the maximum number of Inform messages to be confirmed in the inform buffer.You can configure the **snmp-agent inform** command to contain the parameter timeout, resend-times, or pending as needed.

* If a large number of Inform messages are lost on a network, you can run the snmp-agent inform pending *number*command to increase the Inform buffer.
* If the network transmission speed is low, you are advised to increase the timeout period. Increasing the timeout period will increase the waiting time of Inform messages in the Inform buffer. You can also run the snmp-agent inform { timeout *seconds*| pending *number*} \* command to increase the inform message.
* If the transmission speed on the network is high, run the snmp-agent inform timeout *seconds*command to reduce the timeout period.
* If Inform messages are transmitted on an unreliable network, you are advised to increase the number of retransmission times. In this case, the Inform messages in the Inform buffer need to wait for a longer time to be confirmed. You are advised to run the snmp-agent inform { resend-times *times*| pending *number*} \* command to increase the inform buffer.

**Prerequisites**

Parameters for sending Inform messages take effect only after the IP address of the target host for receiving Inform messages is configured using the **snmp-agent target-host inform** command.The IP address of the target host for receiving Inform messages has been configured using the **snmp-agent target-host inform** command.

**Configuration Impact**

You must set suitable parameters timeout, resend-times, and pending. Setting an inappropriate parameter deteriorates SNMP working efficiency.

**Precautions**

Only parameters for sending Inform messages need to be configured using the **snmp-agent inform address** command. Parameters for sending trap messages do not need to be configured.


Example
-------

# Set the times to retransmit an Inform message to 5 and the maximum number of Inform messages waiting to be confirmed in the inform buffer to 100.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent inform resend-times 5 pending 100

```