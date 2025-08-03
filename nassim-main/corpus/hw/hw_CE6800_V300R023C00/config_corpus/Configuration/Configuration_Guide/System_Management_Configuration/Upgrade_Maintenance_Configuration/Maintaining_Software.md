Maintaining Software
====================

Maintaining Software

#### Procedure

During routine maintenance, check the version number of the basic software package and delete the software files that are no longer used to ensure the normal running of the system.

[Table 1](#EN-US_TASK_0000001512690098__table141227425571) describes operations related to software package maintenance.

**Table 1** Operations related to software package maintenance
| **Operation** | **Command** | **Description** |
| --- | --- | --- |
| Check the software version. | [**display version**](cmdqueryname=display+version) **slot** *slot-id* | You can view the current software version to determine whether the device needs to be upgraded or has been upgraded successfully. |
| Delete the patch package that takes effect at the next startup. | [**reset patch-configure**](cmdqueryname=reset+patch-configure) **next-startup** | - |
| Delete the feature package that takes effect at the next startup. | [**reset feature-software next-startup**](cmdqueryname=reset+feature-software+next-startup) | - |
| Verify file integrity. | [**check software file-name**](cmdqueryname=check+software+file-name) *file-name* | System software packages, patch files, feature software packages, and module files can be verified. |
| Verify patch file integrity. | [**check patch**](cmdqueryname=check+patch) { *filename* | [**startup**](cmdqueryname=startup) } | - |
| Verify module file integrity. | [**check module**](cmdqueryname=check+module) { *filename* | [**startup**](cmdqueryname=startup) } | - |
| Check whether the running software package is reliable. | [**display software info**](cmdqueryname=display+software+info) | - |
| Check whether the rollback function is enabled on the device. | [**display upgrade rollback-timer**](cmdqueryname=display+upgrade+rollback-timer) | - |
| Check the digital signature certificate revocation list (CRL). | [**display software crl**](cmdqueryname=display+software+crl) | - |