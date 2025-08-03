dhcp relay reply forward all enable
===================================

dhcp relay reply forward all enable

Function
--------



The **dhcp relay reply forward all enable** command configures a DHCP relay agent to forward all DHCP ACK messages.

The **undo dhcp relay reply forward all enable** command restores the default setting.



By default, a DHCP relay agent forwards only the first received DHCP ACK message.


Format
------

**dhcp relay reply forward all enable**

**undo dhcp relay reply forward all enable**


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

**Usage Scenario**

As defined in RFC2131, the DHCP server that provides only IP addresses for DHCP clients replies with DHCP ACK messages. After receiving a DHCP ACK message, a DHCP relay agent searches for the entry based on the DHCP client's MAC address contained in the message, forwards the message to the corresponding client, and then immediately deletes the entry matching the client.If multiple DHCP servers are deployed on the network, the design of a server does not comply with standards, and a DHCP client requests for an IP address, the server does not provide an IP address for the DHCP client but replies with a DHCP ACK message. If the DHCP relay agent first receives the DHCP ACK message replied by the server, it incorrectly forwards the message to the client and deletes the corresponding entry. After the DHCP relay agent receives the correct DHCP ACK message, it cannot forward the message because the entry matching the client has been deleted. As a result, the client cannot obtain an IP address.To resolve this issue, you can run the **dhcp relay reply forward all enable** command, so that the DHCP relay agent does not immediately delete the entry matching a client after forwarding a DHCP ACK message to the client. Instead, the DHCP relay agent deletes the entry that has been aged out to ensure that the subsequently received DHCP ACK messages can be forwarded to the client.

**Prerequisites**

DHCP has been enabled globally using the **dhcp enable** command.


Example
-------

# Configure a DHCP relay agent to forward all DHCP ACK messages.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] dhcp relay reply forward all enable

```