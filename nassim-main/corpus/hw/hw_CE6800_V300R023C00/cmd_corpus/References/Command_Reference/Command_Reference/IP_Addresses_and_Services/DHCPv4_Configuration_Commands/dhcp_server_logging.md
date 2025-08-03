dhcp server logging
===================

dhcp server logging

Function
--------

The **dhcp server logging** command enables the logging function during IP address allocation of the DHCP server in the interface view.

The **undo dhcp server logging** command disables the logging function during IP address allocation of the DHCP server in the interface view.

By default, the logging function during IP address allocation of the DHCP server is disabled.



Format
------

**dhcp server logging** [ **allocation-fail** | **allocation-success** | **release** | **renew-fail** | **renew-success** | **detect-conflict** | **recycle-conflict** ] \*

**undo dhcp server logging** [ **allocation-fail** | **allocation-success** | **release** | **renew-fail** | **renew-success** | **detect-conflict** | **recycle-conflict** ] \*



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **allocation-fail** | Displays logs when address allocation fails. | - |
| **allocation-success** | Displays logs when address allocation succeeds. | - |
| **release** | Displays logs when addresses are released. | - |
| **renew-fail** | Displays logs when address lease renewal fails. | - |
| **renew-success** | Displays logs when address lease renewal succeeds. | - |
| **detect-conflict** | Displays logs when address conflict occurs. | - |
| **recycle-conflict** | Displays logs when conflicting addresses are reclaimed. | - |




Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

This command is used on a DHCP server. When the DHCP server allocates IP addresses to clients, it records address allocation information to facilitate routine maintenance and fault location. After the logging function during IP address allocation of the DHCP server is configured using the **dhcp server logging** command, the DHCP server records logs about address allocation, conflict, lease renewal, and release.

Run the
**display ip pool interface interface-pool-name** command to check the status of the logging function during IP allocation of the DHCP server.

**Prerequisites**

1. IP addresses in the interface address pool have been configured using the **ip address** command.
2. The DHCP server function of the interface address pool has been enabled on interfaces using the **dhcp select interface** command.

**Precautions**

* With this logging function enabled, if a large number of DHCP clients request IP addresses from the DHCP server, the server frequently records logs. The server performance may therefore be affected.
* IP address allocation logs are recorded in the AM module. To view log information, the information center must be enabled. In addition, default settings for log output vary depending on various factors including the log level and output direction. For example, the level of logs indicating that an IP address is successfully allocated, an IP address is successfully renewed, and an IP address is successfully released is informational, and these logs are not recorded in the log buffer by default. You can run the **info-center source AM channel 4 log level informational** command to change the level of the logs to be recorded in the log buffer. You can then run the **display logbuffer** command to check the preceding logs.


Example
-------

# Enable the logging function during IP address allocation of the DHCP server on the interface
100GE
1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ip address 192.168.1.1 24
[*HUAWEI-100GE1/0/1] dhcp select interface
[*HUAWEI-100GE1/0/1] dhcp server logging

```