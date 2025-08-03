Configuration Precautions for Configuration Management
======================================================

Configuration_Precautions_for_Configuration_Management

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| 1. The best-effort rollback principle is used for configuration rollback. If configuration differences still exist after the rollback is complete, the system prompts you to view the configurations that are not rolled back, but the operation log records an operation success.  2. If configuration differences still exist after the rollback is completed through NETCONF, a message is displayed, indicating that the operation is successful. You can check the differences between the target rollback point and the current running configuration to determine whether all configurations have been rolled back.  3. During the configuration rollback, do not insert, replace, or reset a board. Otherwise, the board cannot be registered. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| If multiple users commit configurations at the same time, the operation may fail due to the conflict. A message indicating that the system is busy is displayed. Configurations need to be committed again. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| When the system is committing configurations or rolling back, there is a possibility that the card that is newly started cannot be registered for a long time. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Configuration change is not allowed when an NMS initiates full synchronization to the device. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| When configurations are restored during device startup, you cannot query the current configurations. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| In two-phase configuration validation mode, the number of uncommitted configurations are limited. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| After the trial run command is executed to enable the device to enter the trial running state, only the current trial running user can modify the configuration. Other users cannot modify the configuration during the trial run. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| During configuration editing, if the device memory usage exceeds 90%, the configuration editing fails. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| The configuration cannot be saved during configuration data restoration when the device is just started. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Configurations cannot be committed when configuration data is being restored upon device startup. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| When the configuration difference comparison command is being executed, if repeated commands exist in the same view, the current command fails to be executed. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |