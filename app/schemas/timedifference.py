import enum

from pydantic import BaseModel, Field


class TimeDifferenceHour(enum.Enum):
    ZERO = "0"
    ONE = "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    ELEVEN = "11"
    TWELVE = "12"
    THIRTEEN = "13"
    FOURTEEN = "14"
    FIFTEEN = "15"
    SIXTEEN = "16"
    SEVENTEEN = "17"
    EIGHTEEN = "18"
    NINETEEN = "19"
    TWENTY = "20"
    TWENTY_ONE = "21"
    TWENTY_TWO = "22"
    TWENTY_THREE = "23"
    TWENTY_FOUR = "24"


class TimeDifferenceMinute(enum.Enum):
    ZERO = "0"
    FIFTEEN = "15"
    THIRTY = "30"
    FORTY_FIVE = "45"


class GetTimeDifferenceRequest(BaseModel):
    start_hour: TimeDifferenceHour = Field(..., description="残業開始時間")
    start_minute: TimeDifferenceMinute = Field(..., description="残業開始分")
    end_hour: TimeDifferenceHour = Field(..., description="残業終了時間")
    end_minute: TimeDifferenceMinute = Field(..., description="残業終了分")


class GetTimeDifferenceResponse(BaseModel):
    over_time: str = Field(..., description="残業時間(10進法表記)")
