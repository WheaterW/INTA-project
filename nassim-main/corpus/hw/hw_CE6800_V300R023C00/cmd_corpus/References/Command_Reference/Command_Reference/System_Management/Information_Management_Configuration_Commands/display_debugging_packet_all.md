display debugging packet all
============================

display debugging packet all

Function
--------



The **display debugging packet all** command displays whether debugging information about all protocol packets is displayed and the timeout period for displaying debugging information.




Format
------

**display debugging packet all**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

After the following operations are performed, you can run the **display debugging packet all** command to check whether debugging information about all protocol packets is displayed and the timeout period for displaying debugging information:

* Run the **debugging packet filter** command to set the filter condition for displaying debugging information about protocol packets.
* Run the **debugging packet timeout timeout\_value** command to set the timeout period for displaying debugging information about protocol packets.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display whether debugging information is displayed for all protocol packets and the timeout period for displaying debugging information.
```
<HUAWEI> display debugging packet all
[Y] : The packet of specified type will display
L2:  Application [Y]  Link [Y]
L3:  Application [Y]  Transport [N]  Ipv4 [Y]  Ipv6 [Y]
Ingress/Egress:  Ingress [Y]  Egress [Y]

Debugging time left: 8(s)

```

**Table 1** Description of the **display debugging packet all** command output
| Item | Description |
| --- | --- |
| Application | A terminal outputs debugging information about protocol packets at the application layer. |
| Link | A terminal outputs debugging information about protocol packets at the link layer. |
| Transport | A terminal outputs debugging information about protocol packets at the transport layer. |
| Ipv4 | A terminal outputs debugging information about IPv4 protocol packets. |
| Ipv6 | A terminal outputs debugging information about IPv6 protocol packets. |
| Ingress | A terminal outputs debugging information about protocol packets on the inbound interface. |
| Egress | A terminal outputs debugging information about protocol packets on the outbound interface. |
| Debugging time left | Whether a terminal sets the timeout interval for tracing protocol packets.   * After the debugging packet timeout command is run to set the timeout interval for tracing protocol packets, the specific interval is displayed here. * If the timeout interval for tracing protocol packets is not set, the following information is displayed: No debugging timeout. |
| [Y] | A terminal outputs debugging information about the specified protocol packets. |
| [N] | A terminal does not output debugging information about the specified protocol packets. |
| L2 | A terminal outputs debugging information about protocol packets at Layer 2. |
| L3 | A terminal outputs debugging information about protocol packets at Layer 3. |