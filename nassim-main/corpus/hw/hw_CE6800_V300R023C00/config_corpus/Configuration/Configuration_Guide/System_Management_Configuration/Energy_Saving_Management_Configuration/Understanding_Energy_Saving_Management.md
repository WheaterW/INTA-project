Understanding Energy Saving Management
======================================

Understanding Energy Saving Management

#### Energy Saving Management Features Supported by a Device

The following energy saving features are supported:

* **Intelligent fan speed adjustment**
  
  Intelligent fan speed adjustment monitors the temperature of key components, enabling the device to run at normal temperatures while reducing power consumption and noise. The fan speed is increased if a sensitive component overheats and decreased when the temperature falls back to its normal range.
* **Automatic laser shutdown (ALS)**
  
  The automatic laser shutdown (ALS) function controls the laser pulse of an optical module by detecting the Loss of Signal (LOS) on an optical interface. It provides protection for users while reducing energy consumption for users.
  
  If ALS is disabled and the optical fiber fails or is not properly installed, data communication is interrupted. In this case, the optical interface and the laser continue to operate, with the laser continuing to emit pulses. This wastes energy and risks damaging an operator's eyes.
  
  Conversely, if ALS is enabled in the preceding scenario, the system automatically disables the laser from emitting pulses after detecting the LOS on the optical interface. When the system detects that the LOS is cleared after the optical fiber is installed or recovers, it enables the laser to resume emitting pulses.
* **Energy Efficient Ethernet (EEE)**
  
  Energy Efficient Ethernet (EEE) reduces system power consumption by dynamically adjusting the electrical interface power according to network traffic volume.
  
  Without EEE configured, the system provides power to every interface, resulting in idle interfaces using the same amount of power as active interfaces. With EEE configured, the system automatically reduces the power supply for idle interfaces, reducing the overall energy consumption of the system. Power supply is restored when the interface starts to transmit data.
* **Shutting down idle circuits and components**
  
  The device shuts down circuits and components based on their usage. Those that are not in use are shut down to save energy. For example, when an optical module is unavailable on the interface, the device shuts down related circuits that are not used. When the optical module is installed, the device automatically starts up the related circuits.
* **Powering off redundant power modules**
  
  The device powers off redundant power modules based on rated or real-time power consumption. This saves energy without affecting the power supply of the device. When the rated or real-time power consumption increases, the device automatically powers on redundant power modules, ensuring stable power supply.