port crc-statistics trigger error-down
======================================

port crc-statistics trigger error-down

Function
--------



The **port crc-statistics trigger error-down** command configures an interface to transit to the Error-Down state when the number of received CRC error packets reaches the alarm threshold.

The **undo port crc-statistics trigger error-down** command disables an interface from transiting to the Error-Down state when the number of received CRC error packets reaches the alarm threshold.



By default, an interface does not transit to the Error-Down state when the number of received CRC error packets reaches the alarm threshold.


Format
------

**port crc-statistics trigger error-down**

**undo port crc-statistics trigger error-down**


Parameters
----------

None

Views
-----

Layer 2 100GE interface view,100GE interface view,Layer 2 10GE interface view,10GE interface view,Layer 2 200GE interface view,200GE interface view,25GE-L2 view,25GE interface view,400GE-L2 view,400GE interface view,Layer 2 50GE interface view,50GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If an interface receives CRC error packets, faults such as packet loss occur on the link. If a backup link is configured on an Ethernet interface, you can configure the interface to transit to the Error-Down state when the number of received CRC error packets reaches the alarm threshold. In this manner, services can be switched to the backup link in a timely manner, ensuring correct data transmission. When a device detects a fault on an interface, the device sets the interface status to Error-Down. The interface cannot send or receive packets, and the interface indicator is off.You can run the **trap-threshold crc-statistics** command to set the alarm threshold for the number of CRC error packets and the alarm interval.

**Follow-up Procedure**

If an interface is in Error-Down state, you are advised to find out the cause of the Error-Down event first. If the two connected interfaces are optical interfaces, check whether optical modules and fiber on the interfaces are securely installed or fail. If the two connected interfaces are electrical interfaces, check whether the network cable is securely connected to the interfaces or fails.An interface in Error-Down state can be recovered using either of the following methods:

* Manual recovery (after an Error-Down event occurs):If a few interfaces need to be recovered, run the **shutdown** and **undo shutdown** commands in the interface view. Alternatively, run the undo port crc-statistics trigger error-down, run the **restart** command in the interface view to restart the interfaces, or remove and reinstall the transmission medium on optical interfaces.
* Automatic recovery (before an Error-Down event occurs):If a large number of interfaces need to be recovered, manual recovery is time consuming and some interfaces may be omitted. To avoid this problem, you can run the **error-down auto-recovery cause crc-statistics interval** command in the system view to enable automatic interface recovery and set the recovery delay time. You can run the **display error-down recovery** command to view information about automatic interface recovery.

Example
-------

# Configure 100GE1/0/1 to transit to the Error-Down state when the number of received error packets reaches the alarm threshold.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] port crc-statistics trigger error-down

```