Configuration Precautions for AAA and User Management for Administrator Users
=============================================================================

Configuration Precautions for AAA and User Management for Administrator Users

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| When a user is online, the user-dependent configurations, such as the user, user group, and user domain configurations, cannot be deleted. You need to manually log out the user and then attempt to delete the configurations. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| The RADIUS or HWTACACS template with the domain name removed cannot be bound to the management domain. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| The MIB NMS cannot be used to configure RADIUS authentication for management users. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |