Configuration Precautions for Dual-Device Backup
================================================

Configuration_Precautions_for_Dual-Device_Backup

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| E-Trunk dual-device hot backup for ARP services does not support master/backup switchover if an Eth-Trunk sub-interface fails. If an Eth-Trunk sub-interface fault occurs, E-Trunk dual-device hot backup does not take effect. As a result, user traffic is interrupted. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| E-Trunk dual-device hot backup does not support a master/backup switchover if an Eth-Trunk sub-interface fails. If an Eth-Trunk sub-interface fault occurs, E-Trunk dual-device hot backup does not take effect. As a result, user traffic is interrupted. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| E-Trunk dual-device hot backup for IGMP services does not support a master/backup switchover if an Eth-Trunk sub-interface fails. If an Eth-Trunk sub-interface fault occurs, E-Trunk dual-device hot backup does not take effect. As a result, user traffic is interrupted. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| E-Trunk dual-device hot backup for IPsec services does not support a master/backup switchover if an Eth-Trunk sub-interface fails. If an Eth-Trunk sub-interface fault occurs, E-Trunk dual-device hot backup does not take effect. As a result, user traffic is interrupted. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| RBS allows different backup modes to be configured, but the three backup modes apply to different services.  Hot backup: applies to all services.  Warm backup: inapplicable to all services.  Virtual backup: applies only to BRAS services.  Currently, some services are mutually exclusive with the backup mode through commands, and some services are not mutually exclusive. For example, virtual backup is not displayed in the current configuration, but it does not take effect for other services except the BRAS service. This does not affect functions. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |