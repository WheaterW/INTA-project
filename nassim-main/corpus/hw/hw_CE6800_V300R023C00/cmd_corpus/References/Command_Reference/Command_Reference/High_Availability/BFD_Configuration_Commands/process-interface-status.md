process-interface-status
========================

process-interface-status

Function
--------



The **process-interface-status** command associates the status of a BFD session with the status of the interface to which the BFD session is bound.

The **undo process-interface-status** command cancels the association between the status of a BFD session and the status of the interface to which the BFD session is bound.



By default, the status of the multicast IP single-hop BFD session is not associated with the status of the bound interface, and the status of the link-bundle single-hop BFD session is associated with the status of the bound interface.


Format
------

**process-interface-status** [ **sub-if** ] [ **reboot-no-impact** ]

**undo process-interface-status** [ **sub-if** ] [ **reboot-no-impact** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **sub-if** | Associates a BFD session with a sub-interface. If a BFD session is bound to an interface, the BFD session status change affects the status of this interface and its sub-interfaces.  This parameter applies only to multicast IP single-hop BFD sessions. | - |
| **reboot-no-impact** | Indicates that the BFD session bound to an interface or sub-interface does not trigger the interface or sub-interface to go down when the initial state is Down after configuration restoration. | - |



Views
-----

BFD session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When transmission devices exist on a link and a fault occurs on the link, the devices on both ends of the link need a long time to detect the fault. To shorten the fault detection time, run the **process-interface-status** command to associate a multicast BFD session with an interface to trigger fast route convergence.

**Prerequisites**



A multicast IP single-hop BFD session or link-bundle single-hop BFD session has been configured.



**Configuration Impact**

If the **process-interface-status** command is run, the following situations occur:

* If a BFD session detects a fault and goes down, the associated interface status becomes BFD\_Down. As a result, the direct route of the interface is deleted from the routing table. The link layer status of the interface is not affected.
* The BFD session status will not be immediately reported to the interface (the BFD session may not be established or does not go Up when the command is run). This prevents the incorrect BFD status information from being reported to the interface and in turn causing an interface status error. If the BFD session status changes, the interface is notified of the change to ensure the association between the BFD session status and the interface status.

**Precautions**

* If multiple single-hop BFD sessions with a multicast IP address configured as the peer address are bound to the same interface, the **process-interface-status** command can be configured only for one BFD session. In other words, the interface status is affected by only one BFD session. Between link-bundle sessions and multicast sessions, and between link-bundle sessions, one interface can be bound to multiple BFD sessions enabled with the **process-interface-status** command. When an interface is bound to multiple BFD sessions that are associated with the interface status, the protocol status of the associated interface goes down as long as one BFD session is down. After the protocol status of the associated interface goes down, the protocol status of the associated interface goes up as long as one BFD session is up.
* Before you associate the BFD status with the interface status, ensure that the BFD configurations on two devices are correct and consistent. If the local BFD session is in the Down state, check whether the BFD configuration on the peer device is correct and whether the remote BFD session is shut down.
* If the BFD session status must be synchronized to the interface status immediately, ensure that the BFD configurations on the two devices are correct, and then run the shutdown and undo shutdown commands to shut down and start the BFD session. When the undo shutdown command is run in the BFD session view, a detection timer is initiated. If the BFD session goes up through negotiation before the timer expires, the BFD session notifies the bound interface of a BFD up event. Otherwise, the BFD session considers the link faulty and notifies the bound interface of a BFD down event. This way, the BFD session status is synchronized with the interface status in real time.
* After the shutdown command is run, the BFD session status will not be reported to the bound interface.
* If the process-interface-status [ sub-if ] command configured for a BFD session exists in the configuration file, after the device is restarted, the BFD session reports a BFD down event to the interface so that the interface sets its protocol state to Down. This prevents traffic loss when the BFD session is up but the interface is down during initialization of the device.
* The **process-interface-status** command associates a BFD session with the protocol status of the interface bound to the BFD session.
* After the **process-interface-status** command is run for a BFD session, the protocol status of the associated interface goes down after the device restarts. After the BFD session goes up or AdminDown, the protocol status of the associated interface goes up. If the interface protocol status is up before the restart, the BFD session cannot go up after the restart. As a result, the interface protocol status before and after the restart is inconsistent. You can run the process-interface-status reboot-no-impact command in the session view to prevent association.


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

# Associate the multicast IP single-hop BFD session with the interface to which the BFD session is bound.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] bfd s1 bind peer-ip default-ip interface 100GE 1/0/1
[*HUAWEI-bfd-session-s1] process-interface-status

```