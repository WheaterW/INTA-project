display license threshold
=========================

display license threshold

Function
--------



The **display license threshold** command displays the alarm threshold of a resource item in a global trotter license (GTL) file.



By default, the alarm threshold of a resource item in a GTL file is 90%.


Format
------

**display license threshold**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To identify resource exhaustion risks in advance, you can run the **set license threshold** command to configure alarm thresholds for resource items registered in the system. After this command is run, the system performs scheduled detection based on the configured alarm threshold. You can run the **display license threshold** command to view the alarm threshold of a resource item in a GTL file. When the usage of a resource item reaches the alarm threshold, the system sends the LCS\_1.3.6.1.4.1.2011.5.25.142.2.2 hwGtlResourceUsedUp alarm.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the alarm thresholds of resource items in a GTL file.
```
<HUAWEI> display license threshold
--------------------------------------------------------------------------------
ResourceItemName         Threshold Configurable Description                     
--------------------------------------------------------------------------------
*****VPN**                      90            1 NULL                            
*****ETSTM**                    77            1 NULL                            
*****40VA1C**                   90            0 NULL                            
*****40VA5C**                   90            0 NULL                            
*****40VAEC**                   95            1 NULL                            
--------------------------------------------------------------------------------

```

# Display the usage thresholds of sales items when activating a license file that supports the consistency between sales items and display items.
```
<HUAWEI> display license threshold
--------------------------------------------------------------------------------
ResourceItemName         Threshold Configurable Description
--------------------------------------------------------------------------------
*****0VA5C**                    95            1 XXXX Virtual Access Host License for 5 Client
*****0VA1C**                    80            1 XXXX Virtual Access Host License for 1 Client
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display license threshold** command output
| Item | Description |
| --- | --- |
| ResourceItemName | Name of a license resource item. |
| Threshold | Current alarm threshold of a license resource item. |
| Configurable | Whether the alarm threshold of a license resource item can be configured:   * 0: no. * 1: yes. |
| Description | Description of a license resource item. |