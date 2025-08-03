bfd (session)
=============

bfd (session)

Function
--------



The **bfd** command displays a specified BFD session view.




Format
------

**bfd** *session-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *session-name* | Specifies the BFD configuration name. | The value is a string of 1 to 64 case-insensitive characters without spaces. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To enter the view of the specified BFD session before setting functional parameters for a created BFD session, run the **bfd session-name** command.

**Prerequisites**



A BFD session has been created using any of the following commands:bfd bind peer-ipbfd bind peer-ip default-ipbfd bind peer-ip source-ip autobfd bind peer-ipv6bfd bind peer-ipv6 source-ipv6 auto



**Follow-up Procedure**

After the BFD session view is displayed, you can perform the following operations:

* Run the **description** command to configure a description for the BFD session.
* Run the **min-tx-interval** command to set a desired minimum interval at which BFD packets are sent.
* Run the **min-rx-interval** command to set a desired minimum interval at which BFD packets are received.
* Run the **detect-multiplier** command to set a local detection multiplier for the BFD session.
* Run the **wtr** command to set a WTR time for the BFD session.

**Precautions**

* After the **bfd session-name** command is run, the BFD session view is displayed irrespective of whether the BFD session is Up.
* If the BFD session is in the Down state and you run the **bfd session-name** command to enter the BFD session view and set functional parameters, the configurations can immediately take effect. If you have run a command, for example, the **description** command before creating a BFD session, running the **description** command again overrides the original configuration after a BFD session is created and the BFD session view is displayed.
* You can run the **undo bfd** command to delete a specified BFD session.


Example
-------

# Enter the view of the BFD session named session.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] bfd session bind peer-ip 10.10.20.2
[*HUAWEI-bfd-session-session] quit
[*HUAWEI] bfd session
[*HUAWEI-bfd-session-session]

```