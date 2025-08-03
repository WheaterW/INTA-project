trunk member-port-inspect
=========================

trunk member-port-inspect

Function
--------



The **trunk member-port-inspect** command enables a device to monitor Layer 3 trunk member interfaces.

The **undo trunk member-port-inspect** command disables a device from monitoring Layer 3 trunk member interfaces.



By default, a device is disabled from monitoring Layer 3 trunk member interfaces.


Format
------

**trunk member-port-inspect**

**undo trunk member-port-inspect**


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



Multiple physical interfaces can be bundled into a logical interface, which is called a trunk interface. The physical interfaces are the trunk interface's member interfaces. If the **ping** command is run to test a trunk interface, the local device sends a ping packet to the remote device through a member interface. The remote device may select any member interface to send a reply packet back to the local device. When the quality of services carried on the trunk interface deteriorates greatly, users cannot determine which member interface of the trunk interface fails.The **trunk member-port-inspect** command can be run on the receive side to ping each trunk member interface to monitor the status of the end-to-end link on each member interface. After the receive side receives a ping packet through the trunk interface, it uses the member interface directly connected to the transmit side to send a reply packet back, monitoring the status of the end-to-end link on a specified member interface and in turn determining the faulty trunk member interface. After this command is run to enable a device to monitor Layer 3 trunk member interfaces, ICMP echo reply packets are sent through the inbound interface of ICMP echo request packets.



**Precautions**



The **trunk member-port-inspect** command is applicable only to the scenarios where trunk interfaces or Eth-Trunk sub-interfaces are directly connected, and it takes effect only when the fast reply function is disabled.




Example
-------

# Enable a device to monitor Layer 3 trunk member interfaces.
```
<HUAWEI> system-view
[~HUAWEI] trunk member-port-inspect

```