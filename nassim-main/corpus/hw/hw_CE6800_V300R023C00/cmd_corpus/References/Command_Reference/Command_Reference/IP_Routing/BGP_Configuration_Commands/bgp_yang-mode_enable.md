bgp yang-mode enable
====================

bgp yang-mode enable

Function
--------



The **bgp yang-mode enable** command enables the YANG management mode for BGP VPN instances and BGP multi-instance VPN instances.

The **undo bgp yang-mode enable** command disables the YANG management mode for BGP VPN instances and BGP multi-instance VPN instances.



By default, the YANG management mode of BGP and BGP multi-instance is disabled.


Format
------

**bgp yang-mode enable**

**undo bgp yang-mode enable**


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

To configure and manage BGP private network instances and BGP multi-instance private network instances in huawei-bgp.yang, you need to enable the YANG-based management mode of the BGP private network instances on the device or globally enable the leaf node (/bgp:bgp/bgp:global/bgp:yang-enable) through the YANG model file.

**Precautions**

Running the **bgp yang-mode enable** command changes the configurations of BGP VPN instances and their peers or peer groups on a device.If a command is supported in both the BGP-VPN instance view and BGP-VPN instance IPv4 address family view, the command can be run in either view before the **bgp yang-mode enable** command is run. After the **bgp yang-mode enable** command is run, the command can be run only in the BGP-VPN instance view. If the command has been run in the BGP-VPN instance IPv4 address family view, the configuration is automatically switched to the BGP-VPN instance view, which does not cause network interruption. However, if you roll back the command in the BGP-VPN instance view to the BGP-VPN instance IPv4 address family view, the command will be deleted and then delivered, causing network interruptions. Therefore, exercise caution when using the configuration rollback function in this case. After the **bgp yang-mode enable** command is run, the configuration that has been automatically converted is not modified, and the command can be run in either view.If a command is supported in both the BGP-VPN instance view and BGP-VPN instance IPv6 address family view, the command can be run in either view before the **bgp yang-mode enable** command is run. After the **bgp yang-mode enable** command is run, the command can be run only in the BGP-VPN instance view. If the command has been run in the BGP-VPN instance IPv6 address family view, the configuration is automatically switched to the BGP-VPN instance view, which does not cause network interruption. However, if you roll back the command in the BGP-VPN instance view to the BGP-VPN instance IPv6 address family view, the command will be deleted and then delivered, causing network interruptions. Therefore, exercise caution when using the configuration rollback function in this case. After the **bgp yang-mode enable** command is run, the configuration that has been automatically converted is not modified, and the command can be run in either view.After the **bgp yang-mode enable** command is run on a device, you cannot configure or manage BGP multi-instance VPN instances in bgp\_bgpmultiinstcomm.xsd using schemas. You can configure and manage BGP VPN instances in huawei-bgp.yang only using NETCONF YANG.After the **bgp yang-mode enable** command is run, the **as-number** command in the BGP-VPN instance IPv4 address family view and BGP-VPN instance IPv6 address family view is converted to the **as-number ipv4** and **as-number ipv6** commands in the BGP-VPN instance view.When peer groups with the same name exist in the BGP-VPN instance IPv4 private address family view and BGP-VPN instance IPv6 private address family view of the same VPN instance, after the **bgp yang-mode enable** command is run, the peer group name in the BGP-VPN instance IPv6 address family view is converted to a new peer group name.


Example
-------

# Enable the YANG management mode of BGP.
```
<HUAWEI> system-view
[~HUAWEI] bgp yang-mode enable
Warning: All the configurations of the BGP VPN instance and its peers and peer groups will be changed to configurations that can be delivered using the YANG model. Continue? [Y/N]:Y
[*HUAWEI]

```