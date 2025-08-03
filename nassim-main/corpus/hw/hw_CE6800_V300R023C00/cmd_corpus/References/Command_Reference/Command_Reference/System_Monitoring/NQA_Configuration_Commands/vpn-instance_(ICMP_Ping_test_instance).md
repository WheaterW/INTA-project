vpn-instance (ICMP Ping test instance)
======================================

vpn-instance (ICMP Ping test instance)

Function
--------



The **vpn-instance** command specifies a VPN instance for an NQA test instance.

The **undo vpn-instance** command deletes the VPN instance for an NQA test instance.



The default VPN instance in an NQA test instance is named \_public\_.


Format
------

**vpn-instance** *vrfName*

**undo vpn-instance**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vrfName* | Specifies the name of a VPN instance to which NQA test packets belong. The VPN instance is created using the ip vpn-instance command. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

NQA view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To specify a VPN instance for an NQA test instance, run the **vpn-instance** command.Before performing NQA tests on a VPN, specify a VPN instance for the NQA test instance.

**Configuration Impact**

The VPN instance must be already created and valid. Otherwise, the test instance fails. After the VPN is deleted, the NQA test instance that uses the VPN is deleted.

**Precautions**

If parameters need to be changed during the running of the test instance, the system prompts you whether to terminate the test instance. Press "Y" or "N" as required.

* If you press "Y", the test instance is terminated and parameters changed. The settings take effect after being committed. To restart the test instance, run the **start** command.
* If you press "N", the test instance keeps running, and the parameters fail to be modified.

Example
-------

# Specify a VPN instance for the test instance named user test.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vrf1
[*HUAWEI-vpn-instance-vrf1] quit
[*HUAWEI] nqa test-instance user test
[*HUAWEI-nqa-user-test] test-type icmp
[*HUAWEI-nqa-user-test] vpn-instance vrf1

```