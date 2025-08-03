domainname-parse-direction (aaa-view)
=====================================

domainname-parse-direction (aaa-view)

Function
--------

The **domainname-parse-direction** command configures the direction in which a domain name is parsed.

The **undo domainname-parse-direction** command restores the default direction in which a domain name is parsed.

By default, the domain name is parsed in the AAA view from left to right.



Format
------

**domainname-parse-direction** { **left-to-right** | **right-to-left** }

**undo domainname-parse-direction**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **left-to-right** | Parses a domain name form left to right. | - |
| **right-to-left** | Parses a domain name form right to left. | - |




Views
-----

AAA view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

In AAA implementations, users belong to different domains. A network access server (NAS) centrally manages users in a domain. During a user's login, the NAS parses the entered user name. A user is authenticated only when the user has the correct user name and domain name. When configuring an AAA scheme, run the domainname-parse-direction { left-to-right | right-to-left } command to configure the direction in which a domain name is parsed.Assume that the user name is username@dom1@dom2.- If the **domain-location** command configures the domain name behind the domain name delimiter:- When left-to-right is specified, the user name is username and the domain name is dom1@dom2.- When right-to-left is specified, the user name is username@dom1 and the domain name is dom2.- If the **domain-location** command configures the domain name before the domain name delimiter:- When left-to-right is specified, the user name is dom1@dom2 and the domain name is username.- When right-to-left is specified, the user name is dom2 and the domain name is username@dom1.

**Precautions**

If you run the domainname-parse-direction command in the AAA view, the direction in which a domain name is parsed is configured globally and the configuration takes effect for all users.



Example
-------

# Configure the device to parse a domain name from right to left in the AAA view.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] domainname-parse-direction right-to-left

```