if-match ip-prefix
==================

if-match ip-prefix

Function
--------



The **if-match ip-prefix** command sets a filtering rule that is based on the IP prefix list.

The **undo if-match ip-prefix** command cancels the configuration.



By default, no filtering rule based on the IP prefix list is set.


Format
------

**if-match ip-prefix** *ip-prefix-name*

**undo if-match ip-prefix** *ip-prefix-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-prefix-name* | Specifies the name of the IP prefix list. | The name is a string of 1 to 169 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

Route-policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After an IP prefix list is configured as a filtering rule of a route-policy on a device, the device uses the IP prefix list to match routes, and permits or denies the routes that match the IP prefix list.The **ip ip-prefix** command must be used to configure an IP prefix so that the filtering rule configured using the **if-match ip-prefix** command can take effect. For example:

* If the if-match ip-prefix aa command is used but the IP prefix named aa is not configured, all routes are permitted.
* If the if-match ip-prefix aa command is used after the ip ip-prefix aa permit 1.1.1.1 32 command is used, the routes with the IP prefix 1.1.1.1 and the mask 32 are permitted.

**Prerequisites**



An ip-prefix list has been configured using the **ip ip-prefix** command and a route-policy has been configured using the route-policy command.



**Configuration Impact**



When you filter routes based on the IP prefixes, the routes that match the filtering rule are permitted and the routes that do not match the filtering rule are denied.



**Precautions**



The if-match ip-prefix and if-match acl commands are mutually exclusive. That is, in the same route-policy node, the later if-match acl configuration overrides the previous if-match ip-prefix configuration. In the same route-policy node, the later if-match ip-prefix configuration overrides the previous if-match ip-prefix configuration.




Example
-------

# Set a filtering rule based on the IP prefix list named p1.
```
<HUAWEI> system-view
[~HUAWEI] ip ip-prefix p1 permit 192.168.1.1 32
[~HUAWEI] route-policy policy permit node 10
[*HUAWEI-route-policy] if-match ip-prefix p1

```