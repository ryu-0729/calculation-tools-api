import enum

from pydantic import BaseModel, Field


class OverTimeHour(enum.Enum):
    SEVENTEEN = "17"
    EIGHTEEN = "18"
    NINETEEN = "19"
    TWENTY = "20"
    TWENTY_ONE = "21"
    TWENTY_TWO = "22"


class OverTimeMinute(enum.Enum):
    ZERO = "0"
    FIFTEEN = "15"
    THIRTY = "30"
    FORTY_FIVE = "45"


class GetOverTimeRequest(BaseModel):
    start_hour: OverTimeHour = Field(..., description="残業開始時間")
    start_minute: OverTimeMinute = Field(..., description="残業開始分")
    end_hour: OverTimeHour = Field(..., description="残業終了時間")
    end_minute: OverTimeMinute = Field(..., description="残業終了分")


class GetOverTimeResponse(BaseModel):
    over_time: str = Field(..., description="残業時間(10進法表記)")
