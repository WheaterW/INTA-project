mac-address learning priority allow-flapping
============================================

mac-address learning priority allow-flapping

Function
--------



The **mac-address learning priority allow-flapping** command allows MAC address flapping on interfaces with the same priority.

The **undo mac-address learning priority allow-flapping** command disables MAC address flapping on interfaces with the same priority.



By default, MAC address flapping is enabled on interfaces with the same priority.


Format
------

**mac-address learning priority** *priority-id* **allow-flapping**

**undo mac-address learning priority** *priority-id* **allow-flapping**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *priority-id* | MAC address learning priority. | The value is an integer ranging from 0 to 3. A larger value indicates a higher priority. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

For a device whose uplink interface connects to a server and downlink interface connects to user terminals, you can disable MAC address flapping on interfaces with the same MAC address learning priority to prevent unauthorized users from intruding the device by forging the server's MAC address. This mechanism prevents the interfaces from learning the same MAC address, and unauthorized users from interfering communication between this device and other devices by using forged MAC addresses.Both the mac-address learning priority and the **undo mac-address learning priority allow-flapping** commands helps improve network security. The differences are as follows:

* After the **undo mac-address learning priority allow-flapping** command is executed, the network device can learn forged MAC address after being powered off, but cannot learn correct MAC addresses after being powered on.
* After the **mac-address learning priority** command is executed, the network device can learn forged MAC address after being powered off, and can still learn correct MAC addresses after being powered on.

**Precautions**



You can configure the system to allow or forbid MAC address flapping with multiple priorities. If you run the mac-address learning priority <priority-id> allow-flapping command multiple times, all the configurations take effect.




Example
-------

# Enable MAC address flapping on interfaces with the priority of 1.
```
<HUAWEI> system-view
[~HUAWEI] mac-address learning priority 1 allow-flapping

```