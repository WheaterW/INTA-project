process-interface-status reboot-no-impact
=========================================

process-interface-status reboot-no-impact

Function
--------



The **process-interface-status reboot-no-impact** command cancels the association between a BFD session in the initial Down state with the Down state of the interface or sub-interface to which the BFD session is bound after the device restarts.

The **undo process-interface-status reboot-no-impact** command restores the default configuration. A single-hop BFD session with a multicast IP address configured as the peer address is not associated with the status of the interface to which the BFD session is bound. After the device restarts, the session in the initial Down state is not associated with the interface or sub-interface. A single-hop BFD for link-bundle session is associated with the status of the interface to which the BFD session is bound. After the device restarts, the session in the initial Down state is associated with the interface or sub-interface.



By default, a single-hop BFD session with a multicast IP address configured as the peer address is not associated with the status of the interface to which the BFD session is bound. After the device restarts, a session in the initial Down state is not associated with the interface or sub-interface. A single-hop BFD for link-bundle session is associated with the interface to which the BFD session is bound. After the device restarts, a session in the initial Down state is associated with the interface or sub-interface.


Format
------

**process-interface-status reboot-no-impact**

**undo process-interface-status reboot-no-impact**


Parameters
----------

None

Views
-----

BFD session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



After associating the status of a multicast BFD session or a BFD for link-bundle session with the status of an interface, you can run the **process-interface-status reboot-no-impact** command to cancel the association between the initial Down state and the Down state of the interface or sub-interface after the device restarts.



**Prerequisites**



A multicast IP single-hop BFD session or link-bundle single-hop BFD session has been configured.



**Configuration Impact**



After the **process-interface-status reboot-no-impact** command is run, once the device restarts, the initial Down state of a single-hop BFD session with a multicast IP address configured as the peer address or a single-hop BFD for link-bundle session is not associated with the Down state of the interface or sub-interface to which the BFD session is bound.



**Precautions**

* If multiple single-hop BFD sessions with a multicast IP address configured as the peer address are bound to the same interface, the **process-interface-status reboot-no-impact** command can be configured only for one BFD session. In other words, the interface status is affected by only one BFD session. Between link-bundle sessions and multicast sessions, and between link-bundle sessions, one interface can be bound to multiple BFD sessions enabled with the **process-interface-status** command.
* Before you associate the BFD status with the interface status, ensure that the BFD configurations on two devices are correct and consistent. If the local BFD session is in the Down state, check whether the BFD configuration on the peer device is correct and whether the remote BFD session is shut down.
* After the shutdown command is run, the BFD session status will not be reported to the bound interface.
* After the device restarts, the associated interface protocol goes down. After the session goes up or AdminDown, the associated interface protocol goes up. If the interface status is up before the restart, the BFD session cannot go up after the restart. As a result, the interface protocol status before and after the restart is inconsistent.You can run the **process-interface-status reboot-no-impact** command in the session view to prevent association.


Example
-------

# Cancel the association between a link-bundle single-hop BFD session and the interface to which the BFD session is bound.
```
<HUAWEI> system-view
[~HUAWEI] interface Eth-Trunk 1
[*HUAWEI-Eth-Trunk1] ip address 10.1.1.1 24
[*HUAWEI-Eth-Trunk1] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] eth-trunk 1
[*HUAWEI-100GE1/0/1] quit
[*HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] bfd test bind link-bundle peer-ip 10.1.1.2 interface Eth-Trunk 1 source-ip 10.1.1.1
[*HUAWEI-bfd-session-test] process-interface-status reboot-no-impact

```