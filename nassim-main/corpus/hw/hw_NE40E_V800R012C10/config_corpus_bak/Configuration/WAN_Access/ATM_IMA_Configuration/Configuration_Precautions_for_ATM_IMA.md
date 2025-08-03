Configuration Precautions for ATM IMA
=====================================

Configuration_Precautions_for_ATM_IMA

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| The number of timeslots bound to the ATM serial interface to be added to an IMA group must be greater than or equal to 3. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K |
| In MC-LMSP scenarios, global IMA is not supported.  In LMSP unidirectional protection mode, global IMA is not supported. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K |
| After an IMA-group or serial sub-interface is added to an ATM-bundle interface, services on the ATM-bundle interface fail to be forwarded if PVC or PVP bidirectional mapping is not configured on ATM-bundle member interfaces. You can run the map pvc <vpi>/<vci> bidirectional command and the map pvp <remote-vpi> bidirectional command on an ATM-bundle member interface to configure PVC-PVP bidirectional mapping. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K |