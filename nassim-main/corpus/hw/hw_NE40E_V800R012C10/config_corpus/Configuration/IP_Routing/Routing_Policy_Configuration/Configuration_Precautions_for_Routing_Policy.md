Configuration Precautions for Routing Policy
============================================

Configuration Precautions for Routing Policy

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| It is recommended that the number of nodes in each route-policy in the system be less than 1000. If the number exceeds 1000, the service processing performance of the route-policy will deteriorate and user experience is affected. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| If more than one node is defined in a route-policy or another type of filter, at least one of them must be in permit mode; otherwise, all routes may be denied. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| If the route-policy nonexistent-config-check disable command is not run, nonexistent route-policies cannot be applied to services. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |