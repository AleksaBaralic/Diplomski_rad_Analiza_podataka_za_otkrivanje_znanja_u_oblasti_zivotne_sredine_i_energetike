USE CO2_DW;
GO

CREATE TABLE DimCountry (
    CountryKey INT IDENTITY(1,1) PRIMARY KEY,
    CountryName NVARCHAR(100) NOT NULL,
    ISOCode NVARCHAR(10) NULL,
    Population2022 BIGINT NULL,
    AreaKm2 FLOAT NULL,
    DensityKm2 FLOAT NULL,
    PercentOfWorldArea FLOAT NULL
);

CREATE TABLE DimYear (
    YearKey INT IDENTITY(1,1) PRIMARY KEY,
    [Year] INT NOT NULL,
    Decade INT NOT NULL,
    Century INT NOT NULL,
    Era NVARCHAR(30) NOT NULL
);

CREATE TABLE FactCO2Emission (
    FactKey INT IDENTITY(1,1) PRIMARY KEY,
    CountryKey INT NOT NULL FOREIGN KEY REFERENCES DimCountry(CountryKey),
    YearKey INT NOT NULL FOREIGN KEY REFERENCES DimYear(YearKey),
    CumulativeEmissionTons DECIMAL(20,2) NOT NULL,
    AnnualEmissionTons DECIMAL(20,2) NULL
);