Understanding HIPS
==================

Understanding HIPS

#### HIPS Detection Modules

After intruding into the underlying operating system of a device, a hacker configures and modifies the system for long-term control and further penetration. HIPS monitors the underlying operating system of the device in real time and provides detection modules described in [Table 1](#EN-US_CONCEPT_0000001512672398__table1771632310272). Once a suspicious event is detected, HIPS immediately sends the corresponding log.

**Table 1** HIPS detection modules
| Name | Description |
| --- | --- |
| File privilege escalation detection | After adding the SUID/SGID permission bit for executable files, a user can run high-risk commands even if the user logs in to the system as a common user later. HIPS sends the corresponding log when it detects that the SUID/SGID permission bit is added for executable files. |
| Abnormal shell detection | After intruding into a device successfully, a hacker may modify an existing shell of the device to facilitate the establishment of a control channel for a reverse shell. HIPS sends the corresponding log when it detects that a shell is modified. |
| Rootkit detection | A rootkit is a tool used by hackers to hide their tracks and retain root access during attacks. HIPS sends the corresponding log when it detects any system file that has rootkit characteristics on the device. |
| Key file tampering detection | After a successful intrusion, a hacker may modify key files or leave malicious files. HIPS sends the corresponding log when it detects that a key file is tampered with or a suspicious file exists in a key path. |
| Unauthorized root user detection | Each user has a user identity (UID), and UID 0 is reserved for the root user, making a non-root account with UID 0 highly suspicious. HIPS sends the corresponding log when it detects a non-root account with UID 0. |



#### Association Between HIPS and the NMS

After the NMS manages the device through NETCONF, HIPS can provide more functions. [Table 2](#EN-US_CONCEPT_0000001512672398__table15478225135217) describes the functions and how they are implemented.

**Table 2** Available functions after HIPS is associated with the NMS
| Function | Description | Implementation |
| --- | --- | --- |
| Policy file customization | The HIPS policy file contains the configuration and status of detection modules. The detection module configuration includes the monitoring list and whitelist information. The status of a detection module indicates whether the detection module is running after HIPS is enabled.  A detection module cannot be configured or independently enabled or disabled on the device â these can only be carried out on the NMS. | 1. The administrator customizes a policy file on the NMS GUI and applies the policy file. 2. The NMS sends a request to the NETCONF northbound interface (NBI) of the device to instruct the device to obtain the policy file from the NMS. 3. The device downloads the policy file from the NMS through SFTP. 4. The NMS instructs the device to apply the downloaded policy file. |
| HIPS log display | HIPS logs sent by the device are displayed on the NMS. | 1. The NMS sends a request to the NETCONF NBI of the device to subscribe to logs of the HIPS module from the device. 2. The device sends HIPS logs to the log server specified by the NMS through the information center. 3. The NMS displays the received logs on a specific page and prompts the administrator to process the logs. |