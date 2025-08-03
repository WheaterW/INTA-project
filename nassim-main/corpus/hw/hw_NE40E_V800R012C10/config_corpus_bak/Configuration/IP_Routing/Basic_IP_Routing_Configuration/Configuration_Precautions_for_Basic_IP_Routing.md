Configuration Precautions for Basic IP Routing
==============================================

Configuration_Precautions_for_Basic_IP_Routing

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| Backup routes cannot be configured for mutual access between public and private networks. If backup routes are configured for public and private network routes, only the forwarding of public and private network routes is ensured. The forwarding of backup routes and the switchover between public and private network routes and their backup routes cannot be ensured.  Plan services properly. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |