Overview of Transmission Alarm Customization and Suppression
============================================================

Transmission alarm customization can control the impact of alarms on interface status. Transmission alarm suppression can efficiently suppress alarms, which prevents interfaces from frequently flapping.

#### Definition

Currently, carrier-class networks require high reliability for IP devices. As such, devices on the networks are required to rapidly detect faults. After fast detection is enabled on an interface, the alarm reporting speed is accelerated. As a result, the physical status of the interface frequently alternates between up and down, causing frequent network flapping. Therefore, alarms must be filtered and suppressed to prevent frequent network flapping.

Transmission alarm suppression can efficiently filter and suppress alarm signals to prevent interfaces from frequently flapping. In addition, transmission alarm customization can control the impact of alarms on the interface status.

Transmission alarm customization and suppression provide the following functions:

* Transmission alarm customization allows you to specify alarms that can cause the physical status of an interface to change. This function helps filter out unwanted alarms.
* Transmission alarm suppression allows you to suppress frequent network flapping by setting thresholds and using a series of algorithms.

#### Purpose

Transmission alarm customization allows you to filter unwanted alarms, and transmission alarm suppression enables you to set thresholds on customized alarms, allowing devices to ignore burrs generated during transmission link protection and preventing frequent network flapping.

On a backbone or metro network, IP devices are connected to transmission devices, such as Synchronous Digital Hierarchy (SDH), Wavelength Division Multiplexing (WDM), or Synchronous Optical Network (SONET) devices. If a transmission device becomes faulty, the interconnected IP device receives an alarm. The transmission devices then perform a link switchover. After the link of the transmission device recovers, the transmission device sends a clear alarm to the IP device. After an alarm is generated, a link switchover lasts 50 ms to 200 ms. In the log information on IP devices, the transmission alarms are displayed as burrs that last 50 ms to 200 ms. These burrs will cause the interface status of IP devices to switch frequently. IP devices will perform route calculation frequently. As a result, routes flap frequently, affecting the performance of IP devices.

From the perspective of the entire network, IP devices are expected to ignore such burrs. That is, IP devices must customize and suppress the alarms that are generated during transmission device maintenance or link switchovers. This can prevent route flapping. Transmission alarm customization can control the impact of transmission alarms on the physical status of interfaces. Transmission alarm suppression can efficiently filter and suppress specific alarm signals to avoid frequent interface flapping.