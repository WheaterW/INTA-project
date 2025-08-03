accounting-scheme (aaa domain view)
===================================

accounting-scheme (aaa domain view)

Function
--------

The **accounting-scheme** command applies an accounting scheme to a domain.

The **undo accounting-scheme** command restores the default accounting scheme of a domain.

By default, the accounting scheme named default is applied to a domain. In this default accounting scheme, non-accounting is used and the real-time accounting function is disabled.



Format
------

**accounting-scheme** *accounting-scheme-name*

**undo accounting-scheme**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *accounting-scheme-name* | Specifies the name of an accounting scheme. | The accounting scheme must already exist. |




Views
-----

AAA domain view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

To charge users in a domain, create an accounting scheme and perform configurations in the accounting scheme, for example, set the accounting mode and policy for accounting-start failures. Run the accounting-scheme command in the AAA domain view to apply the accounting scheme to the domain.

**Prerequisites**

An accounting scheme has been created and configured using the accounting-scheme command. For example, the accounting mode and policy for accounting-start failures have been configured.



Example
-------

# Apply the accounting scheme account1 to the domain isp1.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] accounting-scheme account1
[*HUAWEI-aaa-accounting-account1] quit
[*HUAWEI-aaa] domain isp1
[*HUAWEI-aaa-domain-isp1] accounting-scheme account1

```

# Restore the default accounting scheme of the domain isp2.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] domain isp2
[*HUAWEI-aaa-domain-isp2] undo accounting-scheme

```