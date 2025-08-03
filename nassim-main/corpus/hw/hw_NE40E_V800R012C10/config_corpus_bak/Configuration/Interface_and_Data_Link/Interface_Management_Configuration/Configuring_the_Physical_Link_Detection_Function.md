Configuring the Physical Link Detection Function
================================================

The physical link detection function helps reduce the number of alarms generated on links and avoid system performance degradation caused by plenty of alarms that would be otherwise generated.

#### Usage Scenario

When plenty of alarms are generated on links, system performance deteriorates because the system has to process the huge number of alarms. You can set thresholds for different types of alarms, so that alarms are generated only when the alarm thresholds are reached. In addition, measures can be taken when necessary to remove faults and guarantee the transmission of normal traffic.


#### Pre-configuration Tasks

Before configuring physical link detection, complete the following tasks:

* Power on the Router and ensure that the Router passes the self-check.
* Configure physical attributes for interfaces on the Router.


[Configuring the Alarm Function for CRC Errors, SDH Errors, Input Errors, Output Errors, or Optical Module Power Exceptions](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ifm_cfg_6002.html)

This section describes how to configure the alarm function for CRC errors, SDH errors, input errors, output errors, or optical module power exceptions.

[Configuring the Alarm Function for Pause-Frame Errors Received on an Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ifm_cfg_7010.html)

This section describes how to configure the alarm function for pause-frame errors received on an interface.

[Configuring the Alarm Function in Case the Number of SDH B1 or SDH B2 Error Packets That an Interface Receives Exceeds an Alarm Threshold](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ifm_cfg_6007.html)

You can configure the alarm function in case the number of SDH B1 or SDH B2 error packets exceeds an alarm threshold. If such an alarm is generated, the link is in a poor condition.

[Configuring the Alarm Function in Case the Number of Bytes of Error Packets That an Interface Receives Exceeds an Alarm Threshold](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ifm_cfg_6006.html)

You can configure the alarm function in case the number of bytes of error packets exceeds a threshold. If such an alarm is generated, the link is in a poor condition.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_ifm_cfg_3005.html)

You can check the interface configuration and state information after configuring the physical link detection function.