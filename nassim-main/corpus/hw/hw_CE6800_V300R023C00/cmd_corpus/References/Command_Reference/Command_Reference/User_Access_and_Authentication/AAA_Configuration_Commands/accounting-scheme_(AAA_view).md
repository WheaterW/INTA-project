accounting-scheme (AAA view)
============================

accounting-scheme (AAA view)

Function
--------

The **accounting-scheme** command creates an accounting scheme and displays the accounting scheme view.

The **undo accounting-scheme** command deletes an accounting scheme.

By default, there is an accounting scheme named default in the system. This default accounting scheme can be modified but cannot be deleted. In this default accounting scheme, non-accounting is used and the real-time accounting function is disabled.



Format
------

**accounting-scheme** *accounting-scheme-name*

**undo accounting-scheme** *accounting-scheme-name*



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *accounting-scheme-name* | Specifies the name of an accounting scheme. | The value is a string of 1 to 32 case-sensitive characters. It cannot contain spaces or the following symbols: / \ : \* ? " < > |. The value cannot be - or --. |




Views
-----

AAA view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

To charge users in a domain, create and configure an accounting scheme, for example, the accounting mode and policy for accounting-start failures. Run the **accounting-scheme** command in the AAA domain view to apply the accounting scheme to the domain.

**Follow-up Procedure**

After an accounting scheme is created:

* Run the **accounting interim-fail** command to set the maximum number of real-time accounting failures and configure a policy used after a real-time accounting failure.
* Run the **accounting realtime** command to enable the real-time accounting function and set the interval for real-time accounting in an accounting scheme.
* Run the **accounting start-fail** command to configure a policy for accounting-start failures.
* Run the **accounting-mode** command to configure an accounting mode in an accounting scheme.After an accounting scheme is configured, run the **accounting-scheme** command in the AAA domain view to apply the accounting scheme to a domain.

**Precautions**

If the configured accounting scheme does not exist, the **accounting-scheme** command in the AAA view creates an accounting scheme and displays the accounting scheme view. If the configured accounting scheme already exists, the **accounting-scheme** command in the AAA view displays the accounting scheme view directly.

To delete an accounting scheme applied to a domain, run the undo accounting-scheme (AAA domain view) command.

Example
-------

# Create an accounting scheme named scheme1.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] accounting-scheme scheme1
[*HUAWEI-aaa-accounting-scheme1]

```

# Enter the default accounting scheme view.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] accounting-scheme default
[*HUAWEI-aaa-accounting-default]

```