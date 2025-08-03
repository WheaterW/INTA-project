display qos micro-burst peak-buffer verbose interface
=====================================================

display qos micro-burst peak-buffer verbose interface

Function
--------



The **display qos micro-burst peak-buffer verbose interface** command displays the peak buffer usage of an interface and the buffer usage of queues on the interface.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**display qos micro-burst peak-buffer verbose interface** { *interface-name* | *interface-type* *interface-number* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies the name of an interface. | The value is a string case-sensitive characters, spaces not supported. |
| *interface-type* | Specifies the type of an interface. | - |
| *interface-number* | Specifies the number of an interface. | The value is a string case-sensitive characters, spaces not supported. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



You can run the **display qos micro-burst peak-buffer verbose interface** command to view the peak buffer usage of an interface and the buffer usage of queues on the interface.



**Prerequisites**

1. The microburst detection function has been enabled on the device using the **qos micro-burst detection** [ **enhanced** ] **enable** command in the system view.
2. The microburst detection function has been enabled on an interface using the **qos micro-burst detection enable** command in the interface view.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the peak buffer usage and buffer usage of queues on 10GE1/0/1 in default microburst detection mode.
```
<HUAWEI> display qos micro-burst peak-buffer verbose interface 10GE 1/0/1
------------------------------------------------------------------------------------------------------------------------
 P-Buffer       Queue0     Queue1     Queue2     Queue3     Queue4     Queue5     Queue6     Queue7             DateTime
 (Bytes)       (Bytes)    (Bytes)    (Bytes)    (Bytes)    (Bytes)    (Bytes)    (Bytes)    (Bytes)
------------------------------------------------------------------------------------------------------------------------
 0                   0          0          0          0          0          0          0          0  2021-06-25 18:21:44
 0                   0          0          0          0          0          0          0          0  2021-06-25 18:16:44
 0                   0          0          0          0          0          0          0          0  2021-06-25 18:11:44
 0                   0          0          0          0          0          0          0          0  2021-06-25 18:06:44
 0                   0          0          0          0          0          0          0          0  2021-06-25 18:01:44
 0                   0          0          0          0          0          0          0          0  2021-06-25 17:56:44
 0                   0          0          0          0          0          0          0          0  2021-06-25 17:51:44
 0                   0          0          0          0          0          0          0          0  2021-06-25 17:46:44
 0                   0          0          0          0          0          0          0          0  2021-06-25 17:41:44
------------------------------------------------------------------------------------------------------------------------

```

**Table 1** Description of the **display qos micro-burst peak-buffer verbose interface** command output
| Item | Description |
| --- | --- |
| P-Buffer | Peak value of the buffer usage on the interface. |
| Queue0 | Buffer usage of queue 0. |
| Queue1 | Buffer usage of queue 1. |
| Queue2 | Buffer usage of queue 2. |
| Queue3 | Buffer usage of queue 3. |
| Queue4 | Buffer usage of queue 4. |
| Queue5 | Buffer usage of queue 5. |
| Queue6 | Buffer usage of queue 6. |
| Queue7 | Buffer usage of queue 7. |
| DateTime | Time when the device recorded the entry. |