dhcp select relay
=================

dhcp select relay

Function
--------



The **dhcp select relay** command enables the DHCP relay function.

The **undo dhcp select relay** command disables the DHCP relay function.



By default, the DHCP relay function is disabled.


Format
------

**dhcp select relay**

**undo dhcp select relay**


Parameters
----------

None

Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The dhcp select relay command applies to DHCP relay agents. If the DHCP server and client are on the same network segment, they can directly communicate with each other using DHCP. In this case, no DHCP relay agent is needed. If the DHCP server and client are on different network segments, the DHCP relay function must be enabled to forward DHCP messages.

**Prerequisites**

The DHCP function has been enabled using the **dhcp enable** command in the system view.

**Follow-up Procedure**

* To ensure that a DHCP relay agent can forward DHCP packets to a DHCP server, run the **dhcp relay server-group** or **dhcp relay server-ip** command on the DHCP relay-enabled interface to configure the correct IP address of the DHCP server.
* To ensure that a DHCP server can forward DHCP packets to a DHCP relay agent, you must configure a route to the DHCP relay agent on the DHCP server.

**Precautions**

The DHCP server must select an IP address in the same network segment with the DHCP relay agent from the global address pool to ensure that the DHCP client obtains an IP address on the local network segment. No interface address pool can be configured on the interface that connects the DHCP server and relay agent.


Example
-------

# Enable the DHCP relay function on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] dhcp select relay

```