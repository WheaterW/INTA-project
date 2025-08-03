set ztp
=======

set ztp

Function
--------



The **set ztp enable** command enables the ZTP function on a device.

The **set ztp disable** command disables the ZTP function on a device.



By default, the ZTP function is enabled on a device.


Format
------

**set ztp** { **enable** | **disable** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **enable** | Enable the ZTP function on the device. | - |
| **disable** | Disable the ZTP function on the device. | - |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

By default, a device automatically starts the ZTP process after it is powered on and started without a configuration file. If you do not want to perform ZTP when a device starts without any configuration file, run the **set ztp disable** command to disable the ZTP function.

**Configuration Impact**

If you run the **set ztp disable** command during ZTP, the ZTP process is terminated and the configuration is rolled back to the status before the deployment.

**Precautions**



If you want to enable ZTP again after running the **set ztp disable** command to disable ZTP, run the **set ztp enable** command to enable ZTP before the next startup with factory configuration or empty configuration.




Example
-------

# Disable the ZTP function on a device.
```
<HUAWEI> set ztp disable
Info:The ZTP process will be terminated. When restarting without a configuration file, the device will not start the ZTP process.

```

# Enable the ZTP function on a device.
```
<HUAWEI> set ztp enable
Info:When starting without a configuration file, the device will start the ZTP process.

```