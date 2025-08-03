Overview of DIM
===============

Overview of DIM

#### Definition

Dynamic Integrity Measurement (DIM) is a code integrity measurement technology. It measures the code segment integrity of the running process memory and detects malicious attacks on the running process memory in a timely manner. The running process memory includes process code segment, shared library code segment, kernel, and kernel module.


#### Purpose

Malicious attacks on the running process memory are highly covert and cannot be detected through common methods such as trusted boot and file integrity check. In addition, more and more malware is used to attack the memory. Therefore, it is a must to improve the security detection capability of the device to detect malicious attacks on the running process memory in a timely manner. DIM can detect whether the running process memory is tampered with and whether the memory is changed due to injection attacks. Trusted boot only ensures that the device is trusted or detects untrusted boot behavior during device startup. File integrity check can detect whether static files are tampered with. The combination of DIM, trusted boot and file integrity check can ensure the reliability of the system in the entire running process.


#### Fundamentals

DIM can measure the running process memory whose content (process code segment, shared library code segment, kernel, and kernel module) remains unchanged. The principle of the DIM is to periodically or proactively detect a measurement object, calculate its actual hash value, and match the hash value with the baseline value preset in the software package. If the two values are inconsistent, the measurement object may be tampered with. Then the system saves the hash value to the PCRs of the HTM and records the corresponding stored measurement log (SML). The baseline value preset in the software package stores the reference hash value of the measurement object. The remote attestation (RA) server periodically initiates RA challenges to the device, obtains the PCR values and measurement logs generated during DIM on the device, verifies them based on the baseline file imported to the RA server, and generates a DIM trust report for the device.