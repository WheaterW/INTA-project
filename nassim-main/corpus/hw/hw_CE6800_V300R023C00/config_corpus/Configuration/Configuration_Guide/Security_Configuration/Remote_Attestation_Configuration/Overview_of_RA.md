Overview of RA
==============

Overview of RA

#### Definition

Trusted computing uses the Hardware Trust Module (HTM) as the root of trust and measures the booted components level by level throughout the entire boot process (from device power-on and BIOS boot, to GRUB and operating system kernel loading). It then saves the measurement result in the Platform Configure Registers (PCRs) of the HTM chip, and records the Storage Measurement Log (SML).

Remote Attestation (RA) is one of the key technologies used in trusted computing. RA calculates the actual status of a device based on the PCR values and SML obtained during device boot, and compares the actual status with the reference values in the baseline file to determine whether the device is trusted.


#### Purpose

Malicious actors might tamper with or replace communication devices and the system software they run, compromising security if such devices are connected to networks. In order to build a trusted network environment, each device must be therefore verified to ensure its identity before being connected to the network. RA, which is deployed independent of devices, enables customers to remotely audit each device's trust status, improving network security by preventing untrusted devices from accessing the network.