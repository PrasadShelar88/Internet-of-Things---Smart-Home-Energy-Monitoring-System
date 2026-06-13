from pydantic import BaseModel, Field
from typing import Optional


class EnergyReadingInput(BaseModel):
    voltage: float = Field(..., ge=0, le=300, description="Voltage in volts")
    current: float = Field(..., ge=0, le=100, description="Current in amperes")
    appliance: str = Field(default="Main Circuit", description="Appliance or circuit name")
    duration_minutes: float = Field(default=1, gt=0, le=1440, description="Measurement duration")


class ThresholdConfig(BaseModel):
    max_power_watts: float = Field(default=1500, gt=0)
    max_current_amps: float = Field(default=10, gt=0)
    electricity_rate_per_kwh: float = Field(default=8.0, gt=0)


class RelayCommand(BaseModel):
    status: str = Field(..., pattern="^(ON|OFF)$", description="Relay status: ON or OFF")
