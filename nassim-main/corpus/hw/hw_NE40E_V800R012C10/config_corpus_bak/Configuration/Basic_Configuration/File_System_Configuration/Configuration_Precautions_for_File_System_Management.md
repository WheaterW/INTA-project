Configuration Precautions for File System Management
====================================================

Configuration_Precautions_for_File_System_Management

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| For details about the types and specifications of storage mediums, see "Specifications" in the Hardware Description. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| A file whose size is greater than or equal to 4 GB is not supported. For example, the file size cannot be correctly displayed in the dir command output. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| The available storage space of a file system is less than the maximum size of the physical storage. You can run the dir command to check the available space. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| The total length of the directory and file name in the file system cannot exceed 128 characters. The directory can contain 1 to 128 characters, and the file name can contain 1 to 128 characters. After a directory with the maximum length is created, files cannot be stored in the directory. After a file with the maximum length is created, files cannot be stored in subdirectories. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| The file name is case-sensitive. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |