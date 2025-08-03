Clearing Backup Information
===========================

Clearing backup information may interrupt services. Once the information is cleared, it cannot be restored. Therefore, exercise caution when performing this operation.

#### Procedure

1. Run the [**reset remote-backup-service**](cmdqueryname=reset+remote-backup-service) *rbs-name* **statistic** command to clear RBS statistics.
2. Run the [**reset multicast-rui statistic all**](cmdqueryname=reset+multicast-rui+statistic+all) command to clear statistics about backed up IGMP messages.