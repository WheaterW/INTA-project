Configuration Precautions for Upgrade Maintenance
=================================================

Configuration Precautions for Upgrade Maintenance

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| The patch to be loadded must be the incremental patch for already installed patches. Otherwise, unload the existing patches and then load the new patch. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| The MOD package version must match the system software package version. If the MOD package version does not match the system software package version, the MOD package cannot be loaded. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Patch operations cannot be performed during service configuration. Otherwise, the patch operations may fail. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |