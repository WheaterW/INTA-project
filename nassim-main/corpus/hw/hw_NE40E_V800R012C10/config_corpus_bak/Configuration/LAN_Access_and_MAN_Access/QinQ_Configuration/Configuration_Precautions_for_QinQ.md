Configuration Precautions for QinQ
==================================

Configuration_Precautions_for_QinQ

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| Vlink routes generated on Layer 3 sub-interfaces cannot be IP FRR routes. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| IP FRR does not support fast switching on QinQ VLAN tag termination sub-interfaces or dot1q VLAN tag termination sub-interfaces. IP FRR does not take effect. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Statistics about packets (such as ping packets) delivered by the CPU cannot be collected on a QinQ sub-interface. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |