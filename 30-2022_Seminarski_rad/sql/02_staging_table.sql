USE CO2_DW;
GO

CREATE TABLE StagingCO2Raw (
    Country NVARCHAR(100) NULL,
    Code NVARCHAR(10) NULL,
    CallingCode NVARCHAR(20) NULL,
    [Year] NVARCHAR(20) NULL,
    CO2Emission NVARCHAR(50) NULL,
    Population2022 NVARCHAR(50) NULL,
    Area NVARCHAR(50) NULL,
    PercentOfWorld NVARCHAR(20) NULL,
    Density NVARCHAR(20) NULL
);